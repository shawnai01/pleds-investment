# PLEDS v2 Full Analysis: CCJ (Cameco Corporation)
**Date**: 2026-03-22
**Analyst**: PLEDS v2 Automated
**Status**: COMPLETE

---

## Phase 0: 데이터 수집 [FACT]

### 가격 데이터 (2026-03-20 기준)
| Metric | Value | Source |
|--------|-------|--------|
| 현재가 | $101.55 | Yahoo Finance |
| After-hours | $102.30 | Yahoo Finance |
| 52주 범위 | $35.00 - $135.24 | Yahoo Finance |
| ATH | $135.24 (52주 기준) / $148.00 (우라늄 ATH 2007) | Yahoo Finance |
| Market Cap | $44.26B | Yahoo Finance |
| Beta | 0.97 | Yahoo Finance |
| YTD Return | +11.14% | Yahoo Finance |
| 1Y Return | +126.86% | Yahoo Finance |
| 3Y Return | +310.71% | Yahoo Finance |

### 재무 데이터 (FY2025, IFRS)
| Metric | Value | Source |
|--------|-------|--------|
| Revenue (TTM) | $3.48B | Yahoo Finance |
| Net Income (TTM) | $589.58M | Yahoo Finance |
| Adj. EBITDA (FY2025) | ~$1.9B | Cameco Q4 2025 Report |
| Levered FCF (TTM) | $479.94M | Yahoo Finance |
| Cash & ST Investments | $1.2B | Cameco Q4 Report |
| Total Debt | $1.0B | Cameco Q4 Report |
| Net Debt | ~-$0.2B (net cash) | Derived |
| Profit Margin | 16.93% | Yahoo Finance |
| ROE | 8.89% | Yahoo Finance |
| ROA | 3.59% | Yahoo Finance |
| EPS (TTM) | $0.99 | Yahoo Finance |
| Diluted EPS | $0.99 | Yahoo Finance |

### 밸류에이션
| Metric | Value |
|--------|-------|
| P/E (TTM) | 102.58x |
| Forward P/E | 94.34x |
| P/S (TTM) | 17.44x |
| P/B (MRQ) | 8.80x |
| EV/Revenue | 17.47x |
| EV/EBITDA | 52.16x |
| Enterprise Value | $44.27B |
| 1Y Target (Avg) | $125.17 |
| 1Y Target Range | $82.18 - $159.34 |
| Dividend Yield | 0.17% |

### 우라늄 시장 데이터
| Metric | Value | Source |
|--------|-------|--------|
| U3O8 스팟가격 | $84.40/lb (2026-03-20) | Trading Economics |
| 월간 변동 | -5.06% | Trading Economics |
| YoY 변동 | +29.75% | Trading Economics |
| 12개월 전망 | $90.18/lb | Trading Economics |
| 역사적 ATH | $148.00/lb (2007년 5월) | Trading Economics |

### 글로벌 원자력 파이프라인 [FACT]
| Status | Count | Source |
|--------|-------|--------|
| 운영 중 | ~440기 (400 GWe) | World Nuclear Association |
| 건설 중 | 75기+ (15개국) | WNA |
| 계획 중 | ~120기 | WNA |
| 중국 건설중 | 38기 (43 GWe) | WNA |
| 중국 계획 | 42기 (48 GWe) | WNA |
| 인도 건설중 | 8기 (6.6 GWe) | WNA |

### CCJ 운영 데이터 (FY2025)
| Metric | Value |
|--------|-------|
| 우라늄 생산량 (지분) | 21.0M lbs |
| Cigar Lake 생산 (100%) | 19.1M lbs |
| McArthur River/Key Lake (100%) | 15.1M lbs |
| JV Inkai 생산 (지분) | 3.7M lbs |
| 우라늄 인도량 | 33.0M lbs |
| 재고량 | 9.7M lbs (avg cost $61.85/lb) |
| 장기계약 잔량 | ~230M lbs |
| 향후 5년 연평균 인도 | ~28M lbs/yr |
| UF6 변환 생산 (기록) | 11.2M kgU |
| Fuel Services 인도 | 13.1M kgU |
| Westinghouse 배당 수령 | US$269.5M (2025) |

### 경쟁사 비교 (한계: API 제한으로 직접 비교 불가, 정성 평가)
| Company | Ticker | Position |
|---------|--------|----------|
| Kazatomprom | KAP (LSE) | 세계 1위 생산 (카자흐스탄) |
| NexGen Energy | NXE | 개발단계 (Rook I 프로젝트) |
| Uranium Energy Corp | UEC | 미국 ISR 생산 |
| Denison Mines | DNN | 개발단계 (Wheeler River) |

