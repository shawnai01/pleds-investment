# LUNR (Intuitive Machines Inc.) — PLEDS Full System Deep Dive
## Fresh Eyes Protocol Applied | 2026-03-21

> ⚠️ Zero-Base: 이전 ⭐⭐ 판정 참조하지 않음. 오늘 처음 보는 종목으로 판단.

---

## Phase 0: Data Collection Summary

### 가격 데이터 [FACT]
| 항목 | 값 | 출처 |
|------|-----|------|
| 종가 (Mar 20) | $18.64 | Twelve Data |
| 52주 범위 | $6.14 – $23.32 | Finviz |
| 30일 범위 | ~$15.23 – $20.79 | Twelve Data |
| 시총 | $3.89B (Finviz) / ~$2.6B (Yahoo intraday) | Finviz/Yahoo |
| EV | $4.64B | Finviz |
| 발행주식 | 121.28M | Finviz |
| 유통주식 (Float) | 91.80M | Finviz |
| Perf YTD | +18.03% | Finviz |
| Perf 1Y | +169.42% | Finviz |
| Beta | 1.33 | Finviz |

### 재무 데이터 [FACT]
| 항목 | FY2025 | FY2024 | FY2023 | FY2022 | 출처 |
|------|--------|--------|--------|--------|------|
| Revenue | $210M | $228M | $80M | $86M | StockAnalysis/Macrotrends |
| Revenue Growth | **-7.87%** | +186.6% | -7.4% | — | StockAnalysis |
| Gross Profit | $9.0M | $2.8M | -$24.4M | $10.4M | StockAnalysis |
| Gross Margin | **2.57%** | 1.21% | -30.7% | 12.1% | Finviz/StockAnalysis |
| Operating Income | -$87.2M | -$57.4M | -$61.1M | -$5.5M | StockAnalysis |
| Net Income | -$83.9M | -$284.3M | +$59.4M | -$6.4M | StockAnalysis |
| EPS (diluted) | -$0.73 | -$4.63 | +$2.42 | — | StockAnalysis |
| FCF | -$55.95M | -$67.7M | -$75.2M | -$15.6M | StockAnalysis |
| Cash/sh | $2.88 | — | — | — | Finviz |
| Book/sh | **-$6.22** | — | — | — | Finviz |

### 밸류에이션 [FACT]
| 항목 | 값 | 해석 |
|------|-----|------|
| P/E (TTM) | N/A (적자) | 밸류에이션 불가 |
| Forward P/E | 88.41 | FY2026E EPS $0.22 기준 |
| P/S | 18.53 | Revenue $210M 대비 극도로 높음 |
| EV/Sales | 22.08 | 방산/우주 동종 대비 5-10x 프리미엄 |
| P/B | N/A | 자본잠식 (Book/sh = -$6.22) |

### Short Interest [FACT]
| 항목 | 값 |
|------|-----|
| Short Float | **32.99%** |
| Short Interest | 30.29M shares |
| Short Ratio | 2.69 days |

### 최신 이벤트 [FACT]
1. **Q4 2025 실적 발표 (Mar 19)**: EPS miss (-323.54%), Revenue miss (-16.62%) — Finviz
2. **$175M 희석적 주식 발행 (Feb 25)**: 위성통신/우주 데이터 처리 역량 확대 목적 → 주가 -15.9%
3. **L3Harris SDA Tranche 3 계약 수주 (Mar 3)**: 미사일 추적 위성 — 국방 확장
4. **Lanteris Space Systems 인수**: ~$800M 규모 우주 인프라 인수 [미확인 — Reddit 언급, 공식 금액 미확인]
5. **Stifel 다운그레이드 (Jan 9)**: Buy → Hold, PT $20
6. **Keybanc PT $26으로 상향 (Jan 28)**: 가장 높은 PT

### 분기별 매출 추이 [FACT]
| 분기 | 매출 |
|------|------|
| Q3 FY25 (Sep 30) | $52M |
| Q2 FY25 (Jun 30) | $50M |
| Q1 FY25 (Mar 31) | $63M |
| Q4 FY24 (Dec 31) | $55M |

→ **Q1→Q3 매출 감소 추세 ($63→$50→$52M)**. Q4 FY25 데이터 아직 미반영 (방금 발표, miss).

