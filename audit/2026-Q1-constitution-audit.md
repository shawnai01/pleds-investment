# PLEDS Constitutional Audit — 2026 Q1

> 감사일: 2026-03-26
> 감사 기준: `audit/AUDIT-PROTOCOL.md` 5축 프레임워크
> 대상: METHODOLOGY v4.1, WORKFLOW v4.1, EXPERTS v4.1, PORTFOLIO, DATA-SOURCES v4.1
> **종합 등급: C+ (개선 필요)**

---

## 축별 판정 요약

| 축 | 판정 | 등급 | 핵심 이슈 |
|----|------|------|----------|
| A1 일관성 | 🔴 | **D** | 전문가 수 불일치, Phase 5 Critic 충돌, INDEX.md 미존재 |
| A2 필요성 | 🟡 | **B** | Deep Causal Drill 5단계/Cross-Domain 5축 과잉, 중복 기술 존재 |
| A3 직교성 | 🟡 | **B+** | 통합 전문가 내적 긴장, Geopolitical Strategist 위치 불명확 |
| A4 복잡도 | 🔴 | **C** | 토큰/시간 예산 비현실, Deep Loop 최악 케이스 60 rounds |
| A5 철학 정렬 | ✅ | **A-** | 설계 철학은 명확. 실행과 설계 사이 gap이 주된 리스크 |

---

## A1. 일관성 (Consistency) — 🔴 등급 D

### 발견 1: 전문가 수 불일치 ⚠️ Critical

| 위치 | 기술 |
|------|------|
| EXPERTS.md 요약 테이블 | **18명** (11 전문가 + 5 사회자 + 8 Critic... 계산 오류) |
| EXPERTS.md Phase 1 구성 | Regime + Counter-Consensus + **Geopolitical Strategist** + Moderator = **4명** |
| EXPERTS.md 요약 "Macro" 행 | "2 (Regime Analyst, Counter-Consensus)" — **Geopolitical Strategist 누락** |
| METHODOLOGY §15.3 | "전문가 **19명**" |
| EXPERTS.md 본문 실제 수 | Data Auditor(1) + Macro(3+1M) + Sector(1+1C+1M) + VC(1+1C+1M) + Company(1+1C+1M) + Tech(1+1C+1M) + Cross(1) + Allocator(1) = **19명** |

**문제:** 세 곳에서 세 가지 다른 숫자 (18, 19, 요약 테이블 합계 불명). Critic 열에 "8"이라고 쓰여 있지만 전담 Critic은 5명.

**권고:** EXPERTS.md 요약 테이블 전면 재작성. 19명 기준으로 통일.

---

### 발견 2: Phase 5 Critic 담당 충돌 ⚠️ Critical

| 위치 | 기술 |
|------|------|
| WORKFLOW Phase 5 Round 2 | "**Technical Moderator**가 각 기술적 뷰에 대해 반론" |
| EXPERTS.md L5 | "**Signal Skeptic** (전담 Critic)" |
| METHODOLOGY §10.5 | "L5: **Signal Skeptic** 단일 Loop" |

**문제:** WORKFLOW만 유일하게 Technical Moderator를 Critic으로 기술. EXPERTS와 METHODOLOGY는 Signal Skeptic.

**권고:** WORKFLOW Phase 5 수정 → Signal Skeptic으로 통일.

---

### 발견 3: INDEX.md 미존재

METHODOLOGY §15.1에서 "INDEX.md 반영 여부 확인"을 요구하지만, INDEX.md가 존재하지 않음.

**권고:** 삭제(§15.1에서 참조 제거) 또는 생성.

---

### 발견 4: Counter-Consensus Round 1 역할 불일치 (Minor)

EXPERTS.md에서 Counter-Consensus는 "Round 1 참여하지 않음"이라고 명시하나, Adversarial Debate Protocol 요약표에서는 "Round 1 독립 뷰 후 Round 2 Critic"이라고 기술. 이전 버전 잔재로 보임.

**권고:** 요약표 수정 → "Round 2 Critic 전담"으로 통일.

---

### 발견 5: DATA-SOURCES ↔ METHODOLOGY 중복

Data Source Health Check 절차가 두 문서 모두에 기술됨:
- METHODOLOGY §3-1: 점검 항목 테이블 + 규칙
- DATA-SOURCES.md: 거의 동일한 테이블 + 장애 시 대응

**권고:** METHODOLOGY는 원칙만 (1-2줄), 상세 절차는 DATA-SOURCES로 단일화.

---

## A2. 필요성 (Necessity) — 🟡 등급 B

