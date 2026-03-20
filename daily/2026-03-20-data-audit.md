# Data Integrity Audit — 2026-03-20

> Auditor: The Data Auditor | 검증 시각: 09:05 KST

## 가격 데이터 교차검증

| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| FFR Target | 3.50–3.75% | FRED (DFEDTARU 3.75, DFEDTARL 3.50) | Fed 성명서 3/18 | ✅ Verified | FOMC 3/18 동결 확인 |
| 10Y Treasury | 4.26% | FRED DGS10 (3/18) | — | ⚠️ Single-Source | 전일 4.20→4.26% (+6bp) |
| 2Y Treasury | 3.76% | FRED DGS2 (3/18) | — | ⚠️ Single-Source | 전일 3.68→3.76% (+8bp) |
| 2-10 Spread | +0.50% | 계산 (4.26-3.76) | — | ⚠️ Single-Source | 전일 +0.52%→+0.50% |
| VIX | 24.06 | Yahoo ^VIX (3/19 close) | FRED VIXCLS 25.09 (3/18, 1일 지연) | ✅ Verified | Yahoo 당일값 우선. 3/18 FRED=25.09→3/19 Yahoo=24.06 |
| DXY | 99.27 | Yahoo DX-Y.NYB (3/19) | — | ⚠️ Single-Source | FRED Broad DXY 120.55(3/13)는 다른 지수 |
| SPY | $659.80 | Yahoo (3/19 close) | Alpha Vantage $659.80 | ✅ Verified | 차이 0.00% |
| QQQ | $593.02 | Yahoo (3/19 close) | — | ⚠️ Single-Source | |
| BMNR | $21.14 | Yahoo (3/19 close) | Alpha Vantage N/A | ⚠️ Single-Source | AV 미제공 |
| CRCL | $128.33 | Yahoo (3/19 close) | — | ⚠️ Single-Source | 전일 $132.84→$128.33 (-3.39%) |
| COIN | $202.91 | Yahoo (3/19 close) | Alpha Vantage $202.91 | ✅ Verified | 차이 0.00% |
| BTC | $69,864 | CoinGecko | Yahoo BTC-USD $69,849 | ✅ Verified | 차이 0.02% |
| ETH | $2,136.15 | CoinGecko | Yahoo ETH-USD $2,136.04 | ✅ Verified | 차이 0.01% |
| BTC Dominance | 56.3% | CoinGecko Global | — | ⚠️ Single-Source | |
| ETH Dominance | 10.4% | CoinGecko Global | — | ⚠️ Single-Source | |
| Total Crypto MCap | $2.48T | CoinGecko Global | — | ⚠️ Single-Source | |
| MVRV | [데이터 부재] | — | — | ❌ Unverified | Glassnode 유료 |
| Funding Rates | [데이터 부재] | — | — | ❌ Unverified | API 키 필요 |

## 이벤트 확인

| 이벤트 | 상태 | 비고 |
|--------|------|------|
| FOMC 3/18 결정 | ✅ 발표 완료 | 3.50-3.75% 동결. 1명 반대(Miran, 25bp 인하 선호) |
| FOMC SEP/Dot Plot | ✅ 발표 완료 | PDF 확인됨 (상세 미파싱) |
| CPI | 해당 없음 | 다음 발표 대기 |

## 요약
- ✅ Verified: 6건 (FFR, VIX, SPY, COIN, BTC, ETH)
- ⚠️ Single-Source: 9건
- ❌ Unverified: 2건 (MVRV, Funding Rates)
- ⚡ Data Conflict: 0건
