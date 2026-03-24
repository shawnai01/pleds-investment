# PLEDS System Review — From Analysis Machine to Investment Partner

> **Date:** 2026-03-24
> **Reviewer:** CRO (Chief Research Officer)
> **Version Reviewed:** PLEDS v2.2
> **Scope:** 전체 시스템 진단 + 발전 방향 제안

---

## Executive Summary

PLEDS는 **분석 시스템으로서는 탁월**하다. 14개 섹션, 24명 전문가, Adversarial Debate Protocol, ICL — 모두 잘 설계되어 있다.

그러나 **분석 품질 ≠ 투자 성과**라는 근본적 gap이 있다.

2026-03-24 포트폴리오 리뷰가 이를 증명한다: 시스템은 "이 포트폴리오는 목표 달성이 불가능하다"고 명확히 진단했다. 그러나 그 진단이 **실제 포트폴리오 변경으로 이어졌는가?** 이 연결고리가 약하다.

**핵심 진단:**
- 🟢 **강점:** 분석 프레임워크, 데이터 인프라, 반론 시스템
- 🔴 **약점:** 분석→결정 전환, 행동 추적, 포지션 관리, 복잡도
- 🟡 **기회:** "분석 시스템"에서 "투자 파트너"로의 진화

---

## Part 1: 현재 시스템의 강점과 약점 진단

### 1.1 14개 섹션 실효성 평가

| 섹션 | 이름 | 실효성 | 판정 | 비고 |
|------|------|--------|------|------|
| §1 | Rocket with Tight Bolts | ⭐⭐⭐⭐⭐ | **KEEP** | 핵심 원칙. [THESIS]/[FACT] 구분은 실제로 분석 품질 향상 |
| §2 | AI Commoditization Filter | ⭐⭐⭐⭐ | **KEEP** | Search Problem Lens, Verification Moat — 2026년 시대에 필수 |
| §3 | Reality Grounding Layer | ⭐⭐⭐⭐ | **KEEP** | Data Health Check는 작동 중. 정보 Tier 체계 유용 |
| §4 | Fresh Eyes Protocol | ⭐⭐⭐ | **SIMPLIFY** | 좋은 원칙이나 실제 적용 빈도 낮음. Delta Journal과 통합 가능 |
| §5 | Price Drop Triage | ⭐⭐⭐⭐⭐ | **KEEP** | 실전에서 즉시 적용 가능. 3가지 가설 프레임 명확 |
| §6 | Causal Mechanism Map | ⭐⭐⭐⭐ | **KEEP** | 깊은 이해에 필수. 단, 모든 종목에 작성되고 있는지? |
| §7 | Historical Analogy Engine | ⭐⭐⭐ | **STREAMLINE** | 4축 탐색이 heavy. 2축(밸류에이션+산업)으로 축소 검토 |
| §8 | Management Will Tracker | ⭐⭐⭐⭐ | **KEEP** | Insider 행동 추적은 alpha. Form 4 자동 수집 연동 필요 |
| §9 | Conviction Card & Convergence | ⭐⭐⭐⭐⭐ | **CORE** | C1-C4 프레임이 PLEDS의 핵심. 잘 설계됨 |
| §10 | Adversarial Debate Protocol | ⭐⭐⭐⭐⭐ | **CORE** | Critic 강제 참여가 echo chamber 방지. 실제 작동 확인 |
| §11 | 확률 결합 & 포지션 사이징 | ⭐⭐⭐ | **REVIEW** | Layer별 가중치가 실제로 적용되는지 불분명 |
| §12 | 리스크 관리 Hard Rules | ⭐⭐⭐⭐ | **ENFORCE** | 규칙은 좋으나 실행 추적이 없음 |
| §13 | 성과 추적 | ⭐⭐ | **IMPROVE** | PT 시스템 설계됨, 실제 데이터 축적 부족 |
| §14 | ICL (Investor Context Layer) | ⭐⭐⭐⭐ | **EXPAND** | 방금 추가. 좋은 방향. 더 적극적으로 활용 |

**종합 평가:**
- **Core (유지 필수):** §1, §5, §9, §10, §12, §14
- **Keep (현행 유지):** §2, §3, §6, §8
- **Simplify/Review (간소화 검토):** §4, §7, §11, §13

### 1.2 실제 분석 결과물과 METHODOLOGY의 Gap

**debates/ 폴더 분석 (50+ 파일):**

