# PLEDS 5대 헌법 감사 보고서

**Date**: 2026-03-26  
**Auditor**: Independent System Architect (Opus)

---

## Executive Summary

**전체 건강도: B+ (양호, 개선 필요)**

PLEDS 5대 헌법은 투자 시스템으로서 **이론적 완결성은 높으나, 복잡도가 "바닐라 원칙"을 위반**하고 있다. 

**핵심 발견 3개:**
1. **버전 불일치**: METHODOLOGY.md 내부에서 v3.1과 v4.0이 혼재하며, WORKFLOW.md는 v3.2로 별도 버전 — 동기화 실패
2. **바닐라 원칙 자기모순**: "모듈을 늘리지 않는다"를 명시하면서 11개 Phase + 5개 Layer + 5회 Deep Loop + 4 Round Debate = 시스템 복잡도 과다
3. **전문가 겹침 존재**: Regime Analyst와 Counter-Consensus Analyst가 일부 영역(사이클 판단)에서 중복 기능 수행

---

## 1. 일관성 감사

### 발견된 충돌/모순

#### 1-1. 버전 불일치 (Critical)

| 파일 | 명시된 버전 | 위치 |
|------|------------|------|
| METHODOLOGY.md | v3.1 (상단) | 문서 제목 |
| METHODOLOGY.md | v4.0 | §9 Conviction Card, §10 Deep Loop |
| WORKFLOW.md | v3.2 | 문서 상단 |
| EXPERTS.md | v3.1 | 문서 제목 |
| PORTFOLIO.md | 버전 없음 | — |
| DATA-SOURCES.md | v2.1 | 문서 상단 |

**충돌**: METHODOLOGY.md 내부에서 §9와 §10이 "v4.0 (2026-03-26)"으로 표기되어 있으나, 문서 상단은 여전히 "v3.1". 동일 문서 내 버전 불일치.

#### 1-2. METHODOLOGY 규칙 vs PORTFOLIO 현재 상태 (위반 인지됨)

**METHODOLOGY.md §12:**
> "단일 테마 MAX 40% (크립토 전체 = BMNR+CRCL)"

**PORTFOLIO.md:**
> "Crypto 45.5% > 40% 상한... METHODOLOGY §12 한도 초과"
> "Shawn 인지 하에 conviction override. 90일 후 리뷰 (2026-06-25)."

**판정**: 위반이지만 문서에서 인지+기록됨. 시스템의 자기 인식은 작동 중.

#### 1-3. Phase 순서 표기 혼란 (Minor)

**WORKFLOW.md:**
- Phase 4.5가 Phase 5 설명 **이후**에 나옴 (라인 순서상)
- "Phase 0 → 0.5 → 1 → 2 → 3 → 4 → **4.5** → 5 → 6 → 7 → 8"이라고 명시했으나, 실제 문서 순서는 Phase 5 → Phase 4.5

**인용:**
```
### Phase 5: Layer 5 — Chart & Timing (~15분)
[...]
### Phase 4.5: Technical Data Pipeline (~자동)
```

**문제**: 읽는 순서와 실행 순서 불일치로 혼란 유발.

### 용어 불일치

#### 1-4. "Critic" vs "전담 Critic" 혼용

- METHODOLOGY.md §10.5: "Critic 역할 배정" 테이블에서 Counter-Consensus Analyst를 Critic으로 표기
- EXPERTS.md: Counter-Consensus Analyst를 "⚔️ CRITIC"으로 표기하면서 **"v3.1: 전담 Critic 5명 체제"**라고 상단에 명시
- 그러나 Counter-Consensus Analyst는 "전담 Critic"이 아니라 Round 1에서 독립 뷰도 제시하는 **이중 역할**

**인용 (EXPERTS.md):**
> "**Round 1:** 현재 사이클 위치 판단 + 역발상 관점 제시"
> "**Round 2:** **L1 전담 Critic** — 모든 전문가 주장에 반론 (의무)"

**문제**: "전담 Critic"이라면 Round 1에서 독립 뷰 제시가 역할 외. 용어 정의 모호.

### 버전 불일치

위 1-1에서 상세 기술. 5개 문서의 버전이 v2.1 ~ v4.0까지 산재.

---

## 2. 필요성 감사

### Dead Code (삭제 가능한 섹션)

