# PLEDS Workflow — Step by Step

## 일일 브리핑 워크플로우 (매일 09:00 KST)

### Phase 0: 데이터 수집 (자동/크론, ~08:30)
```
수집 항목:
├── Macro: 전일 종가 — SPY, QQQ, DXY, TLT, GLD, USO, VIX, BTC, ETH
├── Macro: 금리 — FFR, 2Y, 10Y, 2-10 spread, HY spread
├── Macro: Fed/ECB 발언 스캔
├── Sector: 섹터 ETF 성과 (XLK, XLF, XLE, XLV, XLI, XLC, XLU, XLRE, XLB, XLP, XLY)
├── Company: 전일 어닝 서프라이즈, 내부자 거래, 13F 업데이트
├── Chart: 워치리스트 종목 가격/거래량
├── Crypto: BTC, ETH, MVRV, BTC.D, USDT.D, funding rates
└── News: 주요 헤드라인 10개
```

### Phase 0.5: Data Integrity Audit (신규)

**참여:** The Data Auditor (데이터 감사관)

**목적:** Phase 0에서 수집된 모든 데이터를 전문가 토론에 투입하기 전에 교차검증

**절차:**
1. **가격 데이터 교차검증** — 각 자산 가격을 2개+ 소스에서 확인 (CoinGecko vs Yahoo Finance vs Google Finance 등)
2. **재무 데이터 원본 대조** — SEC filing(10-K/10-Q) 원본 vs 스크리너 수치 비교. 기간(TTM vs 분기 vs 연환산) 명시 강제
3. **변동률 기준 시점 명시** — 전일 종가 대비, 주간, 월간 등 기준점을 반드시 기재
4. **신뢰도 등급 부여:**
   - ✅ **Verified** — 2개+ 소스 일치 (허용 오차 ±2%)
   - ⚠️ **Single-Source** — 1개 소스만 확인. 전문가 인용 시 `[단일출처]` 표기 의무
   - ❌ **Unverified** — 확인 불가. **투자 판정에 사용 금지** (참고만 가능)
5. **교차검증 불일치 5% 이상** → `⚡ Data Conflict` 플래그 → 해당 데이터 사용 시 Moderator가 명시적 판단

**산출물:** `daily/YYYY-MM-DD-data-audit.md`
```
| 항목 | 값 | 소스1 | 소스2 | 등급 | 비고 |
|------|---|-------|-------|------|------|
| BTC | $71,173 | CoinGecko | Yahoo | ✅ | 차이 0.02% |
| FFR | 4.25-4.50% | — | — | ❌ | FOMC 날짜 기준 추정 |
```

**핵심 규칙:**
- ❌ Unverified 데이터로 매수/매도 판정 금지
- ⚠️ Single-Source 데이터는 전문가가 인용 시 반드시 `[단일출처]` 표기
- Data Auditor는 검증 결과만 제공하며 투자 의견을 제시하지 않음 (독립성 유지)
- **FOMC/CPI 등 이벤트 당일**: 발표 시점(보통 미국 ET 14:00 = KST 익일 04:00) 확인 → 미발표 시 `[발표 대기중]` 표기, 절대 추정값으로 채우지 않음
- **데이터 소스 우선순위**: API(CoinGecko, FRED, Yahoo Finance API) > 뉴스 사이트(web_fetch) > 추정(금지)
- 전문가 토론에서 Phase 0 테이블과 다른 수치를 사용하면 안 됨 — Phase 0 데이터만 인용

---

### Phase 1: Layer 1 — Macro Debate (~15분)

**참여:** The Machine, The Liquidity Hawk, The Cycle Sentinel, The Contrarian Catalyst, **The Bottleneck Hunter (Cross-Layer)**, Macro Moderator

**절차:**
1. 각 전문가가 1-2문장으로 현재 뷰 제시 (독립적)
2. Contrarian이 컨센서스의 반대 논거 제시 (의무)
3. Moderator가 핵심 분기점(fork) 식별
4. 토론 (2-3 라운드)
5. **투표:** Regime (Risk-On / Neutral / Risk-Off) + 확률 %
6. **산출물:** `layers/L1-macro/regime-tracker.md` 업데이트

### Phase 2: Layer 2 — Sector Scan (~10분)

**참여:** The Disruptor, The Value Mapper, The Theme Hunter, **The Bottleneck Hunter (Cross-Layer)**, Sector Moderator

**절차:**
1. Macro regime을 전달받고 산업 영향 분석
2. 각 전문가가 유망/역풍 산업 3개씩 제시
3. 비컨센서스 테마 1개 이상 의무 발굴 (Theme Hunter)
4. **투표:** 산업 매력도 Top 5 + 회피 산업
5. **산출물:** `layers/L2-sector/sector-rankings.md` 업데이트

### Phase 3: Layer 3 — Value Chain Analysis (~5분)