| 항목 | METHODOLOGY 요구 | 실제 분석 | Gap |
|------|------------------|----------|-----|
| Causal Mechanism Map | L3에서 의무 작성 | 일부 종목에만 존재 | 🔴 미준수 |
| Historical Analogy | 4축 탐색 의무 | 2-3축 탐색이 대부분 | 🟡 부분 준수 |
| Conviction Card | 모든 제안에 C1-C4 | 대부분 포함 | 🟢 준수 |
| Critic 반론 | Round 2에서 의무 | 대부분 포함 | 🟢 준수 |
| Management Will | L4에서 의무 평가 | 일부만 포함 | 🟡 부분 준수 |
| PT Recording | 모든 판단 기록 | tracking/judgments/ 38개 | 🟡 부분 준수 |
| Reality Audit | 주간/월간 실행 | audit/ 폴더 거의 비어있음 | 🔴 미준수 |

**결론:** METHODOLOGY의 약 60-70%가 실제로 적용되고 있음. 그러나 **성과 추적(§13)**과 **현실 감사(§3-4)**가 가장 취약.

### 1.3 "좋은 분석" → "좋은 투자 결정" 연결고리

**문제의 핵심:** 2026-03-24 포트폴리오 리뷰 사례

```
분석 결론: "포트폴리오가 구조적으로 목표 달성 불가능. C- 등급"
실제 행동: ???
```

시스템이 아무리 날카로운 진단을 해도, **그 진단이 Shawn의 실제 결정에 얼마나 영향을 미치는지 추적하지 않는다.**

| 단계 | 현재 상태 | 문제 |
|------|----------|------|
| 분석 | ✅ 탁월 | — |
| 진단 | ✅ 솔직 | — |
| 제안 | ✅ 구체적 | — |
| **결정** | ❓ 추적 안 됨 | Shawn이 제안을 수용했는지, 거부했는지 모름 |
| **실행** | ❓ 추적 안 됨 | 실제 매매가 언제, 어떻게 이루어졌는지 모름 |
| **복기** | ❌ 거의 없음 | 과거 결정의 성과를 체계적으로 리뷰하지 않음 |

**이것이 "분석 시스템"과 "투자 파트너"의 차이다.**

분석 시스템: 보고서를 생산한다.
투자 파트너: 결정을 함께 내리고, 그 결과를 함께 책임진다.

### 1.4 정보 과부하 리스크: 24명 전문가가 너무 많은가?

**현재 전문가 구조:**

| Layer | 전문가 수 | 역할 |
|-------|----------|------|
| Data Integrity | 1 | Data Auditor |
| Macro | 5 | Machine, Hawk, Sentinel, Contrarian, Moderator |
| Sector | 4 | Disruptor, Value Mapper, Theme Hunter, Moderator |
| Value Chain | 3 | Strategist, Network Thinker, Moderator |
| Company | 4 | Compounder, Catalyst, Forensic, Moderator |
| Technical | 4 | Dashboard, Time Series, Structure, Moderator |
| Cross-Layer | 1 | Bottleneck Hunter |
| Synthesis | 1 | Allocator |
| **Total** | **24** | |

**평가:**

🟢 **필요한 전문가:**
- Allocator (필수)
- Forensic Accountant (Critic, 필수)
- Bottleneck Hunter (차별화 요소)
- 각 Layer Moderator (수렴 필수)

🟡 **통합 가능:**
- Machine + Liquidity Hawk → "Macro Regime Analyst" (둘 다 유동성/사이클)
- Cycle Sentinel + Contrarian → "Counter-Consensus Analyst"
- Disruptor + Theme Hunter → "Opportunity Scanner"
- Value Mapper + Strategist → "Moat Analyst"
- Compounder + Catalyst → "Company Analyst" (Forensic이 Critic)
- Time Series + Structure Reader → "Technical Analyst" (Dashboard는 자동화)

**권장안: 24 → 15명으로 축소**

| Layer | 축소 후 | 역할 |
|-------|--------|------|
| Data | 1 | Data Auditor |
| Macro | 3 | Regime Analyst, Counter-Consensus, Moderator |
| Sector | 2 | Opportunity Scanner, Moderator |
| Value Chain | 2 | Moat Analyst, Moderator |
| Company | 3 | Company Analyst, Forensic (Critic), Moderator |
| Technical | 2 | Technical Analyst (Dashboard 자동화), Moderator |
| Cross-Layer | 1 | Bottleneck Hunter |
| Synthesis | 1 | Allocator |
| **Total** | **15** | |

