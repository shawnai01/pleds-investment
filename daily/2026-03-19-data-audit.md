# PLEDS Data Audit — 2026-03-19 (v2)

> Phase 0.5: Data Integrity Audit
> Auditor: The Data Auditor | Methodology: 2+ source cross-validation

## Macro Data

| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| FFR (Target Range) | 3.50–3.75% | FRED DFEDTARU/L (3/18) | FOMC 성명 (3/18 동결) | ✅ | 금리 동결 확인. 이전 3.72% eff rate → 3.64% (Feb) |
| 10Y Treasury | 4.20% | FRED DGS10 (3/17) | — | ⚠️ | 단일출처. 3/16: 4.23%, 3/13: 4.28% |
| 2Y Treasury | 3.68% | FRED DGS2 (3/17) | — | ⚠️ | 단일출처. 3/16: 3.68%, 3/13: 3.73% |
| 2-10 Spread | +0.52% | 계산: 4.20-3.68 | — | ⚠️ | FRED 소스 기반 계산 |
| VIX | 22.37 | FRED VIXCLS (3/17) | — | ⚠️ | 단일출처. 3/16: 23.51, 3/13: 27.19 (하락 추세) |
| DXY (Broad Index) | 120.55 | FRED DTWEXBGS (3/13) | — | ⚠️ | 단일출처. 주의: 3/13 기준, 지연 있음 |
| Fed Funds Effective | 3.64% | FRED FEDFUNDS (Feb 2026) | — | ⚠️ | 월간 데이터, 최신은 2월 |

## Crypto Data

| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| BTC | $70,980 | CoinGecko API | — | ⚠️ | 24h 변동: -4.14%, MCap $1.42T |
| ETH | $2,189.09 | CoinGecko API | — | ⚠️ | 24h 변동: -6.09%, MCap $264.4B |
| BTC Dominance | 56.41% | CoinGecko Global | — | ⚠️ | 단일출처 |
| Total Crypto MCap | $2.52T | CoinGecko Global | — | ⚠️ | 24h 변동: -3.68% |
| MVRV | [데이터 부재] | — | — | ❌ | Glassnode 유료 API 필요 |
| Funding Rates | [데이터 부재] | — | — | ❌ | API 접근 불가 |

## Equity Data

| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| SPY | $661.43 | Yahoo Finance API (3/18 close) | — | ⚠️ | 전일 $670.79 → -1.39% |
| QQQ | $594.90 | Yahoo Finance API (3/18 close) | — | ⚠️ | 전일 $603.31 → -1.39% |
| BMNR | $21.41 | Yahoo Finance (3/18 close) | — | ⚠️ | -7.83%, AH $21.75, MCap $9.74B, EPS -$0.93 |
| CRCL | $123.47 | Yahoo Finance (장중 3/19) | — | ⚠️ | +7.01% (장중), MCap $32.78B |
| COIN | $201.89 | Yahoo Finance (장중 3/19) | — | ⚠️ | +4.47% (장중), MCap $54.44B, P/E 45.47 |

## FOMC Event Verification

| 항목 | 상태 | 비고 |
|------|------|------|
| 3/18 FOMC 금리결정 | ✅ 동결 확인 | FFR 3.50-3.75% 유지. FRED 데이터에서 3/18도 동일 값 |

## Data Quality Summary

- ✅ Verified: 1 (FFR 금리 동결)
- ⚠️ Single-Source: 14 (대부분 — Alpha Vantage/Twelve Data 키 없어 교차검증 제한)
- ❌ Unverified: 2 (MVRV, Funding Rates)

**핵심 제약:** 주식/ETF 교차검증용 2차 소스(Alpha Vantage, Twelve Data) API 키 미확보. 대부분 Single-Source.

**투자 판정 주의:** ❌ MVRV, Funding Rates는 참고 불가. ⚠️ 데이터는 [단일출처] 표기 하에 사용 가능.