---

## Phase 0.5: Data Auditor

### 신뢰도 등급

| 데이터 항목 | 등급 | 비고 |
|------------|------|------|
| 가격/거래량 | ✅ | Twelve Data + Finviz 일치 |
| Revenue/EPS | ✅ | StockAnalysis + Finviz + Macrotrends 교차 일치 |
| Short Interest | ⚠️ | Finviz 단일 소스, 날짜 미명시 |
| 시총 | ⚠️ | Finviz $3.89B vs Yahoo $2.6B — **주식수 × 가격 불일치, Finviz가 diluted 기준일 가능성** |
| Lanteris 인수 금액 | ❌ | Reddit 언급만, 공식 소스 미확인 |
| Forward EPS $0.22 | ⚠️ | Forward P/E 88.41에서 역산, 컨센서스 소스 미확인 |

### ⚡ Data Conflicts
1. **시총 불일치**: Finviz $3.89B vs Yahoo ~$2.6B. 121.28M shares × $18.64 = $2.26B → Yahoo가 맞고, Finviz는 fully diluted shares 기준일 가능성. **실제 시총 ~$2.3B으로 판단.**
2. **Employees**: Finviz 525 vs Yahoo 435 — Lanteris 인수 후 증가 가능성

### SPAC 구조 확인
- IPO: Nov 17, 2021 (SPAC: Inflection Point Acquisition Corp.)
- Book/sh: **-$6.22** → 자본잠식 상태 [FACT]
- 워런트/희석: $175M 추가 발행 (Feb 2026), Shares Change YoY +88% (FY2025) [FACT]
- Insider Own: 35.49% — SPAC 치고는 높은 편 (긍정적?) [FACT]
- Insider Trans: -4.59% — 순매도 [FACT]

---

## Phase 1: Macro (L1)

### 1-1. The Machine (Ray Dalio)
**NASA 예산 및 우주 지출 사이클:**
- [FACT] NASA CLPS (Commercial Lunar Payload Services) 프로그램은 Artemis 프로그램의 일환
- [FACT] Artemis 프로그램은 정치적 지지가 초당적이나, 구체 일정은 지속 지연
- [THESIS] 국방우주(SDA/Space Force) 지출은 구조적 증가 추세 — L3Harris 계약이 이를 반영
- **레짐**: 정부 우주 지출은 Early/Mid Cycle — 아직 대규모 상업 우주경제는 미성숙

### 1-2. Liquidity Hawk (Druckenmiller)
- [FACT] LUNR은 소형 적자 성장주 → 금리/유동성에 극도로 민감
- [FACT] Forward P/E 88x → 할인율 변화에 밸류에이션 취약
- [THESIS] 현재 금리 환경에서 이런 밸류에이션은 "꿈 프리미엄"에 의존
- **판정**: 유동성 Neutral — 긴축 강화 시 가장 먼저 타격받는 종류

### 1-3. Cycle Sentinel (Howard Marks)
- [FACT] 우주 테마 ETF (UFO, ARKX) 활성, SpaceX IPO 기대감으로 섹터 전체 과열 조짐
- [FACT] LUNR Perf 1Y +169% — 강한 모멘텀
- [THESIS] 시장 온도 7/10 (탐욕 쪽) — SpaceX IPO 내러티브가 우주주 전체를 끌어올리는 중
- **판정**: 테마 과열 경계. 내러티브가 실적을 앞서가는 전형적 구간.

### 1-4. Contrarian Catalyst (Soros/Burry)
- 🔴 **Artemis 지연/축소 시나리오**: 정권 교체, 예산 삭감 시 NASA CLPS 물량 급감 가능
- 🔴 **DOGE/정부 효율화**: 트럼프 행정부의 정부 지출 삭감이 NASA 계약에 영향 가능 [THESIS]
- 🔴 **SpaceX IPO 역설**: IPO 후 자금이 SpaceX로 집중되면 LUNR 같은 소형주에서 이탈 가능

### Macro Moderator 종합
- **Regime**: Neutral (정부 우주지출 확대 vs 금리/유동성 역풍)
- **핵심 변수**: Artemis 예산, Fed 금리 경로, SpaceX IPO 시점
- **확률**: Risk-On 35% / Neutral 40% / Risk-Off 25%

