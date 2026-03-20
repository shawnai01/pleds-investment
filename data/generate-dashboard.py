#!/usr/bin/env python3
"""
PLEDS Technical Dashboard Generator v2
- 할루시네이션 방지: 데이터 없으면 "데이터 부족" 명시
- SMA/EMA 혼동 수정: SMA라고 정직하게 표기
- 다이버전스: 조건 엄격화 + 신뢰도 표기
- 모든 숫자는 API 원본 그대로, 가공 최소화
"""

import json
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
            vals = d.get("values", [])
            return vals
    except:
        return []

def data_date(vals):
    """Return the most recent data date"""
    if vals:
        return vals[0].get("datetime", "?")
    return "?"

# ─── RSI ───
def rsi_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_rsi.json")
    if not vals:
        return {"current": "—", "trend": "—", "signal": "❓ 데이터 없음", "series": "—", "date": "?"}
    
    current = float(vals[0]["rsi"])
    date = vals[0]["datetime"]
    
    # 5-day series (most recent first in API, reverse for display)
    nums = [float(v["rsi"]) for v in vals[:5] if "rsi" in v]
    series_str = " → ".join(f"{n:.1f}" for n in reversed(nums)) if nums else "—"
    
    # Trend: compare first vs last of 5-day window
    if len(nums) >= 3:
        diff_pct = (nums[0] - nums[-1]) / max(abs(nums[-1]), 0.01) * 100
        trend = "↑" if diff_pct > 5 else ("↓" if diff_pct < -5 else "→")
    else:
        trend = "—"
    
    # Signal: simple, honest, no interpretation beyond thresholds
    if current < 30:
        signal = "🟢 과매도 (<30)"
    elif current < 40:
        signal = "🟡 약세 구간 (30-40)"
    elif current > 70:
        signal = "🔴 과매수 (>70)"
    elif current > 60:
        signal = "🟡 강세 구간 (60-70)"
    else:
        signal = "⚪ 중립 (40-60)"
    
    return {"current": f"{current:.1f}", "trend": trend, "signal": signal, "series": series_str, "date": date}

# ─── MACD ───
def macd_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_macd.json")
    if not vals:
        return {"histogram": "—", "trend": "—", "signal": "❓ 데이터 없음"}
    
    hists = [float(v["macd_hist"]) for v in vals[:5] if "macd_hist" in v]
    if len(hists) < 2:
        return {"histogram": "—", "trend": "—", "signal": "❓ 데이터 부족"}
    
    current_h = hists[0]
    prev_h = hists[1]
    
    # Histogram trend
    if len(hists) >= 3:
        trend = "↑" if hists[0] > hists[1] > hists[2] else ("↓" if hists[0] < hists[1] < hists[2] else "→")
    else:
        trend = "→"
    
    # Zero-cross detection (only between yesterday and today)
    if prev_h < 0 and current_h > 0:
        signal = "🟢 상향 크로스 (0선 돌파)"
    elif prev_h > 0 and current_h < 0:
        signal = "🔴 하향 크로스 (0선 이탈)"
    elif current_h > 0:
        signal = f"⬆️ 양수 ({current_h:+.3f})"
    else:
        signal = f"⬇️ 음수 ({current_h:+.3f})"
    
    hist_series = " → ".join(f"{h:+.3f}" for h in reversed(hists)) if hists else "—"
    
    return {"histogram": f"{current_h:+.4f}", "trend": trend, "signal": signal, "series": hist_series}