#### 2-1. METHODOLOGY.md §7 "Historical Analogy Engine" — 보존 권장

**사용 여부**: WORKFLOW.md Phase 4에서 "Historical Analogy Engine 4축 탐색 주도" 명시. 실제 사용됨.
**판정**: Dead Code 아님.

#### 2-2. WORKFLOW.md "Bottleneck Thesis Scan" 섹션 — **Dead Code 의심**

**인용:**
```
### Tsunami 테마 재스캔 계획
| # | 테마 | 핵심 질문 | 상태 |
|---|------|----------|------|
| 1 | AI Agent/A2A Economy | 결제 인프라 (CRCL) | ✅ 완료 2026-03-19 |
[...]
| 7 | Synbio | 설계 지능 AI for Bio (TWST 조건부) | ✅ 완료 2026-03-19 |
```

**문제**: 7개 테마 모두 "✅ 완료"로 표기. 이 섹션은 **히스토리 기록**이지 **실행 가능 절차**가 아님.
**권고**: "완료된 스캔 아카이브" 섹션으로 이동하거나 별도 파일(`archive/tsunami-scan-2026-03.md`)로 분리.

#### 2-3. DATA-SOURCES.md "우선 확보 요청 (Shawn)" 섹션 — **Dead Code**

**인용:**
```
### 🔴 필수 (매일 사용)
1. **FRED API Key** — ✅ 확보 완료

### 🟡 권장 (데이터 품질 향상)
2. **Alpha Vantage Key** — ✅ 확보 완료
3. **Twelve Data Key** — ✅ 확보 완료
```

**문제**: 3개 모두 "✅ 확보 완료". 이 섹션은 **완료된 태스크 리스트**. 
**삭제해도 영향 없는 이유**: 분석 결과에 영향을 주지 않음. API 키는 이미 환경변수에 설정됨.
**권고**: 삭제 또는 "API 키 히스토리" 아카이브로 이동.

#### 2-4. METHODOLOGY.md §3-4 "Reality Coherence Audit" — 사용되나 중복

**인용 (METHODOLOGY.md):**
> "**산출물:** `audit/YYYY-MM-reality-audit.md`"

**인용 (WORKFLOW.md 주간 전략 리뷰):**
> "**Phase B — 전략적 판단 (Reality Coherence Audit)**"
> "5. **예측 vs 실제 괴리** — 지난 7일 PLEDS 판정 vs 실제 시장 결과"

**문제**: METHODOLOGY에서 "월간"으로, WORKFLOW에서 "주간"으로 각각 정의. 동일 내용이 두 곳에 분산.
**권고**: METHODOLOGY에서 원칙만 정의, WORKFLOW에서 실행 주기 통합 관리.

### 과도 세분화

#### 2-5. Phase 0 vs Phase 0.5 — 통합 가능

**Phase 0**: 데이터 수집 (자동/크론)
**Phase 0.5**: Data Integrity Audit (Data Auditor)

**문제**: Phase 0.5는 Phase 0의 산출물을 검증하는 것. 별도 Phase로 분리할 필요성 낮음.
**권고**: "Phase 0: 데이터 수집 + 검증"으로 통합. Data Auditor가 Phase 0 내에서 작동.

#### 2-6. Phase 7 중복 기재

**WORKFLOW.md에서 Phase 7이 두 번 나옴:**
1. 첫 번째 (Phase 6 다음): 브리핑 전송 설명
2. 두 번째 (Phase 8.5 이후): 동일한 내용 반복

**인용 (두 번째 Phase 7):**
```
### Phase 7: Delivery (~09:00 KST)

**Shawn에게 텔레그램 브리핑 전송:**
```

**문제**: 완전 중복. 복붙 오류로 추정.
**권고**: 두 번째 Phase 7 삭제.

---

## 3. 직교성 감사

### 전문가 겹침 분석

**18명 전문가 매트릭스 분석:**

#### 겹침 높은 쌍