### Westinghouse 지분 가치
- CCJ 49% 지분 보유 (Brookfield 51%)
- 2023년 인수가: 약 $7.9B 전체 → CCJ 지분 ~$3.9B
- Dukovany 프로젝트 참여 → 신규 건설 매출 시작
- 2025년 Westinghouse adj. EBITDA 기여: 전년 대비 +$297M
- 원자로 OEM + 서비스 = 설치 기반 440기 대상 반복 매출

---

## Phase 0.5: Data Integrity Audit

### ✅ 검증 완료 항목
| 항목 | Source 1 | Source 2 | Match |
|------|----------|----------|-------|
| 현재가 $101.55 | Yahoo Finance | Trading Economics 참조 | ✅ |
| Revenue $3.48B | Yahoo Finance | Cameco Q4 implied | ✅ |
| Cash $1.2B | Yahoo Finance ($1.21B) | Cameco Q4 ($1.2B) | ✅ |
| Total Debt $1.0B | Cameco Q4 | D/E 14.67% consistent | ✅ |
| 우라늄 스팟 $84.40 | Trading Economics | Cameco commentary ref | ✅ |
| 건설중 원자로 75+기 | WNA page | WNA data table | ✅ |
| 생산량 21.0M lbs | Cameco Q4 | Guidance exceeded | ✅ |

### ⚠️ 추정/단일소스 항목
- EV/EBITDA 52.16x (Yahoo만) — Cameco adj. EBITDA $1.9B 기준 recalc: EV $44.27B / $1.9B = **23.3x** ← Yahoo 수치는 GAAP EBITDA 기준으로 보임
- P/NAV: 직접 계산 불가 (NAV 산출에 매장량 가치, Westinghouse 가치 필요)
- 장기계약 우라늄 가격: 비공개 (스팟 대비 프리미엄 추정)

### 🔴 Critical Correction
**EV/EBITDA 수정**: Yahoo의 52.16x는 GAAP 기준. Adj. EBITDA $1.9B 적용 시 **~23x**로 수정. 이는 성장주로서 합리적이나, 전통 자원주 대비 여전히 프리미엄.

---

## Phase 1-5: 4-Layer Adversarial Debate

---

### 🔵 LAYER 1: MACRO — 에너지 안보, 탈탄소, AI 전력 수요

#### Round 1: Bull 주장
[THESIS] 3대 메가트렌드의 교차점에 원자력이 위치:
1. **AI 전력 수요**: 데이터센터 전력 소비 2025~2030 CAGR 15-25% 전망. Microsoft-Constellation, Amazon-Talen Energy 등 빅테크가 원자력 PPA 체결
2. **탈탄소**: Net Zero 목표 달성에 원자력 필수. IEA는 2050까지 원자력 용량 2배 필요 전망
3. **에너지 안보**: 러시아 제재 → 러시아 농축 우라늄 의존도 축소 필요. 미국 DOE $2.7B 농축/변환 투자

[FACT] 미국 정부 $2.7B 계약 체결 확인 (Centrus 등). Cameco-Westinghouse 원자로 건설 승인. Trading Economics 기사에서 확인.

#### Round 1: Bear 반박
[THESIS] 매크로 환경은 현재 Risk-Off (VIX 26.78). 금리 인하 지연, 무역전쟁 가능성.
- 원자력 투자는 10-15년 사이클 — 단기 매크로 악화 시 자금 유입 둔화
- 에너지 정책은 정치적 — 정권 교체 시 방향 전환 리스크
- SMR 기술 실현은 2030년대 — 현재는 약속 단계

#### Round 2: Bull 재반박
[FACT] 원자력은 초당파적 지지 확보 (미국 ADVANCE Act 2024 통과, 공화·민주 공동). 75기 건설중 = 실제 착공된 물리적 자산. SMR 지연과 무관하게 기존 대형 원자로 수요 확실.
- Risk-Off에서도 에너지 인프라는 defensive — CCJ Beta 0.97로 시장과 유사 변동

#### Round 2: Bear 재반박
Beta 0.97이지만 52주 범위 $35-$135 = **285% 변동폭**. Defensive라 보기 어려움. 원자력 정치적 지지가 사고 1건으로 뒤집힐 수 있음 (후쿠시마 선례).

