# PLEDS Workflow — Step by Step

> v2: Adversarial Debate Protocol 적용

---

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

**Data Source Health Check (METHODOLOGY §3-1 연동):**
- 각 데이터 소스 응답 정상 여부 확인
- 장애 발견 시 `[DATA SOURCE ALERT]` 발행 + 대체 소스 전환
- 데이터 최신일 확인 (1영업일 이상 지연 시 경고)

### Phase 0.5: Data Integrity Audit

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

**Critic 담당:** Contrarian Catalyst (기존 역할 확장)

**Adversarial Debate 절차:**

1. **Round 1 — 독립 제시**
   - 각 전문가가 1-2문장으로 현재 뷰 제시 (독립적, 다른 전문가 뷰 모름)
   - The Machine: 현재 레짐 판정
   - The Liquidity Hawk: 유동성 방향
   - The Cycle Sentinel: 시장 온도
   - Bottleneck Hunter: 매크로 병목

2. **Round 2 — Critic 반론**
   - **Contrarian Catalyst**가 각 전문가의 주장에 대해 구체적 반론 제시 (의무)
   - "모두가 동의하면 틀렸다" — 컨센서스의 취약점 공격
   - 각 주장에 대해 최소 1개 반론 의무

3. **Round 3 — 재반박/수정**
   - 각 전문가가 Critic의 반론에 대응:
     - **defend**: 추가 근거로 본인 관점 구체화
     - **revise**: 반론을 수용하여 수정
     - **abandon**: 논거 폐기
   - "defend 실패 시 반드시 revise 또는 abandon"

4. **Round 4 — Moderator 수렴**
   - Macro Moderator가 살아남은 논거만 정리
   - 핵심 분기점(fork) 식별
   - 투표 주재

5. **투표:** Regime (Risk-On / Neutral / Risk-Off) + 확률 %

**산출물:** `layers/L1-macro/regime-tracker.md` 업데이트

---

### Phase 2: Layer 2 — Sector Scan (~10분)

**참여:** The Disruptor, The Value Mapper, The Theme Hunter, **The Bottleneck Hunter (Cross-Layer)**, Sector Moderator

**Critic 담당:** Sector Moderator (겸임)

**Adversarial Debate 절차:**

1. **Round 1 — 독립 제시**
   - Macro regime을 전달받고 산업 영향 분석
   - 각 전문가가 유망/역풍 산업 3개씩 제시
   - Theme Hunter: 비컨센서스 테마 1개 이상 의무 발굴

2. **Round 2 — Critic 반론**
   - **Sector Moderator**가 각 전문가의 산업 선택에 대해 반론 제시 (의무)
   - "왜 이 산업이 아니라 저 산업인가?" 도전
   - 매크로 Layer와의 정합성 검증

3. **Round 3 — 재반박/수정**
   - 각 전문가가 defend / revise / abandon 선택
   - 비컨센서스 테마는 특히 강하게 검증

4. **Round 4 — Moderator 수렴**
   - 살아남은 산업 뷰만 정리
   - 핵심 분기점 식별
   - 투표 주재

5. **투표:** 산업 매력도 Top 5 + 회피 산업

**산출물:** `layers/L2-sector/sector-rankings.md` 업데이트

---

### Phase 3: Layer 3 — Value Chain Analysis (~10분)

**참여:** The Strategist, The Network Thinker, **The Bottleneck Hunter (Cross-Layer, 주도적 역할)**, Value Chain Moderator

**Critic 담당:** Value Chain Moderator (겸임)

**Adversarial Debate 절차:**

1. **Round 1 — 독립 제시**
   - Phase 2에서 선정된 유망 산업의 밸류체인 매핑
   - 가치 집중 노드 식별 (곡괭이, 플랫폼, 톨게이트)
   - **[의무] Causal Mechanism Map 작성**
     - 분석 대상 기업의 매출 인과사슬을 명시적으로 그린다
     - 형식: `[투입] → [프로세스] → [핵심 노드] → [산출] → [최종 가치]`
     - 치명적 약점 + 대안 경로 식별

2. **Round 2 — Critic 반론**
   - **Value Chain Moderator**가 각 전문가의 노드 선택에 대해 반론
   - "이 노드가 정말 가치를 포착하는가?" 도전
   - AI Commoditization Filter 적용: "이 해자가 AI로 대체 가능한가?"

3. **Round 3 — 재반박/수정**
   - 각 전문가가 defend / revise / abandon 선택
   - Causal Mechanism Map의 약점 보완

4. **Round 4 — Moderator 수렴**
   - 살아남은 노드만 정리
   - 밸류체인 내 최적 투자 포지션 합의

5. **투표:** 산업별 밸류체인 맵 + 최적 투자 노드

**산출물:** `layers/L3-valuechain/frameworks.md` 업데이트

---

