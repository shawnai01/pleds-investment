#!/usr/bin/env python3
"""
PLEDS Regime Sentinel — 선제적 레짐 감지
5개 지표 임계치 모니터링

Usage:
  python3 data/regime-sentinel.py
  
Output: JSON with indicators, alerts, status
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta

FRED_KEY = os.environ.get('FRED_API_KEY')
TWELVE_KEY = os.environ.get('TWELVEDATA_API_KEY')

# Thresholds
THRESHOLDS = {
    'VIX': {'value': 25, 'operator': '>'},
    '2-10 Spread': {'value': 0, 'operator': '<'},
    'HY Spread': {'value': 400, 'operator': '>'},
    'BTC Weekly %': {'value': -15, 'operator': '<'},
    'DXY Monthly %': {'value': 3, 'operator': '>'}
}


def get_vix():
    """Yahoo Finance v8 API for VIX"""
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=1d"
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        data = r.json()
        return round(data['chart']['result'][0]['meta']['regularMarketPrice'], 2)
    except Exception as e:
        print(f"[WARN] VIX fetch failed: {e}", file=sys.stderr)
        return None


def get_yield_spread():
    """FRED: 10Y - 2Y spread (T10Y2Y series)"""
    if not FRED_KEY:
        print("[WARN] FRED_API_KEY not set", file=sys.stderr)
        return None
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=T10Y2Y&api_key={FRED_KEY}&file_type=json&limit=1&sort_order=desc"
        r = requests.get(url, timeout=10)
        data = r.json()
        val = data['observations'][0]['value']
        if val == '.':
            return None
        return round(float(val) * 100, 0)  # Convert to basis points
    except Exception as e:
        print(f"[WARN] Yield spread fetch failed: {e}", file=sys.stderr)
        return None


def get_hy_spread():
    """FRED: High Yield Spread (BAMLH0A0HYM2)"""
    if not FRED_KEY:
        return None
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=BAMLH0A0HYM2&api_key={FRED_KEY}&file_type=json&limit=1&sort_order=desc"
        r = requests.get(url, timeout=10)
        data = r.json()
        val = data['observations'][0]['value']
        if val == '.':
            return None
        return round(float(val) * 100, 0)  # Convert to basis points
    except Exception as e:
        print(f"[WARN] HY spread fetch failed: {e}", file=sys.stderr)
        return None


def get_btc_weekly():
    """CoinGecko: BTC 7-day change"""
    try:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false"
        r = requests.get(url, timeout=10)
        data = r.json()
        return round(data['market_data']['price_change_percentage_7d'], 2)
    except Exception as e:
        print(f"[WARN] BTC weekly fetch failed: {e}", file=sys.stderr)
        return None


def get_dxy_monthly():
    """Yahoo Finance: DXY (DX-Y.NYB) 30-day change"""
    try:
        # Use Yahoo Finance for DXY as Twelve Data doesn't support it directly
        url = "https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?interval=1d&range=1mo"
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        data = r.json()
        
        result = data.get('chart', {}).get('result', [])
        if not result:
            return None
        
        closes = result[0].get('indicators', {}).get('quote', [{}])[0].get('close', [])
        closes = [c for c in closes if c is not None]
        
        if len(closes) < 15:
            return None
        
        current = closes[-1]
        month_ago = closes[0]
        return round(((current - month_ago) / month_ago) * 100, 2)
    except Exception as e:
        print(f"[WARN] DXY monthly fetch failed: {e}", file=sys.stderr)
        return None


def check_threshold(name, value):
    """Check if indicator breaches threshold"""
    if value is None:
        return None  # Unknown
    
    threshold = THRESHOLDS[name]
    if threshold['operator'] == '>':
        return value > threshold['value']
    else:  # '<'
        return value < threshold['value']


def check_regime():
    """Main regime check function"""
    # Collect all indicators
    indicators = {
        'VIX': get_vix(),
        '2-10 Spread': get_yield_spread(),
        'HY Spread': get_hy_spread(),
        'BTC Weekly %': get_btc_weekly(),
        'DXY Monthly %': get_dxy_monthly()
    }
    
    alerts = []
    
    for name, value in indicators.items():
        if value is None:
            continue
        
        breached = check_threshold(name, value)
        if breached:
            threshold = THRESHOLDS[name]
            alerts.append({
                'indicator': name,
                'value': value,
                'threshold': f"{threshold['operator']}{threshold['value']}"
            })
    
    # Determine status
    alert_count = len(alerts)
    if alert_count == 0:
        status = '🟢 정상'
    elif alert_count == 1:
        status = '🟡 주의'
    elif alert_count == 2:
        status = '🟠 경고'
    else:  # 3+
        status = '🔴 레짐전환'
    
    # Build indicator status table
    indicator_status = {}
    for name, value in indicators.items():
        if value is None:
            indicator_status[name] = {'value': None, 'status': '⚪ 미수집'}
        else:
            breached = check_threshold(name, value)
            indicator_status[name] = {
                'value': value,
                'threshold': f"{THRESHOLDS[name]['operator']}{THRESHOLDS[name]['value']}",
                'status': '🔴' if breached else '🟢'
            }
    
    return {
        'timestamp': datetime.now().isoformat(),
        'indicators': indicator_status,
        'alerts': alerts,
        'alert_count': alert_count,
        'status': status,
        'action': _get_action(alert_count)
    }


def _get_action(alert_count):
    if alert_count == 0:
        return "상태 표시만"
    elif alert_count == 1:
        return "모니터링 강화"
    elif alert_count == 2:
        return "Macro 긴급 재판정 권고, Shawn 알림"
    else:
        return "전 포지션 재검토, Shawn 즉시 알림"


def format_markdown(result):
    """Format result as markdown for daily briefing"""
    lines = [
        "## 🚦 Regime Sentinel",
        f"**상태:** {result['status']} ({result['alert_count']}/5 임계치 돌파)",
        f"**액션:** {result['action']}",
        "",
        "| 지표 | 현재값 | 임계치 | 상태 |",
        "|------|--------|--------|------|"
    ]
    
    for name, data in result['indicators'].items():
        val = data['value'] if data['value'] is not None else '—'
        threshold = data.get('threshold', '—')
        status = data['status']
        
        # Format value with unit
        if name == '2-10 Spread' and val != '—':
            val = f"{val}bp"
        elif name == 'HY Spread' and val != '—':
            val = f"{val}bp"
        elif name in ['BTC Weekly %', 'DXY Monthly %'] and val != '—':
            val = f"{val}%"
        
        lines.append(f"| {name} | {val} | {threshold} | {status} |")
    
    return '\n'.join(lines)


if __name__ == '__main__':
    result = check_regime()
    
    # Check for --markdown flag
    if len(sys.argv) > 1 and sys.argv[1] == '--markdown':
        print(format_markdown(result))
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