### 발견 6: Deep Causal Drill 5단계 — 과잉 의심

5단계까지 인과사슬 추적은 이론적으로 강력하나:
- 실제 분석에서 3단계 이상 추적한 사례: BMNR Deep Loop에서 **미실행**
- 5단계까지 추적 가능한 데이터가 공개 소스로 존재하는 경우 극히 드묾
- 예시(나프텐 원유)는 인상적이나, 실제 반복 가능한 절차가 아닌 **이상적 사례**

**바닐라 테스트:** "Deep Causal Drill을 삭제하면 최근 분석 결과가 달라졌을까?" → **NO** (최근 3건에서 미실행)

**권고:** 5단계 → 3단계로 축소. "3단계 이상 추적 가능하면 보너스" 정도로 완화. 또는 Bottleneck Hunter의 기존 역할에 자연스럽게 통합 (별도 모듈 불필요).

---

### 발견 7: Cross-Domain Comparison 5축 × Layer별 의무 — 과잉 의심

현재: 5개 비교 축(X1-X5)이 정의되고, Layer별 의무 탐색 축이 지정됨.
- L2: X1, X2 의무
- L3: X2, X4 의무
- L4: X1, X3, X5 의무

**문제:**
- 총 7개 의무 비교가 매 분석마다 실행되어야 함
- 실제 분석에서 의미 있는 이종 비교가 나오는 빈도: 낮음
- 의무이므로 무의미한 비교도 형식적으로 채워야 하는 압박

**바닐라 테스트:** "Cross-Domain 비교를 삭제하면 BMNR Deep Loop 결과가 달라졌을까?" → **부분적 YES** (MSTR 유비는 유용했으나, X4 인재경쟁은 무관)

**권고:** 5축 → "Moderator가 가장 유관한 1-2축을 선택하여 탐색" (의무 축 지정 삭제). 형식적 채우기보다 선택적 깊이.

---

### 발견 8: Historical Analogy Engine 위치 중복

- METHODOLOGY §7에 Historical Analogy Engine 상세 기술
- WORKFLOW Phase 4에서 "Round 1 후, Round 2 전" 별도 단계로 기술
- EXPERTS.md Company Analyst에도 "Historical Analogy Engine 4축 탐색 주도" 기술

세 곳에서 같은 내용을 반복. 변경 시 3곳 동시 수정 필요 → 정합성 리스크.

**권고:** METHODOLOGY에만 상세 기술, WORKFLOW/EXPERTS는 "§7 참조"로 단순화.

---

## A3. 직교성 (Orthogonality) — 🟡 등급 B+

### 발견 9: Geopolitical Strategist 직교성 — 우수하나 위치 불명확

v4.1에서 신설된 Geopolitical Strategist(Papic Constraints Framework)는 **기존 전문가 누구도 커버하지 못하는 독자적 관점** 제공 → 직교성 우수.

**문제:** L1에만 배치되어 있으나, 실제로 지정학은 L2(산업정책), L4(기업 리스크)에도 직접 영향. Cross-Layer로 승격할 가치 있음.

**권고:** 현재 위치 유지하되, L4 Company에서 "지정학 리스크 있는 종목은 Phase 1의 Geopolitical Strategist 결과를 명시적으로 참조" 규칙 추가.

---

### 발견 10: 통합 전문가 내적 긴장

| 전문가 | 통합 대상 | 긴장 |
|--------|----------|------|
| Regime Analyst | Dalio (구조적/장기) + Druckenmiller (전술적/유동성) | 시간축 충돌 — "명시적 분리" 규칙으로 관리 중 ✅ |
| Opportunity Scanner | Wood (파괴적 혁신) + Lynch (일상 발굴) | 철학 충돌 — Wood는 고밸류 성장, Lynch는 GARP. 분리 규칙 없음 ⚠️ |
| Company Analyst | Buffett (장기 복리) + Ackman (이벤트/행동주의) | 시간축 충돌 — "장기/단기 분리" 규칙으로 관리 중 ✅ |

**권고:** Opportunity Scanner에 "혁신적 관점"과 "일상 발굴 관점" 명시적 분리 규칙 추가.

---

### 발견 11: Critic 직교성 — 우수

5명의 전담 Critic이 각각 다른 공격 벡터를 담당:
- Counter-Consensus: 컨센서스 반전
- Sector Skeptic: 버블/TAM 과대
- Moat Breaker: 해자 파괴/AI 치환
- Forensic Accountant: 회계/재무 사기
- Signal Skeptic: 시그널 과적합