**참여:** The Strategist, The Network Thinker, **The Bottleneck Hunter (Cross-Layer, 주도적 역할)**, Value Chain Moderator

**절차:**
1. Phase 2에서 선정된 유망 산업의 밸류체인 매핑
2. 가치 집중 노드 식별 (곡괭이, 플랫폼, 톨게이트)
3. **산출물:** `layers/L3-valuechain/frameworks.md` 업데이트

### Phase 4: Layer 4 — Company Deep Dive (~15분)

**참여:** The Compounder, The Catalyst Hunter, The Forensic Accountant, **The Bottleneck Hunter (Cross-Layer)**, Company Moderator

**절차:**
1. 워치리스트 + 현재 보유 종목 리뷰
2. 신규 종목 후보 검토 (Phase 2-3에서 도출)
3. Forensic Accountant가 모든 매수 후보에 Bear Case 제시 (의무)
4. **투표:** 종목별 확신도 (1-10) + 적정가 + 액션
5. **산출물:** `layers/L4-company/watchlist.md` + `active-positions.md` 업데이트

### Phase 5: Layer 5 — Chart & Timing (~15분)

**참여:** The Momentum Master, The Accumulation Reader, The Wave Counter, The Quant Signal, Chart Moderator

**절차:**
1. Phase 4 통과 종목의 차트 분석
2. 크립토: BTC, ETH 파동 카운트 + MVRV/도미넌스 분석 (Wave Counter 전담)
3. 진입/청산 타이밍 토론
4. **투표:** 기술적 등급 + 진입 구간 + 손절 라인
5. **산출물:** `layers/L5-chart/signals.md` 업데이트

### Phase 4.5: Technical Data Pipeline (~자동)

**절차:**
1. `bash data/collect-indicators.sh` — Twelve Data에서 OHLCV + RSI/MACD/BB/ADX 수집
2. `python3 data/generate-dashboard.py` — 시계열 분석 + TECHNICAL-DASHBOARD.md 생성
3. 대시보드의 기계적 등급(🟢/🟡/🔴/⚪)을 Phase 6 Allocator에게 전달

**원칙:**
- 대시보드는 팩트(숫자+기계적 판정)만 제공. LLM TA 의견 금지.
- 시계열 데이터는 `data/` 디렉토리에 일 1회 누적 적재.
- L5는 L1-L4를 override하지 않음 — 타이밍 보조 역할.

### Phase 6: Synthesis — Conviction Convergence (~10분)

**참여:** The Allocator (수석 투자 책임자)

**원칙:** Phase 1-5의 자유 토론 결과를 읽고, Conviction Card (C1-C4)로 수렴한다.

**절차:**
1. 5개 Layer + Cross-Layer(Bottleneck Hunter) 결과 종합
2. 확률 가중 계산 (METHODOLOGY.md 공식)
3. **모든 종목/테마에 Conviction Card 작성:**
   - C1 🔥 Burn? — 태울 만한가? (⭐~⭐⭐⭐ + 비대칭 배율)
   - C2 🚪 Entry — 진입 조건 (가격, 시점, 이벤트)
   - C3 🎯 Exit — 목표가/익절 (시간축별)
   - C4 ☠️ Kill — 가설 폐기/손절 조건 (기계적 실행)
4. 기존 보유 종목의 C2/C3/C4 **조건 달성 여부 체크** (Pre-Commitment Trigger)
5. 포지션 사이징 결정
6. '100배 똑똑한 Shawn이라면?' 섹션
7. **산출물:**
   - `synthesis/action-list.md` — 오늘의 투자 액션 + Conviction Cards
   - `synthesis/conviction-cards.md` — 전 종목 카드 누적 관리
   - `daily/YYYY-MM-DD.md` — 일일 브리핑 전문

### 운영 규칙 (전 Phase 공통)

1. **포트폴리오 변경 권한**: PLEDS는 제안만 함. Shawn이 명시적으로 변경을 말하지 않는 한 기존 배분 유지. PORTFOLIO.md 수정은 Shawn 지시 시에만.
2. **동조 금지**: Shawn의 테시스에 무조건 동조하지 않음. 전문가들은 독립적으로 반론/지지 제시.
3. **"100x Shawn" 프레임**: 매 브리핑 말미에 "100배 똑똑한 Shawn이라면?" 섹션 포함. 동일한 리스크 성향 + 시드 극대화 목표를 가진 최적 의사결정자의 관점.
4. **블랙스완 워치**: 보유 종목의 existential risk (회사가 깨지는가?)를 매일 모니터링. 경고 시 즉시 알림.
5. **GitHub 아카이빙**: 모든 일일 브리핑, 데이터 검증, 포트폴리오 변경을 git commit + push.

### Phase 7: Delivery (~09:00 KST)