| 쌍 | 겹침 영역 | 겹침 정도 | 판정 |
|----|----------|----------|------|
| **Regime Analyst ↔ Counter-Consensus Analyst** | 사이클 판단 | 🟡 중간 | 분리 유지 권장 |
| **Opportunity Scanner ↔ Sector Skeptic** | 산업 전망 (정반) | 🟢 낮음 (의도적 대립) | OK |
| **Moat Analyst ↔ Moat Breaker** | 해자 분석 (정반) | 🟢 낮음 (의도적 대립) | OK |
| **Company Analyst ↔ Forensic Accountant** | 기업 분석 (Bull/Bear) | 🟢 낮음 (의도적 대립) | OK |
| **Technical Analyst ↔ Signal Skeptic** | 시그널 해석 (정반) | 🟢 낮음 (의도적 대립) | OK |

**Regime Analyst ↔ Counter-Consensus Analyst 상세:**

**EXPERTS.md 인용:**

Regime Analyst:
> "**프레임워크:** Dalio 관점: 장기 부채 사이클... / Druckenmiller 관점: 연준 유동성"

Counter-Consensus Analyst:
> "**프레임워크:** 시장 온도계 (1-10, 1=공포 10=탐욕) / 재귀성 이론, 시장 컨센서스의 취약점 탐색"

**겹침**: 둘 다 "사이클 위치"를 판단함.
- Regime Analyst: "현재 레짐 (Early Cycle / Mid Cycle / Late Cycle / Recession)"
- Counter-Consensus Analyst: "시장 온도계 (1-10)"

**차이점**: 관점은 다름 (구조적 vs 심리적). 그러나 최종 질문 "지금 사이클 어디인가?"에 둘 다 답함.

**권고**: 
- 유지하되 역할 경계 명확화
- Counter-Consensus는 **"Critic으로서의 반론"**에 집중 (Round 1 독립 뷰 제한)
- 또는 v4에서 Counter-Consensus의 Round 1 역할을 Regime Analyst에 흡수

### 빠진 관점

| 영역 | 현재 담당자 | 커버리지 |
|------|------------|---------|
| **ESG/지속가능성** | 없음 | ❌ 빠짐 |
| **지정학적 리스크** | Regime Analyst (부분) | ⚠️ 약함 |
| **소비자/리테일 관점** | Company Analyst (부분) | ⚠️ 약함 |
| **법률/소송 리스크** | Forensic Accountant (부분) | ⚠️ 약함 |

**ESG 부재 영향**: ERII(Water) 같은 종목 분석 시 ESG 프리미엄/할인 관점이 구조적으로 빠짐.

**권고**: 
- 별도 ESG 전문가 추가보다 **Moat Analyst의 분석 체크리스트**에 "ESG 리스크/기회" 항목 추가 (바닐라 원칙 준수)

### 최적 전문가 수 권고

**현재**: 18명 (11 전문가 + 5 Moderator + 5 Critic 역할, 일부 겸임)

| 레벨 | 현재 | 권고 | 근거 |
|------|------|------|------|
| L1 Macro | 3 (2+1mod) | 2 (1+1mod) | Counter-Consensus를 Critic 전념으로 전환 |
| L2 Sector | 3 | 3 | 유지 |
| L3 Value Chain | 3 | 3 | 유지 |
| L4 Company | 3 | 3 | 유지 |
| L5 Technical | 3 | 2 | Signal Skeptic 역할을 Technical Moderator에 부분 흡수 |
| Cross-Layer | 1 | 1 | 유지 |
| Synthesis | 1 | 1 | 유지 |
| Data | 1 | 1 | 유지 |
| **합계** | **18** | **16** | -2명 |

**Critic 5명 차별화 분석:**

| Critic | 고유 공격 벡터 | 차별화 수준 |
|--------|--------------|------------|
| Counter-Consensus Analyst | 사이클/재귀성 | 🟢 명확 |
| Sector Skeptic | 버블 패턴/TAM 과대추정 | 🟢 명확 |
| Moat Breaker | AI Commoditization/파괴적 혁신 | 🟢 명확 |
| Forensic Accountant | 회계 부정/부채 구조 | 🟢 명확 |
| Signal Skeptic | 백테스트 과적합/noise vs signal | 🟢 명확 |

**결론**: 5명 Critic의 공격 벡터는 잘 차별화되어 있음.

---

## 4. 복잡도 감사

### 바닐라 원칙 위반 사례

**METHODOLOGY.md §2 "바닐라 원칙" 인용:**
> "1. **모듈을 늘리지 않는다** — 새 인사이트가 생기면 기존 모듈을 업그레이드하지, 새 모듈을 만들지 않는다. 복잡도는 적이다."