**효과:**
- 인지 부하 37% 감소
- 토론 품질 유지 (Critic + Moderator 구조 보존)
- 분석 시간 단축
- 핵심 인사이트에 집중

---

## Part 2: Gap Analysis — 빠진 것들

### 2.1 시장 구조 변화 감지 (Regime Change Detection) 🔴 MISSING

**현재 상태:** Macro Layer가 레짐을 판정하지만, **변화 시점을 감지하는 systematic trigger가 없음.**

**문제:**
- VIX 25+ 돌파 시 Macro 재판정 → 이건 반응형
- **선제적** 레짐 변화 감지가 없음

**필요한 것:**

| 지표 | 임계치 | 의미 |
|------|--------|------|
| VIX | 20→25 상향 돌파 | 공포 시작 |
| 2-10 Spread | 0→음수 | 경기 침체 신호 |
| HY Spread | +50bp 급등 | 신용 리스크 |
| BTC | -15% 주간 | 크립토 레짐 전환 |
| DXY | +3% 월간 | 달러 강세 레짐 |

**→ P1 제안: Regime Sentinel 시스템 신설**

### 2.2 포지션 관리 (Holding Period Management) 🔴 MISSING

**현재 상태:**
- C2 Entry, C4 Kill은 있음
- **진입 후 관리가 없음**

| 상황 | 현재 대응 | 필요한 대응 |
|------|----------|------------|
| +30% 수익 | 규칙 없음 | Trim 규칙 필요 |
| -10% 손실 | Price Drop Triage | ✅ 있음 |
| 6개월 보유 후 | 규칙 없음 | Re-evaluation 강제 |
| Thesis 진행 중 | 규칙 없음 | Milestone check |
| 목표가 도달 | C3에 명시 | 실행 추적 없음 |

**문제:** "언제 진입하고 언제 손절하는지"는 있지만, **"보유 중에 어떻게 관리하는지"가 없음.**

**→ P2 제안: Position Management Protocol 신설**

### 2.3 심리/행동 편향 추적 (Decision Tracking) 🔴 CRITICAL MISSING

**현재 상태:** Shawn의 실제 결정 vs 시스템 권고를 추적하지 않음

**이것이 중요한 이유:**

```
시나리오 A: 시스템이 "매수"라고 했는데 Shawn이 안 샀다 → 이후 +50%
시나리오 B: 시스템이 "손절"이라고 했는데 Shawn이 버텼다 → 이후 -30%
```

이런 패턴을 추적하면:
1. **시스템의 실제 정확도**를 알 수 있음
2. **Shawn의 행동 편향**을 식별할 수 있음
3. **"어떤 조언을 Shawn이 잘 따르고, 어떤 조언을 무시하는지"** 패턴 발견
4. ICL을 더 정교하게 캘리브레이션 가능

**→ P1 제안: Decision Tracker 시스템 신설**

### 2.4 실시간 뉴스/이벤트 반응 프로토콜 🟡 PARTIAL

**현재 상태:** WORKFLOW.md에 이벤트 트리거 테이블 존재

```
| 트리거 | 대응 |
| 보유 종목 ±5% | Chart + Company 긴급 리뷰 |
| VIX 25+ | Macro 긴급 재판정 |
```

**문제:** 
- 트리거는 있으나 **표준화된 대응 템플릿이 없음**
- 각 이벤트에 대한 **의사결정 트리가 없음**

**예시 — FOMC 발표 대응:**
```
현재: "Macro 즉시 업데이트"
필요: 
  - 예상 대비 Hawkish → 포지션 X% 축소?
  - 예상 대비 Dovish → 워치리스트 진입?
  - In-line → 유지?
```

**→ P2 제안: Event Playbook 신설**

### 2.5 섹터 로테이션 / 상관관계 모니터링 🔴 MISSING

**현재 상태:** Sector Layer가 섹터를 평가하지만, **포트폴리오 내 상관관계를 모니터링하지 않음**

**문제:**
- 포트폴리오 리뷰에서 "BMNR + CRCL = 사실상 하나의 베팅"이라고 진단
- 그러나 이 상관관계를 **상시 모니터링하는 시스템이 없음**

**필요한 것:**
- 포지션 간 상관계수 추적
- 단일 테마 익스포저 경고
- 섹터 로테이션 신호