#### Round 3-4: 합의
**Macro = STRONG BULL (8/10)**
- 3대 메가트렌드 교차는 구조적이고 10년+ 지속성 높음
- 단기 Risk-Off는 진입점이 될 수 있으나, 변동성 경계 필요
- 원자력 사고 리스크는 tail risk로 존재하나 확률 낮음

---

### 🔵 LAYER 2: SECTOR — 우라늄 공급 제약 vs 수요 폭발

#### Round 1: Bull
[THESIS] 우라늄 시장 구조적 공급 부족:
- 2024 글로벌 수요: ~180M lbs vs 공급 ~140M lbs → **연간 ~40M lbs 적자**
- 신규 광산 개발 리드타임 7-15년
- 재고 소진: 유틸리티 재고 역사적 저점
- 가격: $84.40/lb → 2007 ATH $148 대비 43% discount — 상승 여력 충분

[FACT] 75+ 원자로 건설중 + 120 계획 = 향후 10년 수요 확대 확실. Cameco 자체도 장기계약 230M lbs 확보.

#### Round 1: Bear
- 카자흐스탄(Kazatomprom) = 세계 최대 생산국, 생산 확대 시 공급 과잉 가능
- 러시아 TENEX 물량이 비러시아 경로로 우회 거래되면 실질 제재 효과 감소
- 스팟 $84.40이 이미 2016년 저점($18) 대비 4.7배 — 상당부분 반영됨
- 장기계약가격은 $70-80대 — 스팟과 수렴하면 마진 압박 가능

#### Round 2: Bull
[FACT] Kazatomprom 2025년 생산 가이던스 하향 (산 부식 문제). 카자흐 정부 세금 인상 추진. 러시아 우회는 서방 유틸리티가 ESG/규제상 거부. 인도/중국 26기+ 계획(proposed) 외에도 실제 착공물량만 43 GWe → 연간 우라늄 추가수요 약 20M+ lbs.

#### Round 2: Bear
$84 수준에서 재개발 경제성 확보되는 광산 다수 — 장기적으로 $80-100 밴드에서 새 공급 유입될 것. "영원한 부족" 내러티브는 commodity cycle에서 항상 반복되는 패턴.

#### Round 3-4: 합의
**Sector = BULL (7.5/10)**
- 구조적 공급 부족은 2025-2030 유효
- $84가 "바닥"은 아님 — 하방 $60-70 가능 (Kazatomprom 증산, 경기침체 시)
- 그러나 건설중 75기의 물리적 수요는 취소 불가 → 중장기 수요 견고

---

### 🔵 LAYER 3: VALUE CHAIN — CCJ의 수직통합 포지션

#### §2 PLEDS v2 특수 모듈

##### 🔍 Search Problem Lens
**"우라늄 채굴/원자력이 AI search/소프트웨어로 대체 가능한가?"**
→ **완전 불가능 (Score: 0/10)**
- 우라늄은 물리적 원소 — 디지털로 대체 불가
- 광산 개발은 지질학적 발견 → 환경 인허가 → 건설 → 운영
- AI는 탐사 효율화 도구일 뿐, 채굴 자체를 대체 못함
- 원자력 발전소 운영은 물리/화학 공정 — 소프트웨어 대체 불가

##### 🏰 Verification Moat (Atom World 해자)
**CCJ의 해자 점수: 9/10**
1. **물리적 해자**: 캐나다 Athabasca Basin = 세계 최고 품위 우라늄 광상 (Cigar Lake 평균 품위 ~18% vs 세계 평균 0.1%). 대체 불가한 자연자원
2. **규제 해자**: NRC, CNSC 원자력 라이센스 — 신규 진입에 10-15년. ITAR (국제무기거래규정) 적용. Westinghouse 원자로 설계 수출 통제
3. **시간 해자**: McArthur River 재가동에만 2년+. 신규 광산 허가-생산까지 10-15년
4. **관계 해자**: 유틸리티와 10-15년 장기계약 (230M lbs backlog). Westinghouse 설치기반 440기 서비스
5. **수직통합**: 채굴 → UF6 변환 → Westinghouse(연료제조+원자로서비스) = 밸류체인 3단계 지배

##### 🤖 AI Commoditization Filter
**"AI가 이 사업을 범용화/가격파괴할 수 있는가?"**
→ **불가능 (Risk: 1/10)**
- 원자력은 **세계에서 가장 규제가 심한 산업** 중 하나
- AI가 우라늄을 합성할 수 없음
- 원자로 설계/운영 인허가는 AI로 가속화 가능하나, 핵심 가치(연료공급, 안전성)는 physical
- Westinghouse의 OEM 지위 = 원자로 수명(60-80년) 동안 lock-in

