#!/usr/bin/env python3
"""
PLEDS Technical Dashboard Generator
Reads local indicator JSON files and generates a markdown dashboard
with time-series analysis (not just snapshots).
"""

import json, os, sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent
OHLCV_DIR = BASE / "ohlcv"
IND_DIR = BASE / "indicators"
OUTPUT = BASE / "TECHNICAL-DASHBOARD.md"

TICKERS = ["NVDA","ERII","LEU","TWST","CRCL","WST","ISRG","TER","TXN","COIN","BMNR","CCJ"]

def load_json(path):
    try:
        with open(path) as f:
            d = json.load(f)
            return d.get("values", [])
    except:
        return []

def trend_direction(values, key, n=5):
    """Analyze trend of last n values: ↑ rising, ↓ falling, → flat"""
    if len(values) < n:
        return "—", []
    nums = []
    for v in values[:n]:
        try:
            nums.append(float(v[key]))
        except:
            pass
    if len(nums) < 3:
        return "—", nums
    # values[0] is most recent
    diff = nums[0] - nums[-1]
    avg = sum(nums) / len(nums)
    pct = (diff / avg * 100) if avg != 0 else 0
    if pct > 3:
        return "↑", nums
    elif pct < -3:
        return "↓", nums
    else:
        return "→", nums

def rsi_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_rsi.json")
    if not vals:
        return {"current": "—", "trend": "—", "signal": "⚪", "series": "—"}
    current = float(vals[0]["rsi"])
    trend, nums = trend_direction(vals, "rsi", 5)
    
    if current < 30:
        signal = "🟢 과매도" if trend == "↓" or trend == "→" else "🟡 과매도→반등중"
    elif current > 70:
        signal = "🔴 과매수" if trend == "↑" or trend == "→" else "🟡 과매수→하락중"
    else:
        signal = "⚪ 중립"
    
    series_str = " → ".join(f"{n:.1f}" for n in reversed(nums)) if nums else "—"
    return {"current": f"{current:.1f}", "trend": trend, "signal": signal, "series": series_str}

def macd_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_macd.json")
    if not vals:
        return {"histogram": "—", "trend": "—", "signal": "⚪", "divergence": "—"}
    
    hists = []
    for v in vals[:10]:
        try:
            hists.append(float(v["macd_hist"]))
        except:
            pass
    
    if len(hists) < 3:
        return {"histogram": "—", "trend": "—", "signal": "⚪", "divergence": "—"}
    
    current_h = hists[0]
    trend = "↑" if hists[0] > hists[1] > hists[2] else ("↓" if hists[0] < hists[1] < hists[2] else "→")
    
    # Crossover detection
    if hists[1] < 0 and hists[0] > 0:
        signal = "🟢 골든크로스"
    elif hists[1] > 0 and hists[0] < 0:
        signal = "🔴 데드크로스"
    elif current_h > 0:
        signal = "⬆️ 양수"
    else:
        signal = "⬇️ 음수"
    
    return {"histogram": f"{current_h:.4f}", "trend": trend, "signal": signal}

def bbands_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_bbands.json")
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    if not vals or not ohlcv:
        return {"position": "—", "width_trend": "—", "signal": "⚪"}
    
    upper = float(vals[0]["upper_band"])
    lower = float(vals[0]["lower_band"])
    middle = float(vals[0]["middle_band"])
    close = float(ohlcv[0]["close"])
    
    # Band width trend (squeeze detection)
    widths = []
    for v in vals[:10]:
        try:
            w = float(v["upper_band"]) - float(v["lower_band"])
            widths.append(w)
        except:
            pass
    
    width_trend = "→"
    if len(widths) >= 5:
        if widths[0] < widths[-1] * 0.8:
            width_trend = "🔄 Squeeze (밴드 수축)"
        elif widths[0] > widths[-1] * 1.2:
            width_trend = "💥 Expansion (밴드 확장)"
    
    # Position
    if close > upper:
        position = "🔴 상단 이탈"
    elif close < lower:
        position = "🟢 하단 이탈"
    elif close > middle:
        position = "⬆️ 중간선 위"
    else:
        position = "⬇️ 중간선 아래"
    
    pct_b = (close - lower) / (upper - lower) * 100 if (upper - lower) > 0 else 50
    
    return {"position": position, "pct_b": f"{pct_b:.0f}%", "width_trend": width_trend}

def adx_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_adx.json")
    if not vals:
        return {"current": "—", "signal": "⚪"}
    current = float(vals[0]["adx"])
    if current > 40:
        signal = "🔥 매우 강한 추세"
    elif current > 25:
        signal = "📈 추세 진행 중"
    elif current > 20:
        signal = "🟡 약한 추세"
    else:
        signal = "⚪ 비추세 (횡보)"
    return {"current": f"{current:.1f}", "signal": signal}