### Phase 4: Layer 4 — Company Deep Dive (~20분)

**참여:** The Compounder, The Catalyst Hunter, **The Forensic Accountant (전담 Critic)**, **The Bottleneck Hunter (Cross-Layer)**, Company Moderator

**Critic 담당:** Forensic Accountant (전담 — 역할 강화)

**Adversarial Debate 절차:**

1. **Round 1 — 독립 제시**
   - 워치리스트 + 현재 보유 종목 리뷰
   - 신규 종목 후보 검토 (Phase 2-3에서 도출)
   - **[의무] Management Will Tracker 평가**
     - 각 전문가가 경영진 의지 평가 포함
     - Insider Transactions, Capital Allocation, Guidance Behavior 등 추적
     - 🟢 Aligned / 🟡 Neutral / 🔴 Misaligned 판정

2. **Historical Analogy Engine (Round 1 후, Round 2 전)**
   - 4축 탐색 의무:
     1. **밸류에이션 유비**: P/S Xx에서 성장률 Y%인 동종이 3년 후 어디 갔나?
     2. **전환기 유비**: CEO 교체/턴어라운드 성공/실패 사례는?
     3. **산업 유비**: 독점 인프라가 경쟁에 무너진/버틴 사례는?
     4. **매크로 유비**: 유사 매크로 환경에서 이 섹터/종목은?
   - 유비의 한계(차이점) 3개 이상 명시 의무
   - `[THESIS]` 태그로 표기

3. **Round 2 — Critic 반론 (Forensic Accountant 전담)**
   - **Forensic Accountant**가 모든 매수 후보에 대해 **Bear Case 의무 제시**
   - "이 기업을 죽이는 시나리오" **3가지 이상** 제시 의무
   - 회계 적자 신호, 부채 구조, 내부자 행동 분석
   - "숫자가 이야기와 맞지 않을 때" 집중 공격
   - Historical Analogy의 한계 지적

4. **Round 3 — 재반박/수정**
   - Compounder, Catalyst Hunter가 Forensic Accountant의 반론에 대응
   - defend / revise / abandon 선택
   - Bear Case를 반박 못하면 확신도 자동 하향

5. **Round 4 — Moderator 수렴**
   - Company Moderator가 살아남은 논거만 정리
   - Bull/Bear 균형 검증
   - 핵심 모니터링 변수 식별
   - 투표 주재

6. **투표:** 종목별 확신도 (1-10) + 적정가 + 액션

**산출물:** `layers/L4-company/watchlist.md` + `active-positions.md` 업데이트

---

### Phase 5: Layer 5 — Chart & Timing (~15분)

**참여:** The Quant Dashboard, The Time Series Analyst, The Structure Reader, Chart Moderator

**Critic 담당:** Technical Moderator (겸임)

**Adversarial Debate 절차:**

1. **Round 1 — 독립 제시**
   - Phase 4 통과 종목의 차트 분석
   - Quant Dashboard: 정량 지표 팩트 제시 (RSI, MACD, BB, EMA, ADX 등)
   - Time Series Analyst: 시계열 추세 분석 (다이버전스, BB Squeeze 등)
   - Structure Reader: 구조적 위치 판독
   - 크립토: BTC, ETH 파동 카운트 + MVRV/도미넌스 분석

2. **Round 2 — Critic 반론**
   - **Technical Moderator**가 각 기술적 뷰에 대해 반론
   - "이 시그널이 페이크인 경우는?" 도전
   - L1-L4와의 정합성 검증

3. **Round 3 — 재반박/수정**
   - 각 전문가가 defend / revise / abandon 선택
   - 상충하는 시그널 해결

4. **Round 4 — Moderator 수렴**
   - 살아남은 기술적 판단만 정리
   - 진입/청산 타이밍 합의
   - 투표 주재

5. **투표:** 기술적 등급 + 진입 구간 + 손절 라인

**산출물:** `layers/L5-chart/signals.md` 업데이트

---

### Phase 4.5: Technical Data Pipeline (~자동)

**절차:**
1. `bash data/collect-indicators.sh` — Twelve Data에서 OHLCV + RSI/MACD/BB/ADX 수집
2. `python3 data/generate-dashboard.py` — 시계열 분석 + TECHNICAL-DASHBOARD.md 생성
3. 대시보드의 기계적 등급(🟢/🟡/🔴/⚪)을 Phase 6 Allocator에게 전달

**원칙:**
- 대시보드는 팩트(숫자+기계적 판정)만 제공. LLM TA 의견 금지.
- 시계열 데이터는 `data/` 디렉토리에 일 1회 누적 적재.
- L5는 L1-L4를 override하지 않음 — 타이밍 보조 역할.

---

### Phase 6: Synthesis — Conviction Convergence (~15분)

**참여:** The Allocator (수석 투자 책임자)

