#!/usr/bin/env python3
"""
PLEDS Watchlist Alert System — 가격 체크 + 만료 체크

Usage:
  python3 scripts/watchlist-check.py [--markdown]

Output: JSON alerts or markdown format
"""

import os
import sys
import json
import requests
from datetime import datetime, date, timedelta
from pathlib import Path

# Get the project root directory
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
WATCHLIST_PATH = PROJECT_DIR / 'data' / 'watchlist.json'


def load_watchlist():
    """Load watchlist from JSON file"""
    with open(WATCHLIST_PATH, 'r') as f:
        return json.load(f)


def save_watchlist(data):
    """Save watchlist to JSON file"""
    data['last_updated'] = datetime.now().isoformat()
    with open(WATCHLIST_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_price(ticker):
    """Get current price from Yahoo Finance v8 API"""
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        data = r.json()
        return round(data['chart']['result'][0]['meta']['regularMarketPrice'], 2)
    except Exception as e:
        print(f"[WARN] Price fetch failed for {ticker}: {e}", file=sys.stderr)
        return None


def check_watchlist():
    """Check all watchlist items for alerts"""
    data = load_watchlist()
    alerts = []
    today = date.today()
    
    for item in data['watchlist']:
        if item['status'] != 'active':
            continue
        
        ticker = item['ticker']
        current = get_price(ticker)
        
        if current is None:
            continue
        
        # Target price check
        target = item['target_price']
        target_type = item['target_type']
        
        if target_type == 'below' and current <= target:
            alerts.append({
                'type': 'TARGET_HIT',
                'ticker': ticker,
                'current_price': current,
                'target_price': target,
                'thesis': item['thesis_summary'],
                'conviction': item['conviction']
            })
        elif target_type == 'above' and current >= target:
            alerts.append({
                'type': 'TARGET_HIT',
                'ticker': ticker,
                'current_price': current,
                'target_price': target,
                'thesis': item['thesis_summary'],
                'conviction': item['conviction']
            })
        
        # Kill price check
        kill_price = item.get('kill_price')
        if kill_price is not None:
            if current >= kill_price:
                alerts.append({
                    'type': 'KILL_HIT',
                    'ticker': ticker,
                    'current_price': current,
                    'kill_price': kill_price,
                    'reason': item['kill_reason']
                })
                item['status'] = 'killed'
        
        # Expiry check
        expiry = datetime.strptime(item['expiry_date'], '%Y-%m-%d').date()
        days_until_expiry = (expiry - today).days
        
        if days_until_expiry <= 0:
            alerts.append({
                'type': 'EXPIRED',
                'ticker': ticker,
                'added_date': item['added_date'],
                'expiry_date': item['expiry_date']
            })
            item['status'] = 'expired'
        elif days_until_expiry <= 7:
            alerts.append({
                'type': 'EXPIRING_SOON',
                'ticker': ticker,
                'days_left': days_until_expiry,
                'expiry_date': item['expiry_date']
            })
    
    # Save any status changes
    save_watchlist(data)
    
    return {
        'timestamp': datetime.now().isoformat(),
        'alerts': alerts,
        'watchlist_count': len([i for i in data['watchlist'] if i['status'] == 'active'])
    }


def format_markdown(result):
    """Format result as markdown for daily briefing"""
    alerts = result['alerts']
    
    # Group by type
    target_hits = [a for a in alerts if a['type'] == 'TARGET_HIT']
    kill_hits = [a for a in alerts if a['type'] == 'KILL_HIT']
    expiring = [a for a in alerts if a['type'] == 'EXPIRING_SOON']
    expired = [a for a in alerts if a['type'] == 'EXPIRED']
    
    lines = [
        "## 📋 Watchlist Alerts",
        f"**Active:** {result['watchlist_count']} 종목",
        ""
    ]
    
    # Target hits
    if target_hits:
        lines.append("🎯 **TARGET HIT — 진입 검토:**")
        for a in target_hits:
            stars = '⭐' * a['conviction']
            lines.append(f"- **{a['ticker']}**: 현재 ${a['current_price']} (목표 ${a['target_price']}) {stars}")
            lines.append(f"  - \"{a['thesis']}\"")
        lines.append("")
    else:
        lines.append("🎯 **TARGET HIT:** (없음)")
        lines.append("")
    
    # Kill hits
    if kill_hits:
        lines.append("☠️ **KILL HIT — 워치리스트 제거:**")
        for a in kill_hits:
            lines.append(f"- **{a['ticker']}**: ${a['current_price']} (Kill ${a['kill_price']})")
            lines.append(f"  - 사유: {a['reason']}")
        lines.append("")
    else:
        lines.append("☠️ **KILL HIT:** (없음)")
        lines.append("")
    
    # Expiring soon
    if expiring:
        lines.append("⏰ **EXPIRING SOON (7일 이내):**")
        for a in expiring:
            lines.append(f"- {a['ticker']}: {a['days_left']}일 남음 (만료: {a['expiry_date']}) — 재평가 필요")
        lines.append("")
    
    # Expired
    if expired:
        lines.append("⏳ **EXPIRED — 재평가 또는 폐기:**")
        for a in expired:
            lines.append(f"- {a['ticker']}: 만료됨 (등록: {a['added_date']})")
        lines.append("")
    
    return '\n'.join(lines)


if __name__ == '__main__':
    result = check_watchlist()
    
    # Check for --markdown flag
    if len(sys.argv) > 1 and sys.argv[1] == '--markdown':
        print(format_markdown(result))
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