**→ P3 제안: Correlation Dashboard 신설**

### 2.6 Watchlist → Entry 전환 자동화 🟡 PARTIAL

**현재 상태:** PORTFOLIO.md에 워치리스트와 진입 조건이 명시됨

```
| QXO | $16-17 | ⭐⭐ WATCH |
```

**문제:**
- 가격이 타겟에 도달해도 **자동 알림이 없음**
- "48시간 내 실행 또는 thesis 업데이트" 규칙이 있지만 **추적되지 않음**

**→ P2 제안: Watchlist Alert 자동화**

---

## Part 3: 발전 방향 제안 — Priority 순

### P1-1: Decision Tracker 시스템 🔴 즉시 구현

**WHY:** 현재 gap 중 가장 치명적. 시스템이 좋은 조언을 해도 **실제로 따랐는지, 그 결과가 어땠는지** 모르면 개선 불가능.

**WHAT:** 
- 모든 시스템 권고(BUY/SELL/HOLD)를 기록
- Shawn의 실제 결정을 기록
- 이후 결과를 추적
- 분기별 "System vs Shawn" 정확도 비교

**HOW:**

```markdown
# tracking/decisions/YYYY-MM-DD-TICKER.md

## 시스템 권고
- 날짜: 2026-03-24
- 종목: BMNR
- 권고: TRIM (35% → 20%)
- 근거: Kelly oversized, 목표 달성 불가

## Shawn 결정
- 결정: [ ] 수용 / [x] 부분 수용 / [ ] 거부
- 실제 행동: TRIM (35% → 17.8%)
- Shawn 근거: "일단 보수적으로"

## 추적
- +30d 가격: $___
- +90d 가격: $___
- 사후 평가: 시스템 맞음 / Shawn 맞음 / 무승부
```

**파일 구조:**
```
tracking/
├── decisions/
│   ├── 2026-03-24-BMNR-trim.md
│   ├── 2026-03-24-LLY-entry.md
│   └── ...
├── decision-accuracy.md  # 분기별 집계
└── behavioral-patterns.md  # 발견된 패턴
```

**PRIORITY:** P1 (즉시)

**ICL Critic Pass:**
- ✅ "Shawn에게 도움이 되는가?" — 자신의 행동 패턴을 객관적으로 볼 수 있음
- ✅ "인식을 확장하는가?" — "나는 어떤 조언을 무시하는 경향이 있는가?" 인사이트
- ✅ "실행 가능한가?" — 매 권고 시 1분 추가 기록. 인지 비용 낮음

---

### P1-2: Regime Sentinel 시스템 🔴 즉시 구현

**WHY:** 레짐 변화를 **반응형**이 아닌 **선제적**으로 감지해야 함

**WHAT:**
- 5개 핵심 지표의 임계치 모니터링
- 임계치 돌파 시 자동 알림 + Macro Layer 긴급 소집

**HOW:**

```markdown
# daily/regime-sentinel.md

## 현재 레짐: Risk-On (70%)
## 최종 업데이트: 2026-03-24

| 지표 | 현재값 | 임계치 | 상태 |
|------|--------|--------|------|
| VIX | 18.2 | >25 | 🟢 정상 |
| 2-10 Spread | +42bp | <0 | 🟢 정상 |
| HY Spread | 320bp | >400bp | 🟢 정상 |
| BTC 주간 | -3.2% | <-15% | 🟢 정상 |
| DXY 월간 | +0.8% | >+3% | 🟢 정상 |

## 경고: 0/5
## 다음 점검: 2026-03-25 09:00 KST
```

**트리거 규칙:**
- 1개 임계치 돌파 → 🟡 주의, 해당 Layer 재검토
- 2개 임계치 돌파 → 🟠 경고, Macro 긴급 재판정
- 3개+ 임계치 돌파 → 🔴 레짐 전환 선언, 전 포지션 재검토

**PRIORITY:** P1 (즉시)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — 시장 변화를 더 빨리 감지하여 대응 시간 확보
- ✅ "복잡도 대비 가치?" — 5개 지표만 추적. 단순함
- ✅ "실행 가능한가?" — 일일 브리핑에 10초 추가

---

### P1-3: 전문가 시스템 간소화 (24 → 15)

**WHY:** 현재 24명은 인지 과부하. 실제로 모든 전문가가 독립적 가치를 제공하지 않음.