def price_vs_ema(ticker):
    """Check price position relative to key EMAs from OHLCV data"""
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    if len(ohlcv) < 20:
        return {"ema_status": "—"}
    
    closes = [float(v["close"]) for v in ohlcv]
    current = closes[0]
    
    ema20 = sum(closes[:20]) / 20 if len(closes) >= 20 else None
    ema50 = sum(closes[:50]) / 50 if len(closes) >= 50 else None
    
    parts = []
    if ema20:
        rel = "위" if current > ema20 else "아래"
        parts.append(f"EMA20({ema20:.2f}) {rel}")
    if ema50:
        rel = "위" if current > ema50 else "아래"
        parts.append(f"EMA50({ema50:.2f}) {rel}")
    
    # Trend: 20 > 50 = bullish alignment
    if ema20 and ema50:
        if current > ema20 > ema50:
            alignment = "🟢 정배열 (Bullish)"
        elif current < ema20 < ema50:
            alignment = "🔴 역배열 (Bearish)"
        else:
            alignment = "🟡 혼조"
    else:
        alignment = "—"
    
    return {"ema_detail": " | ".join(parts), "alignment": alignment}

def detect_divergence(ticker):
    """Price makes new low but RSI doesn't = bullish divergence"""
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    rsi_vals = load_json(IND_DIR / f"{ticker}_rsi.json")
    if len(ohlcv) < 10 or len(rsi_vals) < 10:
        return "데이터 부족"
    
    prices = [float(v["close"]) for v in ohlcv[:10]]
    rsis = [float(v["rsi"]) for v in rsi_vals[:10]]
    
    # Check last 10 days: price lower but RSI higher = bullish divergence
    if prices[0] < min(prices[3:7]) and rsis[0] > min(rsis[3:7]):
        return "🟢 Bullish Divergence (가격↓ RSI↑)"
    elif prices[0] > max(prices[3:7]) and rsis[0] < max(rsis[3:7]):
        return "🔴 Bearish Divergence (가격↑ RSI↓)"
    else:
        return "없음"

def composite_signal(rsi, macd, bb, adx, ema):
    """Generate composite technical rating"""
    score = 0
    
    # RSI
    if "과매도" in rsi["signal"]:
        score += 2
    elif "과매수" in rsi["signal"]:
        score -= 2
    
    # MACD
    if "골든크로스" in macd["signal"]:
        score += 2
    elif "데드크로스" in macd["signal"]:
        score -= 2
    elif "양수" in macd["signal"]:
        score += 1
    else:
        score -= 1
    
    # BB
    if "하단 이탈" in bb["position"]:
        score += 1
    elif "상단 이탈" in bb["position"]:
        score -= 1
    
    # ADX
    if "비추세" in adx["signal"]:
        score = int(score * 0.5)  # dampen signal in non-trending market
    
    # EMA alignment
    if "정배열" in ema.get("alignment", ""):
        score += 1
    elif "역배열" in ema.get("alignment", ""):
        score -= 1
    
    if score >= 3:
        return "🟢 Tech Favorable"
    elif score <= -3:
        return "🔴 Tech Unfavorable"
    elif score >= 1 and "과매도" in rsi["signal"]:
        return "⚪ Oversold Bounce"
    else:
        return "🟡 Tech Neutral"

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# 📊 PLEDS Technical Dashboard",
        f"> Generated: {now} | Source: Twelve Data API + Local Time Series",
        f"> ⚠️ L5는 L1-L4를 override하지 않음 — 타이밍 보조 역할만",
        "",
        "## 종합 등급",
        "",
        "| Ticker | 종합 등급 | RSI(14) | RSI 추세 | MACD | ADX | BB 위치 | EMA 배열 | 다이버전스 |",
        "|--------|----------|---------|---------|------|-----|--------|---------|-----------|",
    ]
    
    details = []
    
    for ticker in TICKERS:
        rsi = rsi_analysis(ticker)
        macd = macd_analysis(ticker)
        bb = bbands_analysis(ticker)
        adx = adx_analysis(ticker)
        ema = price_vs_ema(ticker)
        div = detect_divergence(ticker)
        composite = composite_signal(rsi, macd, bb, adx, ema)
        
        lines.append(
            f"| **{ticker}** | {composite} | {rsi['current']} | {rsi['trend']} {rsi['signal']} | "
            f"{macd['signal']} | {adx['current']} {adx['signal']} | {bb['position']} | "
            f"{ema.get('alignment', '—')} | {div} |"
        )
        
        # Detail section
        details.append(f"\n### {ticker}")
        details.append(f"- **RSI 시계열 (5d):** {rsi['series']}")
        details.append(f"- **MACD Histogram:** {macd['histogram']} (추세: {macd.get('trend', '—')})")
        details.append(f"- **BB:** {bb['position']} | %B={bb.get('pct_b', '—')} | {bb['width_trend']}")
        details.append(f"- **ADX:** {adx['current']} — {adx['signal']}")
        details.append(f"- **EMA:** {ema.get('ema_detail', '—')} | {ema.get('alignment', '—')}")
        details.append(f"- **다이버전스:** {div}")
        details.append(f"- **종합:** {composite}")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 상세 분석")
    lines.extend(details)
    
    lines.append("")
    lines.append("---")
    lines.append(f"*Auto-generated by PLEDS Quant Dashboard | {now}*")
    lines.append("*이 대시보드는 매수/매도 의견이 아닌 정량 팩트입니다. L1-L4와 결합하여 판단하세요.*")
    
    OUTPUT.write_text("\n".join(lines))
    print(f"Dashboard written to {OUTPUT}")

if __name__ == "__main__":
    main()