---

## Phase 2: Sector (L2)

### 2-1. Disruptor (Cathie Wood)
- [THESIS] 달 경제(Lunar Economy)는 2030년대 중반 $100B+ TAM이 될 수 있다 — 단, S-curve 극초기
- [FACT] 현재 달 경제의 "고객"은 거의 100% NASA + 동맹국 정부기관
- [THESIS] 상업 달 화물 수요는 10년 이상 후 — 달 기지, 자원 채굴은 아직 SF 수준
- **현실 체크**: TAM이 "실현 불확실한 미래"에 기반. 지금은 정부 계약 비즈니스.

### 2-2. Value Mapper (Damodaran)
- [FACT] LUNR EV/Sales 22x vs 방산 대형주(LMT 1.7x, RTX 2.7x, LHX 2.6x) → **8-12배 프리미엄**
- [FACT] LUNR EV/Sales 22x vs Rocket Lab (RKLB) — 비교 필요하나 RKLB도 고밸류 [미확인]
- [THESIS] 이 프리미엄은 "달 독점 포지션 + 미래 성장"에 대한 옵션 가치. 실적으로 정당화 불가.
- **적정 밸류에이션**: Revenue $210M × 방산 평균 5x P/S = ~$1.05B → **현재 $2.3B 대비 55% 고평가**

### 2-3. Theme Hunter (Peter Lynch)
- [FACT] "달의 FedEx" 내러티브 — 유일한 상장 달 착륙 기업
- [FACT] 경쟁: Astrobotic (비상장, IM-1 전 Peregrine 미션 실패), Firefly Aerospace (최근 상장, $3.1B 시총)
- [THESIS] 유일무이한 "달 순수주(Pure Play)" → 테마 ETF/리테일 수요 집중
- **리스크**: 순수주(Pure Play) 프리미엄은 테마 사이클에 따라 급격히 수축 가능

### Sector Moderator 종합
- **산업 매력도**: 6/10 — 장기 잠재력 높으나 현재 수익 모델 미확립
- **LUNR 섹터 포지션**: 유일한 상장 달 착륙 Pure Play → 희소 프리미엄 존재하나, 펀더멘탈 부재

---

## Phase 3: Value Chain (L3)

### 달 물류 밸류체인 매핑

```
발사 (SpaceX) → 궤도 이동 (LUNR Nova-C) → 달 착륙 (LUNR) → 화물 배달 (LUNR) → 지상 운용 (LUNR/NASA)
```

### 3-1. Strategist (Porter/Dorsey)
- **LUNR의 위치**: 착륙 + 배달 — 밸류체인 중간
- **상류 의존성**: 발사체는 SpaceX에 100% 의존 [FACT]
- **하류 의존성**: 수요는 NASA에 ~90%+ 의존 [FACT 기반 추정]
- **해자**: 달 착륙 기술은 진입장벽 높음 (Astrobotic Peregrine 실패가 증명)
- **BUT**: IM-1 Odysseus도 옆으로 착륙 → **기술 신뢰도 미확립** [FACT]

### 3-2. Network Thinker
- [THESIS] 달 데이터 네트워크(Lunar Data Network) 구축 시 네트워크 효과 가능 — 먼 미래
- [FACT] 현재는 일회성 미션 기반 수익 → 반복 수익 모델 없음
- **판정**: 네트워크 효과는 5-10년 후 가능성, 현재 해당 없음

### Bottleneck Hunter (Phase 3 관점)
- **현재 병목**: 달 접근의 병목은 **수요(Demand)**, 착륙 기술이 아님
  - 발사: SpaceX가 해결 (병목 아님)
  - 착륙: 기술 자체는 가능하나 신뢰도 미확립 (50% 성공률?)
  - **수요**: NASA만이 유일한 고객. 상업 수요 없음 → 이것이 진짜 병목
- [THESIS] LUNR은 "병목 소유자"가 아님. 병목(수요)에 **의존하는** 기업.

---

## Phase 4: Company (L4)

### 4-1. Compounder (Buffett/Terry Smith)
- **매출 구조**: NASA 계약 중심, L3Harris SDA(국방) 확장 시도
- **매출 추이**: FY2024 $228M → FY2025 $210M (**-7.87% 감소**) [FACT]
  - FY2024 급증은 IM-1 미션 매출 인식 효과 → 비반복