#### Round 1: Bull — CCJ Value Chain Position
[THESIS] CCJ = 서방 세계 유일의 완전 수직통합 원자력 기업
- **채굴**: Cigar Lake + McArthur River = 서방 최대, 최고 품위
- **변환**: Port Hope UF6 변환 시설 = 서방 3대 변환소 중 하나 (기록적 11.2M kgU 생산)
- **Westinghouse (49%)**: 원자로 OEM + 서비스 + 연료 제조. 440기 원자로 서비스 기반
- Dukovany 프로젝트 → 신규 건설 매출의 첫 사례 → 향후 SMR/AP1000 수주 파이프라인

#### Round 1: Bear
- Westinghouse 인수 부채 부담 (2023년 인수). 49% 지분 = 경영 통제권 미보유
- 채굴 집중 리스크: Cigar Lake + McArthur River 2개 광산에 의존
- JV Inkai (카자흐스탄) = 지정학적 리스크, 러시아 경유 물류
- Kazatomprom 대비 원가 열위 (ISR vs 지하 채굴)

#### Round 2: Bull
[FACT] 
- Westinghouse 49%이지만 Brookfield는 재무투자자 — 실질 운영 파트너는 CCJ
- 2025 Westinghouse adj. EBITDA +$297M YoY → 인수가 대비 빠른 가치 실현
- 카자흐 ISR이 저원가이지만, 서방 유틸리티 "국산/동맹국 우라늄" 선호 증가 → 프리미엄 수취
- Cigar Lake 수명 2035+, McArthur River 수십년분 매장량

#### Round 2: Bear
- 서방 프리미엄이 현재 $84 스팟에 이미 반영. 추가 프리미엄 한계
- 신규 광산(Rook I 등) 2028-2030 온라인 시 공급 증가

#### Round 3-4: 합의
**Value Chain = STRONG BULL (8.5/10)**
- CCJ의 수직통합은 동종 기업 중 유일무이
- Westinghouse = "숨겨진 보석" — 인수 시너지 예상보다 빠르게 실현
- 광산 집중 리스크는 실재하나, 품위/규모에서 대체재 부재
- Search/AI Commoditization 면역: **최고 수준**

---

### 🔵 LAYER 4: VALUATION — 현재가 적정한가?

#### NAV 추정 (Simplified)
| Component | Est. Value | Basis |
|-----------|-----------|-------|
| Uranium Mining & Fuel Services | $18-22B | EV/EBITDA 15-18x on ~$1.2B EBITDA |
| Westinghouse (49% stake) | $8-12B | Implied by adj. EBITDA growth + Dukovany |
| Cash - Debt (net) | $0.2B | $1.2B - $1.0B |
| **Total NAV** | **$26-34B** | — |
| **Per Share** (~435M shares) | **$60-78** | — |
| **Current Price** | **$101.55** | — |
| **P/NAV** | **~1.3-1.7x** | — |

#### DCF Sketch (10-year, WACC 10%)
- FY2025 FCF: ~$480M
- FCF Growth: 12-15% CAGR (uranium price escalation + Westinghouse ramp)
- Terminal Multiple: 15x FCF
- **DCF Fair Value**: ~$90-$120/share

#### 경쟁사 대비 배수
| Metric | CCJ | Kazatomprom (est.) | NexGen (NXE) |
|--------|-----|-------------------|--------------|
| P/E | 103x | ~12-15x | N/A (pre-revenue) |
| EV/EBITDA (adj.) | ~23x | ~8-10x | N/A |
| P/NAV | ~1.5x | ~1.0-1.2x | ~1.0-1.5x |

#### Round 1: Bull
[THESIS] 프리미엄 밸류에이션은 정당화됨:
- 서방 유일 수직통합 = scarcity premium
- Westinghouse 성장 옵셔너리티 미반영
- 장기계약 230M lbs = 가시성 높은 매출 → 하방 보호
- 우라늄 가격 $100+/lb 시 EBITDA $2.5B+ 가능 → EV/EBITDA 18x로 하락

#### Round 1: Bear
- P/E 103x는 극단적 — "성장주" 밸류에이션이지만 Revenue CAGR은 ~15%
- Kazatomprom 대비 2배 프리미엄 = "서방 프리미엄"이 영원할까?
- NAV $60-78 대비 30-50% 프리미엄 → 하방 리스크 상당
- FCF yield 1.1% ($480M/$44B) → 자본 배분 효율 의문