**원칙:** Phase 1-5의 Adversarial Debate 결과를 읽고, **살아남은 논거만** 기반으로 Conviction Card (C1-C4)로 수렴한다.

**절차:**

1. **5개 Layer + Cross-Layer(Bottleneck Hunter) 결과 종합**
   - 각 Layer에서 "살아남은 논거" 확인
   - Round 3에서 abandon된 논거는 제외

2. **확률 가중 계산** (METHODOLOGY.md 공식)

3. **Price Drop Triage 적용 (해당 종목)**
   - 보유종목 중 -10%+ 하락 종목 식별
   - 3가지 가설 동등 분량 검증:
     - A. 시장 실수 (Mr. Market)
     - B. 펀더멘탈 훼손 (Thesis Break)
     - C. 정보 비대칭 (Information Gap)
   - 각 가설에 최소 2개 근거 제시 의무
   - 가장 높은 확률의 가설에 따라 행동 결정

4. **모든 종목/테마에 Conviction Card 작성:**
   - C1 🔥 Burn? — 태울 만한가? (⭐~⭐⭐⭐ + 비대칭 배율)
   - C2 🚪 Entry — 진입 조건 (가격, 시점, 이벤트)
   - C3 🎯 Exit — 목표가/익절 (시간축별)
   - C4 ☠️ Kill — 가설 폐기/손절 조건 (기계적 실행)

5. **기존 보유 종목 C2/C3/C4 조건 달성 여부 체크** (Pre-Commitment Trigger)

6. **포지션 사이징 결정**

7. **Conviction Journal 업데이트 지시**
   - `conviction/` 폴더에 해당 종목 Journal 업데이트
   - Entry Thesis 변화 여부, Delta 기록
   - **"이 기업에 인생을 걸 수 있는가?"** 수준의 conviction 에센스 추출

8. **'100배 똑똑한 Shawn이라면?' 섹션**

**산출물:**
- `synthesis/action-list.md` — 오늘의 투자 액션 + Conviction Cards
- `synthesis/conviction-cards.md` — 전 종목 카드 누적 관리
- `daily/YYYY-MM-DD.md` — 일일 브리핑 전문
- `conviction/*.md` — 종목별 Conviction Journal 업데이트

---

### Phase 7: Delivery (~09:00 KST)

**Shawn에게 텔레그램 브리핑 전송:**
```
🔎 PLEDS 일일 브리핑 [날짜]

📊 Macro Regime: [Risk-On/Neutral/Risk-Off] (확률 X%)
🏭 유망 산업: [Top 3]
📈 투자 액션:
  - [종목] [BUY/SELL/HOLD] [사이즈%] [근거 1줄]
  - ...
⚠️ Price Drop Triage: [해당 종목 있으면]
⚠️ 리스크 알림: [있으면]
🔗 상세: [파일 링크]
```

---

### Phase 8: PT Recording (Prospective Tracking 기록)

> PLEDS의 모든 판단은 PT 시스템에 기록된다. 이 단계를 건너뛸 수 없다.

**절차:**
1. `tracking/judgments/YYYY-MM-DD-TICKER.md` 생성
   - 인풋 (Shawn 요청/맥락)
   - 판단 시점 데이터 스냅샷 (주가, VIX, Regime)
   - 각 Layer 판단 + Critic 결과 (survive/revise/abandon)
   - Conviction Card (C1-C4)
   - 최종 Action
2. Checkpoint 날짜 설정 (판단일 +30d/+90d/+180d/+1yr)
3. `tracking/accuracy.md` 판정 기록 테이블에 행 추가
4. git commit + push

**주간 리뷰 (일요일)에 PT 추가 작업:**
- 전 judgment의 현재 주가 수집
- Kill Condition / Catalyst 발생 체크
- Checkpoint 도래한 건 리뷰 작성 → `tracking/reviews/`
- accuracy.md 업데이트

**분기 리뷰에 PT 추가 작업:**
- Feedback Signal Report 생성 → `tracking/signals/`
- 방향 적중률, Layer별 기여도, Critic 효과, 시간축 정확도 분석
- Shawn과 협의 → METHODOLOGY.md 개선 반영

---

### 운영 규칙 (전 Phase 공통)

1. **포트폴리오 변경 권한**: PLEDS는 제안만 함. Shawn이 명시적으로 변경을 말하지 않는 한 기존 배분 유지. PORTFOLIO.md 수정은 Shawn 지시 시에만.

2. **동조 금지**: Shawn의 테시스에 무조건 동조하지 않음. 전문가들은 독립적으로 반론/지지 제시.

3. **"100x Shawn" 프레임**: 매 브리핑 말미에 "100배 똑똑한 Shawn이라면?" 섹션 포함. 동일한 리스크 성향 + 시드 극대화 목표를 가진 최적 의사결정자의 관점.