- **Gross Margin 2.57%**: 사실상 원가 수준에서 납품 → **가격결정력 부재** [FACT]
- **Operating Margin -41.53%**: SG&A $92.6M이 매출의 44% → 과도한 간접비 [FACT]
- **FCF**: 연 -$56M~-$76M 지속 소진 [FACT]
- **Cash**: $2.88/sh × 121M = ~$349M → **약 6년 소진** (현 burn rate 기준, 단 인수/투자 제외)
- **자본잠식**: Book/sh -$6.22 → 자기자본 음수 [FACT]
- **결론**: Compounder 관점에서 **투자 부적격**. ROIC 음수, FCF 음수, 마진 없음.

### 4-2. Catalyst Hunter (Ackman/Einhorn)
**잠재 촉매:**
1. 🟢 **IM-2 미션 성공**: 성공적 달 착륙 시 기술 검증 → 주가 급등 가능 [미확인 — 일정 불명]
2. 🟢 **추가 CLPS 수주**: NASA 추가 계약 시 백로그 확대
3. 🟢 **SDA/국방 확장**: L3Harris 계약 외 추가 국방 수주
4. 🟢 **SpaceX IPO 연계**: 우주 테마 전체 re-rating
5. 🟢 **Artemis 프로그램 가속**: 정치적 결정에 의한 일정 당김

**촉매 실현 확률**: IM-2 성공이 가장 중요하나 일정 불명 [미확인]

### 4-3. Forensic Accountant (Chanos/Hindenburg) — 🔴 Bear Case 의무

#### Bear Case #1: Short 33% — 왜?
- [FACT] 30.29M shares short / 91.8M float = 33%
- [THESIS] 숏 세력의 논리 추정:
  1. **밸류에이션 괴리**: EV/Sales 22x, 적자, 자본잠식 기업에 $3.9B 시총
  2. **매출 역성장**: FY2025 -7.87% — 성장 스토리 훼손
  3. **지속적 희석**: FY2025 주식수 +88% YoY, $175M 추가 발행 → 기존 주주 가치 파괴
  4. **기술 미검증**: IM-1 옆으로 착륙 → 신뢰도 문제
  5. **단일 고객 의존**: NASA 의존도 극히 높음

#### Bear Case #2: IM-1 Odysseus — 기술 신뢰도
- [FACT] IM-1 (Feb 2024): Odysseus 착륙선이 달 표면에 **옆으로 넘어져** 착륙
- 미션은 "부분 성공"으로 평가되었으나, 이것이 기술 성숙도의 증거인가?
- [THESIS] 달 착륙 성공률은 역사적으로 ~50% 미만 — 어려운 기술이지만, "FedEx"로서의 신뢰도에는 의문

#### Bear Case #3: NASA 단일 고객 의존
- [FACT] 매출의 대부분이 NASA CLPS 계약 (SDA 국방 계약은 최근 시작)
- [THESIS] NASA 예산 삭감/Artemis 축소 시 매출 기반 붕괴
- 상업 고객 파이프라인 [미확인]

#### Bear Case #4: 희석 구조
- [FACT] FY2021 주식 39M → FY2025 121M → **3배 이상 증가**
- [FACT] $175M 추가 발행 (Feb 2026) → 추가 희석
- [FACT] FCF 음수 → **추가 증자 불가피** (매년 $50-75M 현금 소진)
- [THESIS] 현재 캐시 ~$349M이지만, Lanteris 인수 + 운영 적자 → 12-18개월 내 추가 증자 가능

#### Bear Case #5: 달 경제 TAM — 꿈 vs 팩트
- [FACT] 현재 달 화물 시장 = 연 수억 달러 규모 (CLPS 총 예산 ~$2.6B, 10년 이상)
- [THESIS] 상업 달 경제는 2035년 이전에는 의미 있는 규모에 도달하기 어려움
- [THESIS] 자원 채굴(헬륨-3, 물)은 기술적/경제적으로 수십 년 거리