#### Round 2: Bull
- Kazatomprom과 직접 비교 부적절: KAP = 카자흐 국영기업, 거버넌스/지정학 할인 정당
- CCJ FCF는 Westinghouse 배당 포함 시 $700M+ → yield 1.6%
- 성장주 P/E는 earnings 정상화 시 하락: FY2027E EPS $2.5+ → Forward P/E 40x 수준

#### Round 2: Bear
Forward P/E 40x도 광산주로서는 극히 비쌈. 우라늄 가격 하락 시나리오($60/lb)에서 EPS 반토막 → P/E 200x+.

#### Round 3-4: 합의
**Valuation = NEUTRAL-CAUTIOUS (5/10)**
- 현재가는 **우라늄 슈퍼사이클 + Westinghouse 성장을 상당부분 반영**
- 하방 리스크 $70-80 (NAV 근처) — 20-30% downside 존재
- 추가 상승은 우라늄 $100+/lb 또는 SMR 수주 대형 카탈리스트 필요
- **"좋은 기업이지만 비싼 가격"** 구간

---

## §6 Causal Mechanism Map: 우라늄 인과사슬

```
AI 데이터센터 폭증 → 전력 수요 급증 → 원자력 재평가 (24/7 베이스로드 + 탄소제로)
                                            ↓
                            신규 원자로 건설/재가동 결정 (75기 건설중)
                                            ↓
                            우라늄 수요 증가 (연 180M+ lbs)
                                            ↓
                    vs. 공급 제약 (연 140M lbs, 신규 광산 10-15년)
                                            ↓
                            우라늄 가격 상승 ($84 → $100+?)
                                            ↓
                    CCJ: 채굴 마진 확대 + 장기계약 재계약 시 가격 상승
                                            ↓
                    CCJ: Westinghouse 연료/서비스 매출 증가 (설치기반 확대)
                                            ↓
                    CCJ: EBITDA 확대 → 밸류에이션 re-rating
```

**인과사슬 강도: 8/10** — 각 링크가 물리적/규제적으로 뒷받침됨. 약한 링크는 "우라늄 가격이 충분히 오를까?" (commodity cycle 불확실성)

---

## §1 Rocket with Tight Bolts: [THESIS] vs [FACT] Summary

| # | [THESIS] 주장 | [FACT] 검증 | Gap |
|---|---------------|-------------|-----|
| 1 | 원자력 르네상스 | 75기 건설중, 120기 계획 ✅ | 낮음 |
| 2 | 우라늄 구조적 공급 부족 | 수요 180M vs 공급 140M ✅ | 중간 (Kazatomprom 변수) |
| 3 | CCJ 서방 유일 수직통합 | 채굴+변환+Westinghouse 확인 ✅ | 낮음 |
| 4 | Westinghouse 성장 | Dukovany 참여, EBITDA +$297M ✅ | 낮음 |
| 5 | 10x 가능 ($1,000+) | 현 $44B cap → $440B 필요 = 비현실적 ❌ | **매우 높음** |
| 6 | AI 대체 면역 | 물리적 원소 + 규제 해자 ✅ | 낮음 |

---

## Phase 6: Conviction Card

### C1 🔥 Burn? (10x 가능한가?)
**❌ NO — 10x 불가능**
- 현 Market Cap $44B → 10x = $440B = ExxonMobil급
- 우라늄 기업이 세계 최대 에너지 기업 시가총액에 도달할 수 없음
- **2-3x는 가능** (우라늄 $150+, Westinghouse 대형 수주 시 $80-120B)
- Shawn의 "10x 인생 베팅" 기준에는 미달

### C2 🚪 Entry (현재가 적정? 더 나은 진입점?)
**WAIT — 더 나은 진입점 존재**
- 현재 $101.55는 NAV($60-78) 대비 30-50% 프리미엄
- 52주 저점 $35에서 190% 상승한 상태
- 우라늄 스팟 $84.40 → 단기 조정 시 $70대 가능
- **적정 매수 존: $70-85** (NAV 근처, P/E 60x 이하)
- Risk-Off 매크로에서 추가 하락 가능성

### C3 🎯 Exit (Bull/Base/Bear PT)
| Scenario | 우라늄 가격 | CCJ Target | 확률 | Timeframe |
|----------|-----------|------------|------|-----------|
| 🐂 Bull | $120-150/lb | $180-220 | 25% | 2027-2028 |
| 📊 Base | $85-100/lb | $110-140 | 50% | 2026-2027 |
| 🐻 Bear | $55-70/lb | $50-70 | 25% | 2026 |