**판정:** ✅ 직교. 겹치는 공격 벡터 없음.

---

## A4. 복잡도 적정성 (Complexity Adequacy) — 🔴 등급 C

### 발견 12: 최악 케이스 Debate Rounds — 비현실적 ⚠️ Critical

**계산:**
- Deep Loop: Inner Loop 4 rounds × Outer Loop max 5 iterations = **20 rounds/Layer**
- L2, L3, L4에 Deep Loop 적용 = **60 rounds** (Event Day)
- 각 round에 전문가 3-4명 참여 = **180-240 전문가 발언**
- 추가: L1, L5 각 4 rounds = 8 rounds
- **총합: 최대 68 rounds, ~200+ 전문가 발언**

**현실:** 단일 Opus 세션에서 이 분량을 09:00 KST까지 처리하는 것은 불가능. 토큰 예산 80-100K로도 부족.

**권고:**
1. Outer Loop 실질적 상한을 **3회**로 축소 (5회는 이론적 상한으로만 유지)
2. Event Day에서도 Deep Loop 적용은 **핵심 Layer 1개만** (보유종목 이벤트 → L4만, 매크로 이벤트 → L1만)
3. On-demand 분석에서만 Multi-Layer Deep Loop 허용

---

### 발견 13: Standard Day 토큰 추정 — 과소

**Standard Day 실제 구성:**
- Phase 0: 데이터 수집 (매크로+종목+크립토+뉴스) — ~5K
- Phase 0.5: Data Audit — ~3K
- Phase 1: L1 Macro Regime (간략) — ~5K
- Phase 4: L4 Company Quick Risk Check (4종목 × Kill+뉴스) — ~8K
- Phase 4.5: Technical Dashboard — ~3K
- Phase 6: Synthesis + Card Check — ~5K
- Phase 7: Delivery formatting — ~2K
- Phase 8: PT Record — ~2K

**실질 추정:** ~33-40K (30K는 낙관적)

**권고:** "~30-40K"로 수정. 또는 Standard Day를 더 압축 (Phase 0.5 생략 가능).

---

### 발견 14: Edge Score 공식 — 불필요하게 정교

현재: Base Score = E통과수 × 2 + Consensus Modifier(0/+1/+2), Cap 10

**문제:**
- Edge Test 4문항 자체가 정성적 YES/NO 판단
- 그 위에 정량 공식을 씌우는 것은 **정밀도 환상** (precision illusion)
- "E1-E4 중 3개 YES, 컨센서스 반대 → 8점"이라는 공식이 "3/4 통과, 컨센서스 반대 → Strong Edge"보다 나은 정보를 제공하지 않음

**권고:** 공식 삭제. 다음으로 단순화:

```
Edge 판정:
- 4/4 YES → 🟢 Strong Edge (적극 포지션)
- 3/4 YES → 🟡 Moderate Edge (소규모 or 워치)
- 2/4 이하 → 🔴 No Edge (PASS)
컨센서스 Modifier: 반대 시 한 단계 상향 허용
```

---

### 발견 15: METHODOLOGY 섹션 수 — 바닐라 경계

현재 §1~§15, 15개 섹션. 일부는 실질적으로 독립 모듈:

| § | 섹션 | 최근 3건 분석 기여 | 판정 |
|---|------|------------------|------|
| 1 | Rocket with Tight Bolts | ✅ 핵심 철학 | 유지 |
| 2 | AI Commoditization Filter | ✅ ERII, CLS 분석에 기여 | 유지 |
| 3 | Reality Grounding Layer | ⚠️ 3-1~3-5가 5개 하위 모듈 | 정리 필요 |
| 4 | Fresh Eyes Protocol | ✅ Fresh Eyes 34종목 직접 사용 | 유지 |
| 5 | Price Drop Triage | ✅ CRCL -17% 직접 사용 | 유지 |
| 6 | Causal Mechanism Map | 🟡 ERII 예시 외 실사용 불명확 | §10 통합 후보 |
| 7 | Historical Analogy Engine | 🟡 BMNR MSTR 유비 외 실사용 불명확 | 단순화 후보 |
| 8 | Management Will Tracker | ✅ BMNR Tom Lee 분석에 기여 | 유지 |
| 9 | Conviction Card | ✅ 핵심 산출물 | 유지 |
| 10 | Deep Loop Protocol | ✅ BMNR Deep Loop 직접 사용 | 유지 (단순화) |
| 11 | 확률 결합 & 사이징 | ✅ 핵심 모듈 | 유지 |
| 12 | 리스크 관리 Hard Rules | ✅ 핵심 모듈 | 유지 |
| 13 | 성과 추적 | ✅ PT 시스템 운영 | 유지 |
| 14 | ICL | ✅ 포트폴리오 전략에 기여 | 유지 |
| 15 | 헌법 정합성 | 🆕 신설 | 유지 |

