# Data Integrity Audit — 2026-03-22

> Phase 0.5 | The Data Auditor

## 가격 데이터 교차검증

| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| FFR | 3.50-3.75% | FRED DFEDTARU 3.75 | — | ⚠️ | 단일출처, FRED 공식 |
| 10Y | 4.25% | FRED DGS10 (3/19) | — | ⚠️ | 금요일 데이터 미반영 가능 |
| 2Y | 3.79% | FRED DGS2 (3/19) | — | ⚠️ | 금요일 데이터 미반영 가능 |
| VIX | 26.78 | Yahoo ^VIX (3/20) | FRED 24.06 (3/19, 1일 지연) | ✅ | Yahoo 당일 우선 |
| DXY | 120.55 | FRED DTWEXBGS (3/13) | — | ⚠️ | 9일 지연, stale data |
| SPY | $648.57 | Yahoo (3/20) | — | ⚠️ | 단일출처 |
| QQQ | $582.06 | Yahoo (3/20) | — | ⚠️ | 단일출처 |
| BMNR | $20.94 | Yahoo (3/20) | Alpha Vantage $20.94 | ✅ | 일치 |
| CRCL | $126.03 | Yahoo (3/20) | Alpha Vantage N/A | ⚠️ | AV 미응답 |
| COIN | $197.50 | Yahoo (3/20) | Alpha Vantage N/A | ⚠️ | AV 미응답 |
| ERII | $9.46 | Yahoo (3/20) | Alpha Vantage $9.46 | ✅ | 일치 |
| BTC | $68,388 | CoinGecko | Twelve Data $68,444 | ✅ | 차이 0.08% |
| ETH | $2,059 | CoinGecko | Twelve Data $2,125 (3/21 종가) | ⚠️ | CoinGecko 실시간, TD 종가 차이. 주말 변동 |
| TLT | $85.83 | Yahoo (3/20) | — | ⚠️ | 단일출처 |
| GLD | $413.38 | Yahoo (3/20) | — | ⚠️ | 단일출처 |

## RSI 교차검증 (Twelve Data)

| 종목 | RSI(14) 3/20 | 등급 | 비고 |
|------|-------------|------|------|
| SPY | 29.61 | ⚠️ | 과매도 근접 |
| QQQ | 35.21 | ⚠️ | 약세 |
| BMNR | 47.46 | ⚠️ | 중립, 주가 급락 대비 RSI 둔감 |
| CRCL | 71.40 | ⚠️ | 과매수 경계 |
| COIN | 51.97 | ⚠️ | 중립 |
| ERII | 23.97 | ⚠️ | 극단 과매도 🔴 |
| BTC | 44.72 (3/22) | ⚠️ | 약세 진입 |
| ETH | 50.44 (3/21) | ⚠️ | 중립 |

## 크립토 글로벌

| 항목 | 값 | 소스 | 등급 |
|------|---|------|------|
| BTC Dominance | 56.29% | CoinGecko Global | ⚠️ |
| ETH Dominance | 10.32% | CoinGecko Global | ⚠️ |
| Total Crypto MC | $2.45T | CoinGecko Global | ⚠️ |
| 24h Volume | $49.94B | CoinGecko Global | ⚠️ |

## ⚡ 주요 플래그

1. **VIX 26.78 > 25 임계값** → Macro 긴급 Regime 재판정 트리거
2. **BMNR -10.47% 주간** → Price Drop Triage 발동
3. **ERII RSI 23.97** → 극단 과매도, 52주 저점 근접
4. **DXY 데이터 9일 지연** → [DATA SOURCE ALERT] FRED 주간 업데이트 지연
5. **TLT + GLD 동반 하락** → 비정상적 — 주식/채권/금 동시 하락 (유동성 경색 시그널?)
6. **BTC Kill Condition** — 현재 $68,388, Kill $60,000까지 -12.3% 여유

## 감사 의견
- 주말(일요일) 기준으로 주식 데이터는 금요일(3/20) 종가 기준
- 크립토는 실시간 (3/22 09:00 KST)
- ❌ Unverified 데이터 없음 — 모든 데이터 최소 ⚠️ Single-Source 이상
- **FOMC/CPI**: 이번 주 주요 발표 없음 (3/18-19 FOMC 동결 완료)