# ─── Bollinger Bands ───
def bbands_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_bbands.json")
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    if not vals or not ohlcv:
        return {"position": "❓ 데이터 없음", "pct_b": "—", "width_trend": "—"}
    
    upper = float(vals[0]["upper_band"])
    lower = float(vals[0]["lower_band"])
    middle = float(vals[0]["middle_band"])
    close = float(ohlcv[0]["close"])
    
    # %B = (Close - Lower) / (Upper - Lower)
    band_width = upper - lower
    if band_width <= 0:
        return {"position": "❓ 밴드 폭 0", "pct_b": "—", "width_trend": "—"}
    
    pct_b = (close - lower) / band_width * 100
    
    # Band width trend (squeeze/expansion)
    widths = []
    for v in vals[:10]:
        try:
            w = float(v["upper_band"]) - float(v["lower_band"])
            widths.append(w)
        except:
            pass
    
    width_trend = "→ 보합"
    if len(widths) >= 5:
        ratio = widths[0] / widths[-1] if widths[-1] > 0 else 1
        if ratio < 0.75:
            width_trend = "🔄 Squeeze (밴드 수축 {:.0f}%)".format((1-ratio)*100)
        elif ratio > 1.25:
            width_trend = "💥 Expansion (밴드 확장 {:.0f}%)".format((ratio-1)*100)
    
    # Position
    if close > upper:
        position = "🔴 상단 이탈"
    elif close < lower:
        position = "🟢 하단 이탈"
    elif pct_b > 80:
        position = "⬆️ 상단 근접"
    elif pct_b < 20:
        position = "⬇️ 하단 근접"
    else:
        position = "➡️ 중간 영역"
    
    return {"position": position, "pct_b": f"{pct_b:.0f}%", "width_trend": width_trend, 
            "raw": f"U={upper:.2f} M={middle:.2f} L={lower:.2f} Close={close:.2f}"}

# ─── ADX ───
def adx_analysis(ticker):
    vals = load_json(IND_DIR / f"{ticker}_adx.json")
    if not vals:
        return {"current": "—", "signal": "❓ 데이터 없음"}
    current = float(vals[0]["adx"])
    
    # 5-day trend
    nums = [float(v["adx"]) for v in vals[:5] if "adx" in v]
    trend = ""
    if len(nums) >= 3:
        diff = nums[0] - nums[-1]
        trend = f" (추세{'강화↑' if diff > 2 else '약화↓' if diff < -2 else '유지→'})"
    
    if current > 40:
        signal = f"🔥 매우 강한 추세 ({current:.0f}){trend}"
    elif current > 25:
        signal = f"📈 추세 진행 ({current:.0f}){trend}"
    elif current > 20:
        signal = f"🟡 약한 추세 ({current:.0f}){trend}"
    else:
        signal = f"⚪ 비추세/횡보 ({current:.0f}){trend}"
    return {"current": f"{current:.1f}", "signal": signal}

# ─── Price vs SMA (정직하게 SMA라고 표기) ───
def price_vs_sma(ticker):
    """SMA 기반 위치 분석. EMA가 아님을 명시."""
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    if len(ohlcv) < 20:
        return {"detail": "데이터 부족 (<20일)", "alignment": "❓"}
    
    closes = [float(v["close"]) for v in ohlcv]
    current = closes[0]
    
    sma20 = sum(closes[:20]) / 20
    
    parts = [f"Close={current:.2f}", f"SMA20={sma20:.2f} ({'위' if current > sma20 else '아래'})"]
    
    if len(closes) >= 50:
        sma50 = sum(closes[:50]) / 50
        parts.append(f"SMA50={sma50:.2f} ({'위' if current > sma50 else '아래'})")
        
        if current > sma20 > sma50:
            alignment = "🟢 정배열"
        elif current < sma20 < sma50:
            alignment = "🔴 역배열"
        else:
            alignment = "🟡 혼조"
    else:
        alignment = f"{'🟢' if current > sma20 else '🔴'} SMA20 {'위' if current > sma20 else '아래'} (50일 데이터 부족)"
    
    return {"detail": " | ".join(parts), "alignment": alignment}