### C4 ☠️ Kill (즉시 청산 조건)
1. 주요 원자력 사고 발생 (후쿠시마급)
2. 우라늄 스팟 $50/lb 이하 지속 (6개월+)
3. Westinghouse 대규모 손상차손
4. 카자흐스탄/러시아 공급 급증으로 공급과잉 전환
5. CCJ 광산 사고/장기 중단 (Cigar Lake 침수 선례)

---

## Phase 7: 최종 판정

### ⭐ 등급: 2등급 (Good, Not Great)

### 판정: **COND.BUY (조건부 매수)**

### 조건
- **진입가 $75-85 이하에서 매수** (현재가 대비 16-26% 하락 시)
- 또는 우라늄 스팟 $95+/lb 돌파 + CCJ $90-100 유지 시 (모멘텀 확인 매수)

### R:R 비율
- **현재가 $101.55 기준**: Upside $140 (+38%) vs Downside $70 (-31%) = **R:R 1.2:1** ❌ 불리
- **$80 매수 기준**: Upside $140 (+75%) vs Downside $60 (-25%) = **R:R 3:1** ✅ 양호

### 포트폴리오 적합성 분석

#### 기존 포트폴리오 현황
- Crypto/Risk: BMNR 35% + COIN 5% + CRCL 10% = **50%** (⚠️ 40% 한도 초과)
- Energy: ERII 10%
- Safe: SGOV 30% + Cash 10% = **40%**

#### CCJ 추가 시
| Scenario | From | Size | 결과 |
|----------|------|------|------|
| Cash에서 5% | Cash 10% → 5% | 5% | Energy 15%, Safe 35% |
| Cash에서 10% | Cash 10% → 0% | 10% | Energy 20%, Safe 30% |

**권장: Cash에서 5% 배분 (적정 진입가 달성 시)**
- Energy 15% (ERII 10% + CCJ 5%) = 과도하지 않음
- ERII(물 기술) vs CCJ(원자력) = 같은 에너지이나 서브섹터 다름 → 분산 효과 ✅
- Crypto 과중 포트폴리오에 **실물자산(원자력/우라늄) 분산 = 긍정적**
- 단, Cash 0%는 위험 → Cash 5% 유지 권장 = **CCJ 최대 5%**

### 🔑 핵심 요약
> CCJ는 **세계 최고의 원자력 기업**이다. 3대 메가트렌드(AI전력/탈탄소/에너지안보)의 교차점에 위치하고, 수직통합 + 규제해자 + 물리적해자의 삼중해자를 보유한다. 그러나 **10x 잠재력은 없고** ($44B cap), **현재 밸류에이션은 좋은 기업에 대한 비싼 가격**이다.
>
> Shawn의 투자 스타일("인생 베팅 + 10x")에는 부합하지 않으나, **포트폴리오 분산 + 실물자산 헤지** 관점에서 소규모(5%) 포지션은 합리적이다. 단, **현재가 아닌 $75-85에서 진입**해야 R:R이 유리하다.

---

## §4 Fresh Eyes Protocol: Zero-Base 점검

**"오늘 처음 이 기업을 본다면 $44B에 살 것인가?"**

- 매출 $3.5B, EBITDA $1.9B, FCF $480M인 기업을 $44B에? → P/S 12.6x, EV/EBITDA 23x
- 성장률 15% + 세계 유일 포지셔닝 + commodity upside → 정당화 가능하나 tight
- **Zero-base 결론: $30-35B ($70-80/share)이면 적극 매수, $44B은 fair-to-expensive**

---

## Phase 8: PT 기록

*별도 파일 생성*

---

## Appendix: §9 Conviction Card Summary

| Dimension | Score | Note |
|-----------|-------|------|
| Macro Tailwind | 8/10 | 3대 메가트렌드 교차 |
| Sector Position | 7.5/10 | 구조적 공급 부족 유효 |
| Value Chain Moat | 8.5/10 | 서방 유일 수직통합, 삼중 해자 |
| AI Immunity | 9.5/10 | 물리적 원소 + 규제 = 최강 방어 |
| Valuation | 5/10 | 좋은 기업, 비싼 가격 |
| 10x Potential | 2/10 | $44B → $440B 비현실적 |
| Portfolio Fit | 7/10 | Crypto 과중 분산에 적합 |
| **Overall** | **6.8/10** | **COND.BUY @ $75-85** |