#### Bear Case #6: -50% 시나리오
- **트리거**: IM-2 실패 + Artemis 예산 삭감 + 추가 증자 발표
- **경로**: $18.64 → $9-10 (52주 저점 $6.14는 이미 경험)
- **확률**: [THESIS] 25-30% — IM-2 실패 단독으로도 -30% 가능

### Company Moderator 종합
- **확신도**: 3/10
- **Bull**: 달 독점 Pure Play, 국방 확장, 장기 옵션 가치
- **Bear**: 적자, 희석, 단일 고객, 기술 미검증, 밸류에이션 과도
- **핵심 모니터링**: IM-2 미션 일정/결과, 분기별 매출/마진 추이

---

## Phase 4.5: Technical Dashboard (v3.1)

### 지표 시계열 [FACT — Twelve Data API]

| 날짜 | RSI(14) | MACD | MACD Signal | MACD Hist | BB Upper | BB Mid (SMA20) | BB Lower | ADX(14) |
|------|---------|------|-------------|-----------|----------|----------------|----------|---------|
| 3/20 | 53.1 | 0.200 | 0.096 | +0.104 | $19.43 | $17.94 | $16.46 | 8.84 |
| 3/19 | 54.3 | 0.171 | 0.070 | +0.101 | $19.35 | $17.89 | $16.43 | 8.90 |
| 3/18 | 51.1 | 0.105 | 0.045 | +0.060 | $19.25 | $17.85 | $16.46 | 9.02 |
| 3/17 | 54.7 | 0.100 | 0.030 | +0.070 | $19.22 | $17.84 | $16.45 | 8.92 |
| 3/16 | 49.7 | 0.012 | 0.013 | -0.001 | $19.12 | $17.72 | $16.33 | 8.81 |

### 기계적 판독

| 지표 | 상태 | 해석 |
|------|------|------|
| RSI(14) | 53.1 | **중립** (30-70 범위) |
| MACD | Hist +0.104, 상승 중 | **약한 매수 시그널** (제로 상향 크로스 완료) |
| Bollinger Bands | 종가 $18.64 > Upper $19.43 근접 | **상단 접근** — 단기 과열 주의 |
| ADX(14) | **8.84** | **극히 약한 추세** (<20 비추세, <10 극히 약함) |
| SMA20 | $17.94 | 가격 > SMA20 (단기 양호) |
| SMA50 | 가격 대비 +3.93% | 양호 |
| SMA200 | 가격 대비 +48.52% | **장기 강세** 유지 |

### 기술적 등급: 🟡 Tech Neutral
- ADX 극히 낮음 → 뚜렷한 추세 없음, 횡보/변동성 구간
- MACD 약한 매수 시그널이나 ADX가 이를 뒷받침하지 못함
- SMA200 대비 +48.5% → 평균회귀 리스크 존재
- **한계**: 소형주 + 높은 변동성(일 평균 9.5-9.9%) → 기술적 지표 신뢰도 낮음

---

## Phase 5: Cross-Layer — Bottleneck Hunter

### "달의 FedEx" — 10년 후 유효한가?

**[THESIS — Bear]**: SpaceX Starship HLS가 LUNR의 존재 이유를 위협
- Starship은 100t+ 달 화물 능력 → Nova-C의 100kg 급과 비교 불가
- NASA가 Starship을 유인 착륙선(HLS)으로 선정 → 무인 화물도 Starship으로 가능
- [THESIS] 장기적으로 LUNR은 "택시" vs SpaceX는 "화물선" → LUNR의 니치가 좁아짐

**[THESIS — Bull]**: LUNR은 소형/정밀 배달에 특화
- Starship은 대형 화물에 최적화 → 소형 과학 장비 배달에는 비효율
- NASA CLPS는 다수 공급자 전략 유지 (경쟁 + 리던던시)
- [THESIS] "달의 FedEx" vs "달의 화물선" — 공존 가능하나 TAM 제한적

### NASA가 LUNR 없이 달에 화물을 보낼 수 있는가?
- **예.** Firefly (Blue Ghost), Astrobotic (재시도 예정), SpaceX Starship — 대안 존재 [FACT]
- LUNR은 현재 "첫 번째 성공적 상업 달 착륙" (부분 성공이지만) → 선점 효과 [FACT]
- [THESIS] 경쟁 진입장벽은 기술적으로는 높지만, 정치적/계약적으로는 낮음 (CLPS 복수 공급자)