**WHAT:** 유사 역할 통합, Critic + Moderator 구조 유지

**HOW:**

```markdown
# EXPERTS-V3.md 개정안

## 통합 전 → 통합 후

### Macro Layer (5 → 3)
- Machine + Liquidity Hawk → **Regime Analyst**
- Cycle Sentinel + Contrarian → **Counter-Consensus Analyst**
- Moderator 유지

### Sector Layer (4 → 2)
- Disruptor + Theme Hunter → **Opportunity Scanner**
- Value Mapper → Moat Analyst로 이동
- Moderator 유지

### Value Chain Layer (3 → 2)
- Strategist + Value Mapper → **Moat Analyst**
- Network Thinker → Moat Analyst에 흡수
- Moderator 유지

### Company Layer (4 → 3)
- Compounder + Catalyst → **Company Analyst**
- Forensic 유지 (전담 Critic)
- Moderator 유지

### Technical Layer (4 → 2)
- Dashboard → 자동화 (전문가 아님)
- Time Series + Structure → **Technical Analyst**
- Moderator 유지
```

**PRIORITY:** P1 (1주 내)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — 분석 속도 향상, 핵심에 집중
- ⚠️ "복잡도 대비 가치?" — 통합 시 미묘한 관점 손실 가능. 3개월 후 평가 필요
- ✅ "실행 가능한가?" — EXPERTS.md 한 번 개정으로 완료

---

### P2-1: Position Management Protocol 🟡 1주 내

**WHY:** 진입 후 "어떻게 보유하는가"에 대한 규칙이 없음

**WHAT:**

| 상황 | 규칙 |
|------|------|
| **+30% 수익** | Trim 25% of position + 손절선 BEP로 상향 |
| **+50% 수익** | Trim 50% of position + 잔여는 "house money" |
| **+100% 수익** | 원금 회수 + 잔여 free ride |
| **3개월 정체** | Thesis 재검토 강제 |
| **6개월 보유** | Full re-evaluation (Fresh Eyes) |
| **Thesis milestone 달성** | 다음 milestone 설정 또는 익절 |
| **Thesis milestone 실패** | 손절 검토 (C4 유사) |

**HOW:**

```markdown
# conviction/BMNR.md에 추가

## Position Management Rules
- Entry: $18 (2026-03-XX)
- Current: $21.57 (+19.8%)
- Next milestone: ETH $3,000 (현재 $2,184)
- Trim trigger: $27 (+50%) → Trim 25%
- Review date: 2026-06-XX (3개월)
```

**PRIORITY:** P2 (1주 내)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — "언제 이익 실현하지?"라는 질문에 답
- ✅ "복잡도 대비 가치?" — 규칙 6개, 단순함
- ⚠️ "실행 가능한가?" — Shawn의 실제 성향(승자 오래 보유 선호)과 충돌 가능. 협의 필요

---

### P2-2: Event Playbook 🟡 1주 내

**WHY:** 이벤트 발생 시 "어떻게 대응하는가"가 표준화되어 있지 않음

**WHAT:**

```markdown
# playbooks/fomc.md

## FOMC 대응 Playbook

### 시나리오 1: 예상 대비 Hawkish (+25bp more than expected)
- 즉시 행동: 
  - 성장주 익스포저 -5%
  - 달러 수혜주 검토
  - VIX 확인
- 48시간 내: Macro Layer 재판정

### 시나리오 2: 예상 대비 Dovish (-25bp more than expected)
- 즉시 행동:
  - 워치리스트 진입 검토
  - 성장주 익스포저 확대 검토
- 48시간 내: Macro Layer 재판정

### 시나리오 3: In-line (예상과 일치)
- 즉시 행동: 없음
- 주간 리뷰에서 반영
```

**커버할 이벤트:**
- FOMC
- CPI/PPI
- 실적 발표 (보유 종목)
- BTC 급변 (±10%)
- VIX 급등 (25+)

**PRIORITY:** P2 (1주 내)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — 이벤트 시 즉각 대응 가이드 제공
- ✅ "복잡도 대비 가치?" — 5개 이벤트 × 3 시나리오 = 15개 규칙. 관리 가능
- ✅ "실행 가능한가?" — 한 번 작성 후 참조만

---

### P2-3: Watchlist Alert 자동화 🟡 1주 내

**WHY:** 워치리스트 진입 조건이 있어도 **가격 도달 시 알림이 없음**

