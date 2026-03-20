#!/bin/bash
# PLEDS Technical Indicator Collector
# Usage: ./collect-indicators.sh [outputsize]
# Default: 30 days. First run: use 60 for backfill.
#
# Rate limit: Twelve Data free = 8 req/min, 800/day
# Strategy: collect OHLCV + 4 key indicators per ticker = 5 calls/ticker
# 14 tickers × 5 = 70 calls total, ~9 min with rate limiting

set -euo pipefail

API_KEY="${TWELVEDATA_API_KEY:-9f49c8d317be414dbf8ffa926108037a}"
OUTSIZE="${1:-30}"
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
OHLCV_DIR="$BASE_DIR/ohlcv"
IND_DIR="$BASE_DIR/indicators"
TIMESTAMP=$(date -u +%Y%m%dT%H%M%SZ)

# Watchlist: Top 10 + portfolio + key watchlist
TICKERS=(NVDA ERII LEU TWST CRCL WST ISRG TER TXN COIN BMNR CCJ)

mkdir -p "$OHLCV_DIR" "$IND_DIR"

fetch() {
  local url="$1" out="$2"
  local resp
  resp=$(curl -sf "$url" 2>/dev/null) || { echo "FAIL: $url"; return 1; }
  # Check for error
  if echo "$resp" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if 'values' in d else 1)" 2>/dev/null; then
    echo "$resp" > "$out"
    echo "OK: $out"
  else
    echo "ERR: $(echo "$resp" | python3 -c "import sys,json; print(json.load(sys.stdin).get('message','unknown'))" 2>/dev/null)"
    return 1
  fi
}

for ticker in "${TICKERS[@]}"; do
  echo "=== $ticker ==="

  # 1. OHLCV
  fetch "https://api.twelvedata.com/time_series?symbol=${ticker}&interval=1day&outputsize=${OUTSIZE}&apikey=${API_KEY}" \
        "$OHLCV_DIR/${ticker}.json"
  sleep 8  # rate limit

  # 2. RSI
  fetch "https://api.twelvedata.com/rsi?symbol=${ticker}&interval=1day&time_period=14&outputsize=${OUTSIZE}&apikey=${API_KEY}" \
        "$IND_DIR/${ticker}_rsi.json"
  sleep 8

  # 3. MACD
  fetch "https://api.twelvedata.com/macd?symbol=${ticker}&interval=1day&outputsize=${OUTSIZE}&apikey=${API_KEY}" \
        "$IND_DIR/${ticker}_macd.json"
  sleep 8

  # 4. Bollinger Bands
  fetch "https://api.twelvedata.com/bbands?symbol=${ticker}&interval=1day&outputsize=${OUTSIZE}&apikey=${API_KEY}" \
        "$IND_DIR/${ticker}_bbands.json"
  sleep 8

  # 5. ADX
  fetch "https://api.twelvedata.com/adx?symbol=${ticker}&interval=1day&time_period=14&outputsize=${OUTSIZE}&apikey=${API_KEY}" \
        "$IND_DIR/${ticker}_adx.json"
  sleep 8

  echo ""
done

echo "=== Collection complete: $TIMESTAMP ==="
echo "OHLCV: $OHLCV_DIR/"
echo "Indicators: $IND_DIR/"