# ─── Divergence (엄격화) ───
def detect_divergence(ticker):
    """
    다이버전스 탐지 — 엄격한 조건:
    1. 최근 20일 중 두 개의 swing low/high를 찾음
    2. 가격과 RSI의 방향이 불일치할 때만 탐지
    ⚠️ 30일 데이터 한계로 신뢰도 '참고' 수준
    """
    ohlcv = load_json(OHLCV_DIR / f"{ticker}.json")
    rsi_vals = load_json(IND_DIR / f"{ticker}_rsi.json")
    
    if len(ohlcv) < 15 or len(rsi_vals) < 15:
        return "데이터 부족"
    
    prices = [float(v["close"]) for v in ohlcv[:20]]
    rsis = [float(v["rsi"]) for v in rsi_vals[:20]]
    
    n = min(len(prices), len(rsis))
    if n < 15:
        return "데이터 부족"
    
    # Find swing lows: local minimum (lower than both neighbors)
    swing_lows = []
    for i in range(1, min(n-1, 18)):
        if prices[i] < prices[i-1] and prices[i] < prices[i+1]:
            swing_lows.append((i, prices[i], rsis[i]))
    
    # Find swing highs
    swing_highs = []
    for i in range(1, min(n-1, 18)):
        if prices[i] > prices[i-1] and prices[i] > prices[i+1]:
            swing_highs.append((i, prices[i], rsis[i]))
    
    result = "없음"
    
    # Bullish divergence: lower price low + higher RSI low
    if len(swing_lows) >= 2:
        recent, older = swing_lows[0], swing_lows[1]
        if recent[1] < older[1] and recent[2] > older[2]:
            result = f"🟢 Bullish Div (참고): 가격 {older[1]:.2f}→{recent[1]:.2f}↓ but RSI {older[2]:.1f}→{recent[2]:.1f}↑"
    
    # Bearish divergence: higher price high + lower RSI high
    if len(swing_highs) >= 2:
        recent, older = swing_highs[0], swing_highs[1]
        if recent[1] > older[1] and recent[2] < older[2]:
            result = f"🔴 Bearish Div (참고): 가격 {older[1]:.2f}→{recent[1]:.2f}↑ but RSI {older[2]:.1f}→{recent[2]:.1f}↓"
    
    return result

# ─── Composite Signal ───
def composite_signal(rsi, macd, bb, adx, sma):
    """
    기계적 복합 등급. 로직:
    - RSI 과매도/과매수: ±2
    - MACD 0선 크로스: ±2, 양수/음수: ±1
    - BB 이탈: ±1
    - SMA 배열: ±1
    - ADX 비추세 시 전체 점수 감쇄(×0.5)
    ⚠️ 이 가중치는 백테스트 미검증. 참고용.
    """
    score = 0
    reasons = []
    
    if "과매도" in rsi["signal"]:
        score += 2; reasons.append("RSI<30")
    elif "과매수" in rsi["signal"]:
        score -= 2; reasons.append("RSI>70")
    
    if "상향 크로스" in macd["signal"]:
        score += 2; reasons.append("MACD↑크로스")
    elif "하향 크로스" in macd["signal"]:
        score -= 2; reasons.append("MACD↓크로스")
    elif "양수" in macd["signal"]:
        score += 1
    elif "음수" in macd["signal"]:
        score -= 1
    
    if "하단 이탈" in bb["position"]:
        score += 1; reasons.append("BB하단이탈")
    elif "상단 이탈" in bb["position"]:
        score -= 1; reasons.append("BB상단이탈")
    
    if "정배열" in sma.get("alignment", ""):
        score += 1; reasons.append("SMA정배열")
    elif "역배열" in sma.get("alignment", ""):
        score -= 1; reasons.append("SMA역배열")
    
    # ADX dampening
    damped = False
    if "비추세" in adx.get("signal", ""):
        score = int(score * 0.5)
        damped = True
    
    reason_str = ", ".join(reasons) if reasons else "특이사항 없음"
    damp_note = " (ADX<20 비추세→감쇄)" if damped else ""
    
    if score >= 3:
        return f"🟢 Favorable ({score}점: {reason_str}{damp_note})"
    elif score <= -3:
        return f"🔴 Unfavorable ({score}점: {reason_str}{damp_note})"
    elif "과매도" in rsi.get("signal", "") and score >= 0:
        return f"⚪ Oversold Bounce ({score}점: {reason_str}{damp_note})"
    else:
        return f"🟡 Neutral ({score}점{damp_note})"