**Shawn에게 텔레그램 브리핑 전송:**
```
🔎 PLEDS 일일 브리핑 [날짜]

📊 Macro Regime: [Risk-On/Neutral/Risk-Off] (확률 X%)
🏭 유망 산업: [Top 3]
📈 투자 액션:
  - [종목] [BUY/SELL/HOLD] [사이즈%] [근거 1줄]
  - ...
⚠️ 리스크 알림: [있으면]
🔗 상세: [파일 링크]
```

---

## 주간 Full Debate (매주 일요일 10:00 KST)

### 추가 절차:
1. **주간 성과 리뷰** — 포트폴리오 수익률 vs 벤치마크
2. **전문가 적중률 업데이트** — 지난주 판정 vs 실제
3. **신규 테마 브레인스토밍** — Theme Hunter 주도
4. **포지션 재조정 토론** — 드리프트 체크
5. **다음 주 핵심 이벤트 프리뷰** — 어닝, FOMC, CPI 등

---

---

## Bottleneck Thesis Scan (제약 조건 테마 스캔)

### 목적
기존 투자 테마 또는 신규 메가트렌드를 **제약 조건 렌즈**로 분석하여 병목 소유자(Constraint Owner)를 식별하고 투자 기회를 발굴한다.

### 절차 (테마당 1회)

1. **테마 정의**: 확장 중인 메가트렌드 명확화 (예: "A2A 경제", "AI 에이전트 확산")
2. **Constraint Chain Mapping**: 
   - 해당 테마가 10x 확장되려면 거쳐야 하는 밸류체인 전체 매핑
   - 각 노드의 현재 capacity vs 필요 capacity 추정
   - **1차 병목** (지금 막고 있는 것) + **2차 병목** (1차 해소 시 다음) 식별
3. **Bottleneck Hunter 분석**:
   - 병목의 해소 난이도 (기술적/자본적/규제적)
   - 병목 지속 기간 추정
   - 역사적 유사 사례 비교 (HBM, 우라늄, 리튬 등)
4. **Constraint Owner 식별**:
   - 병목을 소유/통제하는 상장 기업 리스트
   - Constraint Premium 평가 (대체 불가능성 × 수요 탄력성)
5. **PLEDS Layer 4 연결**: 식별된 기업을 Company 전문가 토론에 투입
6. **Conviction Card 작성**: 식별된 Constraint Owner별 C1-C4 카드 작성
7. **산출물**: `debates/bottleneck-thesis-{YYYY-MM-DD}-{테마}.md` → GitHub push

### Tsunami 테마 재스캔 계획

기존 7개 Tsunami 테마를 제약 조건 렌즈로 순차 재스캔:

| # | 테마 | 핵심 질문 | 상태 |
|---|------|----------|------|
| 1 | AI Agent/A2A Economy | 결제 인프라 (CRCL) | ✅ 완료 2026-03-19 |
| 2 | Robotics | AI 범용 조작 SW (NVDA, TXN) | ✅ 완료 2026-03-19 |
| 3 | GLP-1 / Obesity | 펩타이드 API 제조 (Bachem, WST) | ✅ 완료 2026-03-19 |
| 4 | Nuclear Energy | HALEU 농축 (LEU) | ✅ 완료 2026-03-19 |
| 5 | Water Crisis | 에너지 회수 PX 독점 (ERII) | ✅ 완료 2026-03-19 |
| 6 | Demographic → Automation | SI 인력 부족 (ISRG, TER) | ✅ 완료 2026-03-19 |
| 7 | Synbio | 설계 지능 AI for Bio (TWST 조건부) | ✅ 완료 2026-03-19 |

→ 각 테마를 1개씩 서브에이전트로 실행, 결과를 GitHub에 아카이빙

---

## 이벤트 트리거 워크플로우 (수시)

| 트리거 | 대응 |
|--------|------|
| 보유 종목 ±5% 일일 변동 | Chart + Company 긴급 리뷰 |
| VIX 25+ 돌파 | Macro 긴급 Regime 재판정 |
| FOMC/CPI 발표 | Macro 즉시 업데이트 |
| 어닝 발표 (보유 종목) | Company + Chart 즉시 리뷰 |
| BTC ±10% 일일 변동 | Crypto 전문가 긴급 토론 |

---

## 파일럿 런 체크리스트 (내일 오전)

- [ ] 현재 포트폴리오 기준: BMNR 35%, CRCL 10%, COIN 5%, SGOV 30%, USD 20%
- [ ] Macro: 현 레짐 판정
- [ ] Sector: 크립토/핀테크/인프라 산업 평가
- [ ] Company: BMNR, CRCL, COIN 재평가 + 신규 후보
- [ ] Chart: BTC, ETH 파동 분석 + MVRV/도미넌스
- [ ] Synthesis: 포트폴리오 조정 제안
- [ ] 결과 텔레그램 전송