### 경쟁 진입장벽
- **높은 것**: 달 착륙 기술 자체 (Astrobotic 실패 증명), NASA 관계/실적
- **낮은 것**: CLPS 계약은 NASA가 의도적으로 복수 공급자 육성, SpaceX 진입 가능

### Bottleneck Hunter 최종 판정
- 🔴 **현재 병목**: 상업 수요 부재 — 정부 수요만으로는 성장 제한적
- 🟡 **차기 병목**: 기술 신뢰도 (IM-2 성공 여부가 결정)
- 🟢 **병목 소유자**: LUNR은 병목 소유자가 **아님**. 수요(NASA)에 의존하는 공급자.
- **결론**: Bottleneck Owner Premium을 부여할 수 없음.

---

## Phase 6: Synthesis — Conviction Convergence

### Bear-First (Fresh Eyes 규칙 2)

**-50% 시나리오 ($18.64 → $9.30):**
1. IM-2 실패 → 기술 신뢰도 완전 훼손
2. Artemis 예산 삭감 → 파이프라인 축소
3. 추가 증자 → 주식수 150M+ → 시총 유지해도 주가 하락
4. SpaceX IPO → 자금 이동
5. **확률 추정: 25%**

**-80% 시나리오 ($18.64 → $3.70):**
1. IM-2 실패 + Artemis 취소 + 현금 고갈 → 생존 위기
2. **확률 추정: 10%**

### Bull Case
**+100% 시나리오 ($18.64 → $37):**
1. IM-2 성공 → 기술 검증
2. CLPS 추가 대형 계약 + SDA 국방 확장
3. 매출 $300M+ 달성, 마진 개선 시작
4. 우주 테마 리레이팅
5. **확률 추정: 15%**

**+200%+ 시나리오 ($18.64 → $55+):**
1. 상업 달 경제 가시화 + Artemis 성공적 진행
2. 달 데이터 네트워크 독점
3. **확률 추정: 5-7%**

### 기대값 계산 (대략적)
| 시나리오 | 확률 | 가격 | 수익률 | 가중 기여 |
|----------|------|------|--------|-----------|
| -80% (생존위기) | 10% | $3.70 | -80% | -8.0% |
| -50% (미션실패) | 25% | $9.30 | -50% | -12.5% |
| 현상유지 | 43% | $18.64 | 0% | 0% |
| +100% (검증) | 15% | $37 | +100% | +15% |
| +200% (달경제) | 7% | $55 | +195% | +13.7% |
| **가중 평균** | | | | **+8.2%** |

→ 기대값은 약간 양수이나, **변동성 극히 높고 (vol 9.5%/일), 기대값의 대부분이 낮은 확률 시나리오에 의존.**

---

## Conviction Card

### C1 🔥 Burn?
**⭐½ (1.5/3)** | Risk:Reward = **1:1.5 (부정적)** | "달 독점 Pure Play이나, 적자+희석+단일고객+기술미검증. 꿈 프리미엄이 펀더멘탈을 10배 이상 초과."

- 크게 태울 근거 **부족**
- 바이너리적 성격 강함: IM-2 성공 vs 실패가 주가를 50%+ 움직일 수 있음
- Short 33%가 시사하는 바: 시장의 상당수 참여자가 고평가로 판단

### C2 🚪 Entry
- **진입 조건**: IM-2 미션 성공 확인 **후** 진입 (사전 투기 비추)
- 또는 $12 이하로 하락 시 소규모(1-2%) 비대칭 베팅 고려
- 현재 $18.64는 Q4 miss + Short 33% 감안 시 매력적이지 않음

### C3 🎯 Exit
- 6mo: $20-22 (SDA 확장 + 시장 유지 시)
- 1yr: $25-30 (IM-2 성공 + 매출 회복 시)
- 3yr: $40-60 (달 경제 초기 실현, 국방 매출 확대 시)
- **현실적 기대**: 현 수준에서 6mo +10-15% 정도

### C4 ☠️ Kill
- IM-2 미션 실패 (착륙 실패/부분 성공 미달)
- Artemis 프로그램 예산 30%+ 삭감 or 정치적 중단
- 2회 연속 분기 매출 $40M 미만 (성장 모멘텀 완전 상실)
- 추가 증자 $200M+ (현 가격 기준 주식수 10%+ 희석)
- **기한**: 2027-06 — 이 시점까지 IM-2 미실행 or 매출 $250M 미달 시 테시스 폐기