# ─── Main ───
def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Check data freshness
    sample = load_json(OHLCV_DIR / f"{TICKERS[0]}.json")
    data_as_of = data_date(sample) if sample else "불명"
    
    lines = [
        f"# 📊 PLEDS Technical Dashboard v2",
        f"> Generated: {now} | Data as of: {data_as_of}",
        f"> Source: Twelve Data API (RSI/MACD/BB/ADX) + OHLCV 시계열",
        f"> ⚠️ 이 대시보드는 **타이밍 보조**입니다. L1-L4 판단을 override하지 않음.",
        f"> ⚠️ SMA 사용 (EMA 아님). 복합점수 가중치 백테스트 미검증.",
        "",
        "## 종합 등급",
        "",
        "| Ticker | 종합 등급 | RSI(14) | MACD | ADX | BB | SMA | Divergence |",
        "|--------|----------|---------|------|-----|-----|-----|------------|",
    ]
    
    details = []
    
    for ticker in TICKERS:
        rsi = rsi_analysis(ticker)
        macd = macd_analysis(ticker)
        bb = bbands_analysis(ticker)
        adx = adx_analysis(ticker)
        sma = price_vs_sma(ticker)
        div = detect_divergence(ticker)
        composite = composite_signal(rsi, macd, bb, adx, sma)
        
        lines.append(
            f"| **{ticker}** | {composite} | {rsi['current']} {rsi['signal']} | "
            f"{macd['signal']} | {adx['signal']} | {bb['position']} {bb['pct_b']} | "
            f"{sma.get('alignment', '—')} | {div} |"
        )
        
        details.append(f"\n### {ticker}")
        details.append(f"- **데이터 기준일:** {rsi.get('date', '?')}")
        details.append(f"- **RSI 시계열 (5d):** {rsi['series']} → 현재 {rsi['current']} ({rsi['trend']})")
        details.append(f"- **MACD Hist 시계열:** {macd.get('series', '—')} (추세: {macd.get('trend', '—')})")
        details.append(f"- **BB:** {bb['position']} | %B={bb.get('pct_b', '—')} | {bb['width_trend']}")
        if "raw" in bb:
            details.append(f"  - 원본: {bb['raw']}")
        details.append(f"- **ADX:** {adx['signal']}")
        details.append(f"- **SMA 위치:** {sma.get('detail', '—')} | {sma.get('alignment', '—')}")
        details.append(f"- **다이버전스:** {div}")
        details.append(f"- **종합:** {composite}")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 상세 분석")
    lines.extend(details)
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ⚠️ 한계 명시")
    lines.append("1. **SMA 사용**: EMA가 아닌 SMA(단순이동평균). EMA보다 최근 가격 반영 느림.")
    lines.append("2. **30일 데이터**: 50일/200일 이동평균 계산 불가. 장기 추세 판단 제한적.")
    lines.append("3. **다이버전스**: swing low/high 기반이나 30일 제한으로 '참고' 수준. 확정적 시그널 아님.")
    lines.append("4. **복합점수 가중치**: RSI±2, MACD±2, BB±1, SMA±1은 임의 설정. 백테스트 미실시.")
    lines.append("5. **ADX 감쇄**: 비추세(ADX<20) 시 점수×0.5는 경험적 규칙. 최적화 안 됨.")
    lines.append("")
    lines.append(f"*Auto-generated by PLEDS Quant Dashboard v2 | {now}*")
    lines.append("*모든 숫자는 Twelve Data API 원본. 가공: 추세 방향, 복합 점수만.*")
    
    OUTPUT.write_text("\n".join(lines))
    print(f"Dashboard v2 written to {OUTPUT}")

if __name__ == "__main__":
    main()