4. **블랙스완 워치**: 보유 종목의 existential risk (회사가 깨지는가?)를 매일 모니터링. 경고 시 즉시 알림.

5. **GitHub 아카이빙**: 모든 일일 브리핑, 데이터 검증, 포트폴리오 변경을 git commit + push.

6. **Adversarial Debate 기록**: 각 Phase의 Round 2 반론 + Round 3 대응을 명시적으로 기록. "어떤 논거가 살아남았는가"를 추적 가능하게.

---

### Phase 7: Delivery (~09:00 KST)

**Shawn에게 텔레그램 브리핑 전송:**
```
🔎 PLEDS 일일 브리핑 [날짜]

📊 Macro Regime: [Risk-On/Neutral/Risk-Off] (확률 X%)
🏭 유망 산업: [Top 3]
📈 투자 액션:
  - [종목] [BUY/SELL/HOLD] [사이즈%] [근거 1줄]
  - ...
⚠️ Price Drop Triage: [해당 종목 있으면]
⚠️ 리스크 알림: [있으면]
🔗 상세: [파일 링크]
```

---

## 주간 Full Debate (매주 일요일 10:00 KST)

### 추가 절차:
1. **주간 성과 리뷰** — 포트폴리오 수익률 vs 벤치마크
2. **전문가 적중률 업데이트** — 지난주 판정 vs 실제
3. **Adversarial Debate 회고** — 어떤 논거가 살아남았고, 어떤 것이 폐기되었나
4. **신규 테마 브레인스토밍** — Theme Hunter 주도
5. **포지션 재조정 토론** — 드리프트 체크
6. **Conviction Journal 종합 리뷰** — 각 종목의 conviction 변화 추적
7. **다음 주 핵심 이벤트 프리뷰** — 어닝, FOMC, CPI 등

### Reality Coherence Audit (METHODOLOGY §3-3 연동)
8. **예측 vs 실제 괴리** — 지난 7일 PLEDS 판정 vs 실제 시장 결과
9. **Stale Thesis Detection** — 30일+ 업데이트 없는 conviction 플래그
10. **Echo Chamber Check** — 최근 분석의 Bull/Bear 비율 점검 (80/20+ 시 경고)
11. **Model Drift** — 밸류에이션 모델 전제 vs 현실 괴리 체크

**산출물:** `audit/YYYY-WW-weekly-audit.md`

---

## 월간 Deep Review (매월 첫째 일요일)

### Reality Coherence Audit — 월간 항목
1. **30일 예측 적중률 계산** — 방향 적중률 60% 미만 시 시스템 재검토 트리거
2. **Blind Spot Scan** — "우리가 보지 못하고 있는 리스크는?" (의무 실행)
3. **데이터 인프라 감사** — 모든 소스 정상 작동 여부, Rate limit 상태
4. **Information Source 리뷰** — 새로운 Tier 1-2 소스 발굴, 기존 소스 품질 평가

**산출물:** `audit/YYYY-MM-reality-audit.md`

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

5. **Causal Mechanism Map 작성**:
   - 각 Constraint Owner의 매출 인과사슬 도식화
   - 치명적 약점 + 대안 경로 식별

6. **Historical Analogy Engine 적용**:
   - 4축 탐색으로 유사 사례 비교
   - 유비의 한계 명시

7. **PLEDS Layer 4 연결**: 식별된 기업을 Company 전문가 토론에 투입

8. **Conviction Card 작성**: 식별된 Constraint Owner별 C1-C4 카드 작성

9. **산출물**: `debates/bottleneck-thesis-{YYYY-MM-DD}-{테마}.md` → GitHub push

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
| **보유 종목 -10%+ 하락** | **Price Drop Triage 발동** |
| VIX 25+ 돌파 | Macro 긴급 Regime 재판정 |
| FOMC/CPI 발표 | Macro 즉시 업데이트 |
| 어닝 발표 (보유 종목) | Company + Chart 즉시 리뷰 |
| BTC ±10% 일일 변동 | Crypto 전문가 긴급 토론 |
| C4 Kill 조건 충족 | 48시간 내 기계적 실행 |

---

## 파일럿 런 체크리스트

- [ ] 현재 포트폴리오 기준: BMNR 35%, CRCL 10%, COIN 5%, ERII 10%, SGOV 20%, USD 20%
- [ ] Macro: 현 레짐 판정 (Adversarial Debate)
- [ ] Sector: 유망 산업 평가 (Adversarial Debate)
- [ ] Value Chain: Causal Mechanism Map 작성
- [ ] Company: Management Will Tracker + Historical Analogy Engine 적용
- [ ] Chart: 기술적 타이밍
- [ ] Synthesis: Price Drop Triage (해당 시) + Conviction Card + Conviction Journal 업데이트
- [ ] 결과 텔레그램 전송