**WHAT:**
- PORTFOLIO.md의 워치리스트를 파싱
- 일일 가격 수집 시 진입 조건 체크
- 조건 충족 시 텔레그램 알림

**HOW:**

```bash
# cron 또는 daily briefing에 추가

python3 scripts/watchlist-alert.py
```

```python
# scripts/watchlist-alert.py (pseudo)

watchlist = parse_portfolio_md()
for ticker, target_price in watchlist:
    current = get_price(ticker)
    if current <= target_price:
        alert(f"🚨 {ticker} hit target! Current: ${current}, Target: ${target_price}")
```

**PRIORITY:** P2 (1주 내)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — 기회 놓치지 않음
- ✅ "복잡도 대비 가치?" — 스크립트 50줄
- ✅ "실행 가능한가?" — 자동화, 인지 비용 0

---

### P3-1: Correlation Dashboard 🟢 1개월 내

**WHY:** 포지션 간 숨겨진 상관관계를 모니터링하지 않음

**WHAT:**
- 보유 종목 간 30일 수익률 상관계수 계산
- 0.7+ 상관관계 쌍 경고
- 단일 테마 익스포저 계산

**HOW:**

```markdown
# audit/correlation-dashboard.md

## 2026-03 Correlation Matrix

|       | BMNR | CRCL | LLY | CLS | ERII |
|-------|------|------|-----|-----|------|
| BMNR  | 1.00 | 0.82 | 0.15| 0.31| 0.08 |
| CRCL  | 0.82 | 1.00 | 0.12| 0.28| 0.05 |
| LLY   | 0.15 | 0.12 | 1.00| 0.08| 0.10 |
| CLS   | 0.31 | 0.28 | 0.08| 1.00| 0.12 |
| ERII  | 0.08 | 0.05 | 0.10| 0.12| 1.00 |

⚠️ 경고: BMNR-CRCL 상관계수 0.82 (임계치 0.7 초과)
→ 사실상 26.4%가 단일 크립토 베팅
```

**PRIORITY:** P3 (1개월 내)

**ICL Critic Pass:**
- ✅ "도움이 되는가?" — 숨겨진 집중도 리스크 가시화
- ⚠️ "복잡도 대비 가치?" — 월 1회 업데이트로 충분. 너무 자주 하면 noise
- ✅ "실행 가능한가?" — API로 가격 데이터 수집 후 pandas로 계산

---

### P3-2: Prune 검토 (분기 1회) 🟢 1개월 내

**WHY:** 바닐라 원칙 — "모듈을 늘리지 않는다"

**WHAT:** 분기마다 모든 섹션/전문가가 **실제로 판정을 바꾼 적이 있는지** 검토

**HOW:**

```markdown
# audit/2026-Q1-prune-review.md

## Prune 검토 기준
"최근 3개월 분석에서 해당 모듈이 판정을 바꾼 적이 있는가?"

| 섹션/전문가 | 판정 변경 | 유지/폐기 |
|-------------|----------|----------|
| Contrarian Catalyst | 3회 (BMNR Bear, ERII timing) | ✅ 유지 |
| Theme Hunter | 1회 (A2A 발굴) | ✅ 유지 |
| Historical Analogy 4축 | 0회 (2축으로 충분했음) | 🟡 2축으로 축소 |
| Network Thinker | 0회 (Moat Analyst와 중복) | 🔴 통합 |
```

**PRIORITY:** P3 (2026-Q2부터 분기 실행)

---

## Part 4: "투자 파트너"로서의 시스템 재정의

### 4.1 현재: 분석 시스템

```
[데이터] → [전문가 토론] → [보고서] → [Shawn 읽음] → ???
```

**문제:** Shawn이 읽은 후 무슨 일이 일어나는지 시스템이 모름

### 4.2 목표: 투자 파트너

```
[데이터] → [전문가 토론] → [권고] → [Shawn 결정] → [실행] → [결과 추적] → [복기] → [시스템 개선]
```

**차이점:**

| 항목 | 분석 시스템 | 투자 파트너 |
|------|------------|------------|
| 산출물 | 보고서 | 권고 + 결정 기록 + 결과 추적 |
| Shawn 역할 | 소비자 | 공동 의사결정자 |
| 피드백 루프 | 없음 | 있음 (Decision Tracker → 시스템 개선) |
| 책임 | 없음 | 공동 책임 (결과 복기) |
| 대화 | 일방향 (보고서 전달) | 양방향 (토론, 질문, 반박) |