**권고:** §6(Causal Mechanism Map)을 §10(Deep Loop)의 하위 절차로 통합. §7(Historical Analogy)도 §10에 통합 가능. 이러면 15→13개 섹션.

---

## A5. 철학 정렬 (Philosophy Alignment) — ✅ 등급 A-

### 강점

1. **Dual Thinking 설계 명확** — [THESIS] vs [FACT] 태그 시스템은 간결하고 효과적
2. **Edge 추구 시스템 설계 우수** — C0 Thesis → VP Box → Edge Score의 논리 흐름이 "echo chamber 탈출"이라는 목표에 정확히 부합
3. **ICL 실효성** — Oct 2025 트라우마, 결혼, Arena/Vault 프레임 등 진짜 맥락이 반영됨
4. **Anti-Sycophancy** — "Shawn의 말도 팩트가 아니다" 원칙이 명시적

### 약점

1. **설계 vs 실행 갭** — 설계는 "insight 생성 시스템"이나, 실행은 "절차 체크리스트"에 가까워질 위험. Deep Loop 5회가 형식적으로 진행되면 에코 챔버보다 나을 것이 없음
2. **PT 시스템 미가동** — 설계는 완료했으나 데이터 축적 0건 (4/20 시작 예정). 자기 교정 루프가 아직 열려 있지 않음
3. **"100x Shawn" 섹션 실효성** — 설계 의도는 좋으나, 실제로 읽히고 행동으로 전환되는지 검증 필요

---

## 수정 권고 우선순위

### 🔴 즉시 수정 (이번 세션)

| # | 항목 | 행동 |
|---|------|------|
| 1 | **EXPERTS.md 요약 테이블** | 19명 기준 재작성, Geopolitical Strategist 포함 |
| 2 | **WORKFLOW Phase 5 R2** | "Technical Moderator" → "Signal Skeptic" 수정 |
| 3 | **INDEX.md 참조** | METHODOLOGY §15.1에서 삭제 또는 INDEX.md 생성 |

### 🟡 단기 개선 (1주 내)

| # | 항목 | 행동 |
|---|------|------|
| 4 | **Deep Loop 실질 상한** | Outer Loop 3회 기본, 5회는 예외 (Shawn 요청 시) |
| 5 | **Cross-Domain 의무 축** | 축 지정 삭제 → Moderator 재량 1-2축 |
| 6 | **Edge Score** | 공식 삭제 → 3단계 단순 판정 |
| 7 | **Data Source Health Check 중복** | METHODOLOGY는 원칙 1줄, DATA-SOURCES에 상세 |
| 8 | **Standard Day 토큰** | 30K → 30-40K 수정 |

### 🟢 중기 개선 (분기 내)

| # | 항목 | 행동 |
|---|------|------|
| 9 | §6, §7 → §10 통합 | Causal Map, Analogy를 Deep Loop 하위 절차로 |
| 10 | Counter-Consensus 요약표 정리 | "Round 2 Critic 전담" 통일 |
| 11 | Opportunity Scanner 분리 규칙 | Wood vs Lynch 관점 명시적 분리 |
| 12 | Event Day Deep Loop 적용 범위 | 핵심 Layer 1개만 Deep Loop, 나머지 단일 Loop |

---

## 종합 판정

**등급: C+ (개선 필요)**

| 강점 | 약점 |
|------|------|
| 설계 철학(Rocket with Tight Bolts) 명확 | 실행 복잡도가 설계 철학과 모순 |
| Edge 추구 구조(C0/VP/Edge Score) 우수 | 전문가 수/절차 수가 과도 |
| Critic 직교성 우수 | 문서 간 정합성 오류 다수 |
| ICL/Anti-Sycophancy 실효적 | 토큰/시간 예산 비현실 |
| PT 시스템 설계 완료 | PT 데이터 미축적 |

**핵심 메시지:**
> PLEDS는 **설계 의도로는 A급 시스템**이나, **실행 가능성과 문서 정합성에서 C급**.
> "필요한 만큼 복잡하고 그 이상은 아닌" 바닐라 원칙을 **시스템 자체에도 적용**해야 한다.
> 나사를 더 조이는 것보다, **불필요한 나사를 빼는 것**이 현재 가장 필요한 작업.