---

## "100배 똑똑한 Shawn이라면?"

### 핵심 판단

**이 종목은 "소규모 비대칭 베팅"으로서도 현재 가격에서는 매력이 부족하다.**

이유:
1. **비대칭이 아님**: 상방(+100%)과 하방(-50%)의 확률이 비슷(15% vs 25%) → 비대칭 구조가 아니라 **대칭적 도박**
2. **Short 33%가 시사하는 진짜 메시지**: 이 기업을 가장 잘 아는 사람들(기관 숏 세력) 중 상당수가 고평가로 판단
3. **매출 역성장 + Gross Margin 2.57%**: "달의 FedEx"인데 배달하면 할수록 적자 — 비즈니스 모델 자체가 미검증
4. **SPAC 희석 구조**: 주식수 3년간 3배 증가, 추가 증자 불가피 → 주당 가치 지속 희석

### 그래도 살 수 있는 유일한 논리
- **IM-2 성공 확인 후** $12-15 수준에서 **포트폴리오의 1-2%** 이내
- 이것은 "달 경제 옵션"을 가장 저렴하게 사는 방법
- 그러나 현재 $18.64에서는 옵션 프리미엄이 이미 과도

### 최종 조언
**관망(WATCH)**. 현재 진입하지 않는다.
- IM-2 미션 결과 확인까지 대기
- Short squeeze 가능성은 존재하나, 이것은 투자가 아니라 투기
- "달의 FedEx"는 매력적 내러티브이나, 현재 FedEx가 배달마다 적자를 보고 있다면 아무도 FedEx 주식을 사지 않을 것

---

## Layer별 점수 요약

| Layer | 점수 | 가중치 | 가중점수 |
|-------|------|--------|----------|
| L1 Macro | 5/10 | 0.25 | 1.25 |
| L2 Sector | 6/10 | 0.20 | 1.20 |
| L3 Value Chain | 3/10 | 0.10 | 0.30 |
| L4 Company | 3/10 | 0.30 | 0.90 |
| L5 Technical | 5/10 | 0.15 | 0.75 |
| **Final Score** | | | **4.40/10 → 0.11** |

→ Final Score 0.11 → 확신도 ⭐ (보통) → 포지션 3-8% 범위의 최하단
→ **그러나 Bear case 강도와 Short 33% 감안 시 관망(0%) 권장**

---

## 전문가 투표 결과

| 전문가 | 방향 | 확신도 | 코멘트 |
|--------|------|--------|--------|
| Machine | Neutral | 5/10 | 정부 우주지출은 긍정적이나 기업 레벨 불확실 |
| Liquidity Hawk | Bearish | 3/10 | 소형 적자주에 88x Forward P/E는 유동성 역풍에 취약 |
| Cycle Sentinel | Cautious | 4/10 | 우주 테마 과열, 내러티브 > 실적 |
| Contrarian | Bearish | 3/10 | Artemis 리스크 과소평가 |
| Disruptor | Bullish | 7/10 | 달 경제 S-curve 극초기, 선점자 프리미엄 |
| Value Mapper | Bearish | 2/10 | EV/Sales 22x는 어떤 성장으로도 정당화 어려움 |
| Strategist | Neutral | 4/10 | 병목 소유자 아님, 수요 의존 |
| Compounder | Bearish | 2/10 | 적자, 희석, 마진 없음 — 투자 부적격 |
| Catalyst Hunter | Neutral | 5/10 | IM-2가 유일한 의미있는 촉매 |
| Forensic Accountant | Bearish | 2/10 | Short 33%, 자본잠식, 연속 희석 |
| Bottleneck Hunter | Bearish | 3/10 | 수요 병목 의존자, 소유자 아님 |

**평균: 3.6/10 | 표준편차: 1.6 | High Disagreement ❌ (SD < 2)**

---

*PLEDS Full System Run — Fresh Eyes Protocol Applied*
*Data as of 2026-03-20/21*
*[FACT]/[THESIS]/[미확인] 태그 적용*