### 4.3 투자 파트너가 되려면 추가해야 할 것

**1. Decision Tracker (P1-1)**
- Shawn의 결정을 기록
- 시스템 권고 vs 실제 결정 vs 결과

**2. Weekly 1:1 토론 프로토콜**
- 일방적 보고서 전달이 아닌 **양방향 토론**
- "이 종목에 대해 Shawn은 어떻게 생각하는가?"를 묻고 기록
- Shawn의 직관과 시스템 분석의 차이를 탐구

**3. Quarterly 복기 세션**
- 지난 분기 결정 리뷰
- "어떤 조언이 좋았고, 어떤 조언이 나빴는가"
- 시스템 파라미터 조정 (가중치, 임계치 등)

**4. ICL의 능동적 활용**
- 현재: Shawn 프로파일 참조만
- 목표: Shawn의 행동 패턴까지 반영
- 예: "Shawn은 손절 조언을 70% 무시하는 경향이 있다 → 손절 조언 시 더 강하게 표현"

### 4.4 대화 품질 향상 방향

**현재 대화 패턴:**
```
CRO: [긴 보고서]
Shawn: "알겠어" 또는 "좋아"
```

**목표 대화 패턴:**
```
CRO: BMNR에 대해 시스템은 trim을 권고합니다. 주요 근거는 Kelly 초과 사이징입니다.
     그러나 Shawn의 MSTR 유비 thesis도 일리가 있습니다.
     **질문: ETH가 2년 내 $10K 간다는 확신이 몇 %입니까?**

Shawn: 60% 정도

CRO: 그렇다면 Kelly 공식에 따르면 15% 사이징이 적정합니다. 
     현재 17.8%는 소폭 oversized이지만 허용 범위입니다.
     **trim하지 않고 유지하되, $27(+50%) 도달 시 25% trim하는 것을 권장합니다.**

Shawn: 그렇게 하자

CRO: [기록 완료: BMNR 유지, $27 trim 트리거 설정]
```

**핵심 변화:**
1. 질문을 던져 Shawn의 conviction을 **수치화**
2. 시스템 권고를 Shawn의 답변에 따라 **캘리브레이션**
3. 결정을 **기록**
4. 다음 대화에서 **참조** 가능

---

## Part 5: 핵심 제안 요약 (Priority 순)

| # | 제안 | Priority | 효과 | 구현 난이도 |
|---|------|----------|------|------------|
| 1 | **Decision Tracker** | P1 | 행동 추적, 피드백 루프 | 낮음 |
| 2 | **Regime Sentinel** | P1 | 선제적 레짐 감지 | 낮음 |
| 3 | **전문가 간소화 (24→15)** | P1 | 인지 부하 감소 | 중간 |
| 4 | **Position Management Protocol** | P2 | 보유 중 관리 | 낮음 |
| 5 | **Event Playbook** | P2 | 이벤트 대응 표준화 | 중간 |
| 6 | **Watchlist Alert** | P2 | 기회 포착 자동화 | 낮음 |
| 7 | **Correlation Dashboard** | P3 | 숨겨진 리스크 가시화 | 중간 |

---

## Part 6: 즉시 실행 — P1 구현안

### 6.1 Decision Tracker 템플릿

```markdown
# tracking/decisions/YYYY-MM-DD-TICKER-ACTION.md

## 메타데이터
- 날짜: 
- 종목: 
- 액션 유형: BUY / SELL / TRIM / ADD / HOLD

---

## 시스템 권고
**권고:** 
**확신도:** ⭐ / ⭐⭐ / ⭐⭐⭐
**핵심 근거:**
1. 
2. 
3. 

---

## Shawn 결정
**결정:** [ ] 수용 / [ ] 부분 수용 / [ ] 거부
**실제 행동:**
**Shawn 근거:**

---

## 추적
| 기간 | 가격 | 변동 |
|------|------|------|
| 결정 시점 | $ | — |
| +30d | $ | % |
| +90d | $ | % |
| +180d | $ | % |

---

## 사후 평가 (90d 후 작성)
**정확도:** 시스템 맞음 / Shawn 맞음 / 무승부
**교훈:**
```

### 6.2 Regime Sentinel 일일 체크 템플릿