**현재 시스템 모듈 수:**
- Phase: 11개 (0, 0.5, 1, 2, 3, 4, 4.5, 5, 6, 7, 8, 8.5 — 실제로는 12개)
- Layer: 5개 + Cross-Layer + Synthesis = 7개
- 전문가: 18명
- Debate Round: 4회
- Deep Loop: 최대 5회
- Edge Test: 4문항
- Cross-Domain Comparison: 5축
- Kill Condition 항목: 다수
- Conviction Card: 5장 (C0~C4)
- 트리거 조건: E1~E7

**바닐라 원칙 위반 증거:**

1. **§9 "Conviction Card"가 v4.0에서 C0 추가** — "기존 모듈 업그레이드"가 아니라 "새 카드 추가"
2. **§10 "Deep Loop"가 v4.0에서 Outer Loop 추가** — 새 루프 구조 신설
3. **§10.3 "Cross-Domain Creative Comparison"이 v4.0에서 신설** — 5축 비교 엔진 추가

**인용 (METHODOLOGY.md §10):**
> "**v4.0 (2026-03-26)**: '절차 완료'가 아니라 **'통찰 발견'**이 토론 종료 조건이다."

**문제**: v4.0 업데이트가 "바닐라 원칙"과 직접 충돌. 모듈(C0, Outer Loop, X1~X5 비교축)이 추가됨.

### 삭제 가능한 규칙 목록

"이 규칙을 빼면 분석 품질이 떨어지는가?" → **NO**인 목록:

| 규칙 | 위치 | 삭제 영향 | 권고 |
|------|------|----------|------|
| Cross-Domain 5축 중 X4(인재 경쟁) | METHODOLOGY §10.3 | 낮음 — 현재 포트폴리오에 인재 경쟁이 핵심인 종목 없음 | 선택적 적용으로 변경 |
| Phase 8.5 Decision Recording | WORKFLOW.md | 중간 — PT Recording(Phase 8)과 기능 중복 | Phase 8에 통합 |
| "100x Shawn" 섹션 | WORKFLOW.md | 낮음 — ICL이 같은 역할 수행 | ICL로 통합 |
| Tsunami 테마 재스캔 표 | WORKFLOW.md | 없음 — 이미 완료됨 | 아카이브로 이동 |

### 복잡도 점수 (1-10, 10=과도)

**점수: 7.5/10 — 과도 경계**

| 측면 | 점수 | 근거 |
|------|------|------|
| Phase 수 | 8/10 | 11~12개 Phase는 과다 |
| Layer 수 | 5/10 | 5개 Layer는 적절 |
| 전문가 수 | 6/10 | 18명은 약간 과다 |
| Loop/Round | 8/10 | 5회 Loop × 4 Round = 최대 20회 iteration은 과다 |
| 문서 길이 | 8/10 | METHODOLOGY만 ~600줄, 5개 문서 총 ~2000줄 |
| 조건 분기 | 7/10 | Standard Day vs Event Day, 7개 트리거 등 분기 과다 |

**문서 총 길이 대비 핵심 내용 비율 추정:**
- METHODOLOGY.md: ~60% 핵심, ~40% 예시/설명
- WORKFLOW.md: ~50% 핵심, ~30% 반복, ~20% 완료된 태스크
- EXPERTS.md: ~70% 핵심, ~30% 히스토리 매핑
- PORTFOLIO.md: ~90% 핵심
- DATA-SOURCES.md: ~60% 핵심, ~40% 완료된 키 확보 기록

---

## 5. 실행 가능성 감사

### 모호한 지시 Top 5

#### #1. Edge Test "E1 Novelty" 판정 기준 (Critical)

**METHODOLOGY.md §10.2 인용:**
> "**E1 Novelty** | 이 인사이트가 sell-side 컨센서스에 없는가? | 주요 애널리스트 보고서에서 언급되지 않은 관점"

**문제**: 
- "주요 애널리스트"의 정의가 없음. Top 5? 커버하는 모든 애널리스트?
- "보고서"의 범위가 없음. 최근 30일? 1년? 전체?
- 소형주(BMNR, ERII)는 sell-side 커버리지 자체가 없음 — 자동 E1 통과?

