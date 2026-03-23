# Phase 0.5: Data Integrity Audit — 2026-03-23

> 기준일: 2026-03-20 (금) 미국 장 종가 + 2026-03-23 09:00 KST 크립토

## 가격 데이터 교차검증

| 항목 | 값 | 소스1 | 소스2 | 소스3 | 등급 | 비고 |
|------|---|-------|-------|-------|------|------|
| SPY | $648.57 | Yahoo | AlphaVantage | TwelveData | ✅ | 3소스 일치 |
| QQQ | $582.06 | Yahoo | — | TwelveData | ✅ | 2소스 일치 |
| VIX | 26.78 | Yahoo | FRED 24.06(3/19,1일지연) | — | ✅ | Yahoo 당일값 우선 |
| BTC | $67,885 | CoinGecko | TwelveData $67,923 | — | ✅ | 차이 0.06% |
| ETH | $2,053 | CoinGecko $2,053.38 | TwelveData $2,053.65 | — | ✅ | 차이 0.01% |
| BMNR | $20.94 | Yahoo | AlphaVantage [N/A] | — | ⚠️ | AV 미지원, Yahoo 단일소스 |
| CRCL | $126.03 | Yahoo | — | — | ⚠️ | 단일소스 (신규 IPO) |
| COIN | $197.50 | Yahoo | — | — | ⚠️ | 단일소스 |
| ERII | $9.46 | Yahoo | — | — | ⚠️ | 단일소스 |
| FFR | 3.50-3.75% | FRED DFEDTARU 3.75 | — | — | ✅ | FOMC 공식 |
| 10Y | 4.25% | FRED DGS10 (3/19) | — | — | ⚠️ | 단일소스, 1영업일 지연 |
| 2Y | 3.79% | FRED DGS2 (3/19) | — | — | ⚠️ | 단일소스, 1영업일 지연 |
| 2-10 Spread | +46bp | FRED 산출 (4.25-3.79) | — | — | ✅ | 정상 양수 |
| DXY | 120.55 | FRED DTWEXBGS (3/13) | — | — | ⚠️ | 1주+ 지연, 참고용 |
| BTC Dominance | 56.15% | CoinGecko | — | — | ⚠️ | 단일소스 |

## 데이터 소스 건강 상태

| 소스 | 상태 | 비고 |
|------|------|------|
| Yahoo Finance v8 | 🟢 정상 | 전 종목 응답 |
| FRED API | 🟢 정상 | FFR/금리 정상, DXY 1주 지연 |
| CoinGecko | 🟢 정상 | 실시간 가격 + 글로벌 데이터 |
| AlphaVantage | 🟡 부분 | BMNR 미지원 |
| TwelveData | 🟢 정상 | SPY/BTC/ETH 확인 |
| Brave Search | 🔴 장애 | API 키 미설정 — 뉴스 수집 불가 |

## ⚡ 주요 이벤트 확인

| 이벤트 | 상태 | 비고 |
|--------|------|------|
| FOMC | 다음 회의 미정 [미확인] | 3/19 FOMC 동결 완료 (기존 3.50-3.75%) |
| CPI | [미확인] | 금주 발표 스케줄 확인 불가 (검색 장애) |

## ⚠️ Alert

1. **BMNR 주간 -10.47%** → Price Drop Triage 발동 조건 충족
2. **VIX 26.78** → 25+ 돌파 → Macro 긴급 Regime 재판정 트리거
3. **ERII $9.35 장중 저점** → 52주 최저 터치, 엔트리 $9.5 하회
4. **BTC $67,885** → Kill $60K까지 -11.6% (이전 -14.9%에서 축소)