```markdown
# daily/YYYY-MM-DD-regime.md

## Regime Sentinel Check
**시간:** YYYY-MM-DD HH:MM KST
**현재 레짐:** Risk-On / Neutral / Risk-Off (X%)

| 지표 | 현재값 | 임계치 | 변화 | 상태 |
|------|--------|--------|------|------|
| VIX | | >25 | | 🟢/🟡/🔴 |
| 2-10 Spread | | <0 | | 🟢/🟡/🔴 |
| HY Spread | | >400bp | | 🟢/🟡/🔴 |
| BTC 주간 | | <-15% | | 🟢/🟡/🔴 |
| DXY 월간 | | >+3% | | 🟢/🟡/🔴 |

**경고 수:** 0/5
**액션:** 없음 / 주의 / Macro 재판정 필요

---

## 전일 대비 변화
- VIX: 18.2 → 18.5 (+0.3)
- ...
```

### 6.3 EXPERTS.md 간소화 초안

별도 파일로 제안: `EXPERTS-V3-DRAFT.md`

---

## ICL Final Critic Pass — 전체 제안 검증

### "이 개선이 정말 Shawn의 목표 달성에 도움이 되는가?"

| 제안 | 목표 기여도 | 판정 |
|------|------------|------|
| Decision Tracker | 행동 개선 → 수익률 개선 | ✅ 직접 기여 |
| Regime Sentinel | 손실 방지 → 자본 보존 | ✅ 직접 기여 |
| 전문가 간소화 | 분석 속도 → 기회 포착 | ✅ 간접 기여 |
| Position Management | 이익 실현 → 복리 효과 | ✅ 직접 기여 |
| Event Playbook | 손실 방지 | ✅ 간접 기여 |
| Watchlist Alert | 기회 포착 | ✅ 직접 기여 |
| Correlation Dashboard | 리스크 관리 | 🟡 간접 기여 (P3 적정) |

### "시스템 복잡도를 높이는 대가 대비 실질 가치가 있는가?"

| 제안 | 복잡도 증가 | 가치 | 판정 |
|------|------------|------|------|
| Decision Tracker | 낮음 (템플릿 추가) | 높음 | ✅ |
| Regime Sentinel | 낮음 (5개 지표) | 높음 | ✅ |
| 전문가 간소화 | **감소** | 높음 | ✅✅ |
| Position Management | 중간 (규칙 6개) | 높음 | ✅ |
| Event Playbook | 중간 (15개 시나리오) | 중간 | 🟡 |
| Watchlist Alert | 낮음 (자동화) | 높음 | ✅ |
| Correlation Dashboard | 낮음 (월 1회) | 중간 | ✅ |

### "Shawn이 실행 가능한가?" (인지 비용)

| 제안 | Shawn 추가 작업 | 판정 |
|------|----------------|------|
| Decision Tracker | 결정 시 1분 기록 | ✅ 가능 |
| Regime Sentinel | 없음 (자동) | ✅ 가능 |
| 전문가 간소화 | 없음 | ✅ 가능 |
| Position Management | 규칙 숙지 | 🟡 협의 필요 |
| Event Playbook | 이벤트 시 참조 | ✅ 가능 |
| Watchlist Alert | 알림 확인만 | ✅ 가능 |
| Correlation Dashboard | 월 1회 리뷰 | ✅ 가능 |

---

## Conclusion

PLEDS v2.2는 **분석 시스템으로서 성숙**했다. 이제 다음 단계는 **"투자 파트너"로의 진화**다.

핵심 전환:
1. **일방향 → 양방향:** 보고서 전달이 아닌 대화와 토론
2. **분석 → 행동:** 권고에서 끝나지 않고 결정과 결과까지 추적
3. **복잡 → 단순:** 24명을 15명으로, 핵심에 집중
4. **반응 → 선제:** 레짐 변화를 미리 감지

**다음 스텝:**
1. 오늘: Decision Tracker 템플릿 생성, 첫 기록 시작
2. 이번 주: Regime Sentinel 일일 체크 추가
3. 다음 주: EXPERTS-V3 개정, Position Management 협의
4. 이번 달: Event Playbook, Watchlist Alert 구현
5. 다음 달: Correlation Dashboard, Q2 Prune 검토

---

**"좋은 분석은 좋은 투자의 필요조건이지, 충분조건이 아니다."**

— CRO

---

*Git commit: 2026-03-24-pleds-system-review*
*Status: Complete*