**서브에이전트 혼란 예상**: 높음

#### #2. "살아남은 논거" 정의 (High)

**WORKFLOW.md 다수 위치:**
> "Moderator가 **살아남은 논거만** 정리"

**문제**: "살아남았다"의 기준이 없음.
- Critic이 반론했으나 defend 성공하면 살아남은 것인가?
- revise된 논거는 "살아남은" 것인가, 새로운 논거인가?
- abandon된 논거만 제외인가?

**서브에이전트 혼란 예상**: 중간

#### #3. Edge Score 0-10 산출 기준 주관성 (High)

**METHODOLOGY.md §9 인용:**
> "**8-10** | Strong Edge | Deep Loop Edge Test 4/4 통과 + 컨센서스와 방향 반대 + 인과 메커니즘 명확"

**문제**: 
- "인과 메커니즘 명확"이 주관적
- 4/4 통과 vs 3/4 통과의 점수 차이가 명시되지 않음 (5-7 범위가 "3/4 이상"으로 모호)

**서브에이전트 혼란 예상**: 중간

#### #4. Standard Day vs Event Day 판정 우선순위 (Medium)

**WORKFLOW.md 인용:**
> "| E2 | 보유종목 ±5% 일일 변동 | 전일 종가 기준 | Yahoo v8 |"
> "| E6 | BTC ±10% 일일 변동 | 전일 기준 | CoinGecko |"

**문제**: BMNR이 +6% 움직이고 BTC가 +8% 움직이면?
- E2 트리거 (BMNR ±5%)
- E6 미달 (BTC ±10% 아님)
- 결론: Event Day

그러나 BMNR의 6% 움직임이 **BTC 8% 움직임 때문**이면, 실질적으로 동일 이벤트를 두 번 처리하게 됨.

**서브에이전트 혼란 예상**: 낮음 (트리거 중복은 큰 문제 아님)

#### #5. "3가지 이상" 시나리오 의무 — 최소인가 권장인가? (Medium)

**EXPERTS.md Forensic Accountant 인용:**
> "**'이 기업을 죽이는 시나리오' 3가지 이상** 제시 의무"

**문제**: 
- 3가지가 최소인가, 3~5가 적정 범위인가?
- 10가지 제시하면 과잉인가?
- 작은 기업(BMNR 같은 단순 구조)도 3가지 필수인가?

**서브에이전트 혼란 예상**: 낮음

### 순환 참조

**발견된 순환 없음.** 

문서 간 참조가 단방향:
- METHODOLOGY → 원칙 정의
- WORKFLOW → METHODOLOGY 참조 + 실행 절차
- EXPERTS → METHODOLOGY의 역할 구현
- PORTFOLIO → 현재 상태 (METHODOLOGY 규칙 적용 결과)
- DATA-SOURCES → METHODOLOGY §3 구현

### 처음 읽는 에이전트 혼란 포인트 Top 5

#### #1. "어디서부터 읽어야 하는가?" (Critical)

**문제**: 5개 문서의 읽기 순서가 명시되지 않음.
- METHODOLOGY 먼저? WORKFLOW 먼저?
- 일일 브리핑 수행 시 5개 문서를 모두 읽어야 하는가?

**권고**: `README.md` 또는 `INDEX.md` 생성. 문서 목적과 읽기 순서 명시.

#### #2. v3.1 vs v4.0 — 어느 것이 현재 유효한가? (High)

**문제**: METHODOLOGY.md 내에서 "v4.0 신설"이라고 표기된 섹션이 있으나, 전체 문서가 v4.0으로 업그레이드되었는지 불명확.

**서브에이전트 질문 예상**: "§9 C0 Thesis는 v4.0인데, §8 Management Will Tracker는 무슨 버전인가?"

#### #3. Phase 4.5 위치 (Medium)

**문제**: 위 1-3에서 기술. Phase 5 다음에 Phase 4.5가 나옴.

**서브에이전트 질문 예상**: "Phase 4.5를 Phase 4 다음에 실행하는 건가, Phase 5 다음에 실행하는 건가?"

#### #4. Critic 이중 역할 (Counter-Consensus) (Medium)

**문제**: Counter-Consensus Analyst가 Round 1에서 독립 뷰를 제시하고 Round 2에서 Critic 역할도 수행.

**서브에이전트 질문 예상**: "Counter-Consensus가 Round 1에서 제시한 뷰를 Round 2에서 스스로 반론하는가?"

#### #5. "100배 똑똑한 Shawn" vs ICL (Medium)

**WORKFLOW.md:**
> "9. **'100배 똑똑한 Shawn이라면?' 섹션**"

**METHODOLOGY.md §14.3:**
> "**'100배 똑똑한 Shawn' 섹션 캘리브레이션**... ICL 반영"

**문제**: 두 개념의 관계가 명확하지 않음. 같은 것인가, 다른 것인가?

---

## 6. 종합 권고사항

### 즉시 수정 (Quick Wins)

| # | 항목 | 파일 | 예상 시간 |
|---|------|------|----------|
| 1 | **버전 통일** — 전체 문서를 v4.0으로 명시, 변경 이력 섹션 추가 | ALL | 30분 |
| 2 | **Phase 7 중복 삭제** — WORKFLOW.md 하단의 두 번째 Phase 7 제거 | WORKFLOW.md | 5분 |
| 3 | **Phase 4.5 위치 이동** — Phase 4 바로 다음으로 이동 | WORKFLOW.md | 10분 |
| 4 | **완료된 태스크 아카이브** — Tsunami 테마 표, API 키 확보 목록 제거/이동 | WORKFLOW.md, DATA-SOURCES.md | 15분 |
| 5 | **INDEX.md 생성** — 5개 문서 목적, 읽기 순서, 관계 명시 | 신규 | 20분 |

### 구조적 개선 (Refactoring)

| # | 항목 | 영향 | 우선순위 |
|---|------|------|----------|
| 1 | **Phase 0 + 0.5 통합** — 데이터 수집과 검증을 단일 Phase로 | 복잡도 감소 | 🟡 중간 |
| 2 | **Counter-Consensus Round 1 역할 명확화** — Critic 전념 or 독립 뷰 분리 | 직교성 개선 | 🟡 중간 |
| 3 | **Edge Score 산출 공식 명시화** — E1~E4 통과 수 → 점수 매핑 테이블 | 실행 가능성 | 🟢 높음 |
| 4 | **"살아남은 논거" 정의 추가** — Round 3 결과별 상태 명시 | 실행 가능성 | 🟢 높음 |
| 5 | **바닐라 원칙 실제 적용** — 분기 1회 "모듈 수 감사" 절차 추가 | 자기 정합성 | 🟡 중간 |

### 유지 (잘 되고 있는 것)

| # | 항목 | 근거 |
|---|------|------|
| 1 | **Critic 5명 차별화** | 각 Critic의 공격 벡터가 명확히 구분됨 |
| 2 | **Information Source Tier 체계** | Tier 1~4 분류가 명확하고 실용적 |
| 3 | **Kill Condition 명시** | PORTFOLIO.md에 종목별 Kill 조건이 구체적 |
| 4 | **Price Drop Triage 3가설 프레임워크** | A/B/C 가설 구조가 실행 가능하고 유용 |
| 5 | **2-Track Daily Mode** | Standard/Event 분기로 토큰 효율성 확보 |
| 6 | **Conviction Card 구조** | C0~C4 체계가 투자 의사결정에 필수 요소를 커버 |
| 7 | **User Input Validation (§3-2)** | "Shawn의 말도 팩트가 아니다. 검증한다" — 건강한 원칙 |
| 8 | **ICL Anti-Sycophancy** | "동조 도구가 아닌 캘리브레이션 도구" — 시스템 철학 명확 |

---

## Appendix: 토큰 효율성 추정

| 문서 | 추정 토큰 | 핵심 비율 | 정리 후 추정 |
|------|----------|----------|-------------|
| METHODOLOGY.md | ~8,000 | 60% | ~5,500 |
| WORKFLOW.md | ~6,000 | 50% | ~4,000 |
| EXPERTS.md | ~4,500 | 70% | ~3,500 |
| PORTFOLIO.md | ~1,200 | 90% | ~1,100 |
| DATA-SOURCES.md | ~2,000 | 60% | ~1,400 |
| **합계** | **~21,700** | — | **~15,500** |

**정리 시 ~30% 토큰 절감 가능** (6,200 토큰)

---

*End of Audit Report*
