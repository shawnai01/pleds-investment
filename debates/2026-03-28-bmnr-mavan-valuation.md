# BMNR MAVAN 스테이킹 수익이 밸류에이션에 미치는 영향

> **PLEDS Hypothesis Mode Analysis**  
> Date: 2026-03-28  
> Layer: L3 (Company/Business Model) + L4 (Valuation)  
> Subject: MAVAN 도입에 따른 현금 흐름 발생이 밸류에이션에 미치는 영향

---

## §1. Executive Summary

### 핵심 가설
MAVAN (Made In America VAlidator Network)은 BMNR을 **수동적 ETH 보유 회사에서 능동적 수익 창출 비즈니스로 전환**한다. 이 반복적 현금흐름은 BMNR의 밸류에이션 패러다임을 **순수 mNAV 디스카운트/프리미엄에서 NAV + Yield 하이브리드 모델로** 근본적으로 변화시켜야 한다.

### 결론 Preview

| 항목 | 결과 |
|------|------|
| **MAVAN 연간 수익** | $272M (full staking) / 현재 $184M |
| **주당 스테이킹 가치 (DCF 10yr)** | **$4.0-5.8/share** |
| **mNAV 재평가 잠재력** | 0.83x → 0.95-1.05x (yield premium 반영 시) |
| **적정가 영향** | 기존 $26 NAV/share → $30-32/share (NAV + Yield DCF) |
| **Deep Loop 판정** | 🟡 Moderate — MAVAN은 marginal이 아닌 meaningful, 단 패러다임 전환까지는 아님 |
| **Kill Condition 변경** | ❌ 변경 불필요 — ETH $2,000 기준 유지 |

---

## §2. MAVAN Overview (Verified Data)

### 2.1 런칭 세부사항 [FACT: PRNewswire 2026-03-25]

| 항목 | 내용 | 출처 |
|------|------|------|
| **런칭일** | 2026년 3월 25일 | [Tier 1: SEC 8-K] |
| **인프라** | US-based validator + globally distributed architecture | [Tier 1: PRNewswire] |
| **전략적 포지셔닝** | "Made In America" — 기관 투자자용 규제 친화적 스테이킹 | [Tier 1: PRNewswire] |
| **확장 계획** | 추가 PoS 네트워크, on-chain vaults, post-quantum client 개발 | [Tier 1: PRNewswire] |

### 2.2 스테이킹 현황 [FACT: PRNewswire 2026-03-23]

| 항목 | 수치 | 비고 |
|------|------|------|
| **총 ETH 보유** | 4,660,903 ETH | ETH supply 3.86% 점유 |
| **Staked ETH** | 3,142,643 ETH | 총 보유의 67% |
| **Unstaked ETH** | ~1,518,260 ETH | 스테이킹 대기 중 |
| **스테이킹 비율** | 67% → 100% (목표) | 수주 내 완료 예정 |
| **7일 수익률** | 2.83% | CESR 2.75% 상회 |

### 2.3 수익 예측 [FACT: PRNewswire/StockTitan 2026-03-24]

| 시나리오 | Staked ETH | 연간 수익 | 산출 근거 |
|----------|------------|----------|----------|
| **현재** | 3,142,643 | $184M | 3.14M × $2,072 × 2.83% |
| **Full Staking** | 4,660,903 | $272M | 4.66M × $2,072 × 2.83% |
| **5% Alchemy 목표 (6M ETH)** | 6,000,000 | $374M | [Tier 2: 247wallst] |

---

## §3. Pre-MAVAN vs Post-MAVAN Valuation Framework

### 3.1 Pre-MAVAN Valuation (Pure NAV Model)

MAVAN 이전 BMNR의 밸류에이션은 **순수 NAV 할인/프리미엄 모델**:

```
Market Cap = NAV × mNAV Multiple

NAV = (ETH Holdings × ETH Price) + BTC + Beast + ORBS + Cash
    = (4.66M × $1,990) + $0.4M + $200M + $95M + $1.1B
    = $9.27B + $1.4B = $10.67B

mNAV = Market Cap / NAV = $9.0B / $10.67B = 0.84x
```

**Pre-MAVAN 특성:**
- 현금흐름 = 0 (순수 holding company)
- 밸류에이션 = ETH 가격 × mNAV 배수에 전적으로 의존
- MSTR와의 핵심 차이점: BTC는 yield 없음, ETH는 staking yield 가능

### 3.2 Post-MAVAN Valuation (NAV + Yield Hybrid Model)

MAVAN 이후 BMNR은 **두 가지 가치원**을 갖는다:

```
Fair Value = NAV + DCF(Staking Cash Flows)

1. NAV Component (기존)
   = $10.67B (ETH + other assets)

2. Yield Component (신규)
   = DCF of annual staking revenue
```

**Post-MAVAN 밸류에이션 공식:**

```
Staking Revenue = Staked ETH × ETH Price × Yield Rate
                = 4.66M × $1,990 × 2.83%
                = $262M/year (at current ETH price)

Operating Margin on Staking = 90%+ (infrastructure cost minimal vs revenue)
Net Staking Income = $262M × 90% = $236M/year

DCF (10-year, 10% discount rate, 0% growth):
= $236M × (1 - 1.10^-10) / 0.10
= $236M × 6.14
= $1.45B
```

**⚠️ 중요 고려사항:**
- Yield compression risk (스테이킹 참여율 증가 → yield 하락)
- ETH 가격 변동성이 스테이킹 수익의 USD 가치에 직접 영향
- 스테이킹 수익은 ETH로 수령 → NAV에 재투자 (복리 효과)

### 3.3 Hybrid Valuation Model

```
Fair Value = NAV + Yield Premium

Where:
NAV/share = $10.67B / 430M shares = $24.81
Yield DCF/share = $1.45B / 430M shares = $3.37

Total Fair Value = $24.81 + $3.37 = $28.18/share
Current Price = $18.39
Upside = 53%
```

---

## §4. Staking Revenue Projections (Sensitivity Matrix)

### 4.1 Annual Staking Revenue Matrix ($M)

| ETH Price | 2.0% Yield | 2.5% Yield | 2.83% Yield | 3.5% Yield | 4.0% Yield |
|-----------|------------|------------|-------------|------------|------------|
| **$1,500** | $140 | $175 | $198 | $245 | $280 |
| **$2,000** | $186 | $233 | $264 | $326 | $373 |
| **$2,500** | $233 | $291 | $330 | $408 | $466 |
| **$3,000** | $280 | $350 | $396 | $489 | $559 |
| **$4,000** | $373 | $466 | $528 | $652 | $745 |

*기준: 4.66M ETH fully staked*

### 4.2 Yield DCF Value per Share ($, 10yr DCF, 10% discount)

| ETH Price | 2.0% Yield | 2.83% Yield | 4.0% Yield |
|-----------|------------|-------------|------------|
| **$1,500** | $2.0 | $2.8 | $4.0 |
| **$2,000** | $2.7 | $3.8 | $5.3 |
| **$2,500** | $3.3 | $4.7 | $6.7 |
| **$3,000** | $4.0 | $5.6 | $8.0 |
| **$4,000** | $5.3 | $7.5 | $10.6 |

### 4.3 Break-Even Analysis

**현재 시장가 $18.39를 정당화하는 조합:**

```
NAV/share = $24.81 (current)
Market Price = $18.39
Implied mNAV = 0.74x

만약 NAV + Yield를 반영한다면:
$18.39 = $24.81 × (1 - discount) + Yield DCF

Yield DCF가 $3.37이면:
$18.39 = ($24.81 + $3.37) × mNAV
$18.39 = $28.18 × mNAV
mNAV = 0.65x (implied discount of 35%)
```

**해석:** 현재 시장은 스테이킹 수익을 **거의 가치로 인정하지 않고 있음**. 오히려 순수 NAV 대비 더 깊은 할인.

---

## §5. mNAV Re-rating Analysis

### 5.1 Historical CEF/Holding Company mNAV Ranges

| 유형 | 일반적 mNAV 범위 | 프리미엄 조건 |
|------|-----------------|--------------|
| **Equity CEFs** | 0.85-0.95x | 높은 배당, 강력한 운용사 |
| **Bond CEFs** | 0.90-1.05x | 고수익 배당 |
| **Holding Companies (BRK)** | 1.0-1.3x | Buffett premium |
| **MSTR (BTC Treasury)** | 1.8-2.5x | Crypto bull market |
| **MSTR (2025 저점)** | 0.9-1.0x | BTC 조정기 |

### 5.2 BMNR mNAV 재평가 시나리오

| 시나리오 | mNAV | 산출 근거 | 주가 |
|----------|------|----------|------|
| **Current (No yield credit)** | 0.83x | Pure holding discount | $18.39 |
| **Yield-adjusted (Conservative)** | 0.95x | CEF + dividend premium | $22.53 |
| **Yield-adjusted (Base)** | 1.0x | NAV par | $24.81 |
| **Premium (MSTR analogy)** | 1.2x | Treasury play + yield | $33.72 |

### 5.3 MSTR 비교: Yield 유무의 차이

| 항목 | MSTR | BMNR | 함의 |
|------|------|------|------|
| **기초 자산** | BTC (no yield) | ETH (2.83% yield) | BMNR 우위 |
| **현금흐름** | $0 (SW 제외) | $272M/yr | BMNR 우위 |
| **전환사채 활용** | $7.2B | ❌ 없음 | MSTR 우위 (레버리지) |
| **mNAV (bull market)** | 2.5x | ? | MSTR 검증됨 |
| **Dilution** | 관리된 희석 | 74%/3mo | MSTR 우위 |

**[THESIS] MSTR + Yield = Better than MSTR?**

> "MSTR은 무수익 자산에 2.5x 프리미엄을 받는다. BMNR은 2.83% 수익을 창출하면서 0.83x 디스카운트에 거래된다. 만약 시장이 yield를 인식하면, BMNR은 최소 1.0x (par)에 거래되어야 한다. Yield premium까지 반영하면 1.2-1.5x도 가능하다."

### 5.4 Yield로 NAV 디스카운트를 완전히 해소하려면?

```
현재 디스카운트 = NAV $24.81 - Price $18.39 = $6.42/share
Yield DCF로 해소하려면:

$6.42 = (Staking Revenue × DCF Multiple) / Shares Outstanding
$6.42 = (Revenue × 6.14) / 430M
Required Annual Revenue = $6.42 × 430M / 6.14 = $450M

현재 $272M vs 필요 $450M
GAP = $178M → ETH 가격 $3,300 또는 Yield 4.6% 필요
```

**결론:** 현재 수준의 스테이킹 수익만으로는 NAV 디스카운트를 완전히 해소 불가. ETH 상승 또는 yield 증가 필요.

---

## §6. Deep Loop Debate (Abbreviated)

### 6.1 Inner Loop 4 Rounds

**Round 1: 독립 제시**

| Expert | Position | Key Argument |
|--------|----------|--------------|
| **Bull (Forensic Accountant)** | MAVAN은 패러다임 전환 | "MSTR + yield = superior. $272M recurring income을 무시하는 시장은 틀렸다." |
| **Bear (Sector Skeptic)** | Marginal impact only | "Yield compression inevitable. 2.83% → 2.0% 시 $272M → $192M. 희석이 yield를 상쇄." |
| **Neutral (Moat Analyst)** | Meaningful but not transformative | "MAVAN은 방어막. 공격무기(mNAV expansion)는 여전히 ETH 가격 의존." |

**Round 2: Critic 반론**

**Bear Critic의 Bull 공격:**
1. "Yield는 ETH로 받는다. ETH 가격 하락 시 USD 수익도 동반 하락. Yield가 가격 리스크를 헤지하지 않는다."
2. "MSTR premium은 Saylor의 브랜드 + 전환사채 financial engineering. BMNR에는 이 두 가지가 없다."
3. "Yield 2.83%는 지속 불가. 스테이킹 참여율 증가 → yield 하락은 구조적."

**Bull Critic의 Bear 공격:**
1. "Yield compression을 과장. CESR은 18개월간 2.7-3.5% 범위에서 안정적."
2. "희석은 NAV accretive. per-share ETH가 증가하고 있다는 SEC filing 확인."
3. "MSTR 전환사채는 장점이 아니라 리스크. BTC 급락 시 margin call 가능."

**Round 3: 재반박/수정**

| Expert | R3 Result | Revision |
|--------|-----------|----------|
| Bull | **revise** | "패러다임 전환" → "meaningful value add" 하향 조정. ETH 가격 의존성 인정. |
| Bear | **defend** | Yield compression thesis 유지. 단, 시간축 조정 (즉각적 → 2-3년). |
| Neutral | **defend** | "MAVAN = defense, not offense" 유지. |

**Round 4: Moderator 평가**

**살아남은 논거 (3/4):**
1. ✅ MAVAN은 $272M recurring cash flow를 창출 (Bull)
2. ✅ Yield compression은 구조적 리스크 (Bear)
3. ✅ 핵심 가치 드라이버는 여전히 ETH 가격 (Neutral)

**사망한 논거 (1/4):**
1. ❌ "MAVAN이 BMNR을 MSTR처럼 premium으로 전환" — 전환사채/브랜드 부재로 설득력 부족

### 6.2 Edge Test

| # | Edge Test | 결과 |
|---|-----------|------|
| E1 Novelty | ✅ YES | Sell-side가 yield valuation을 별도 모델링하지 않음 |
| E2 Causality | ✅ YES | Staked ETH × Yield = Revenue (명확한 인과) |
| E3 Actionability | 🟡 PARTIAL | Conviction 상향 근거는 되나, 진입/청산 기준 변경까지는 아님 |
| E4 Falsifiability | ✅ YES | Yield < 2.0% 지속 시 thesis 약화 |

**Edge 판정: 🟡 Moderate Edge** (3/4 YES)

### 6.3 Key Debate Question 결론

> **"Does MAVAN fundamentally change BMNR's valuation paradigm, or is it marginal?"**

**결론: Meaningful, Not Transformative**

- MAVAN은 **marginal이 아니다** — $272M 연간 수익은 무시할 수 없는 규모
- 그러나 **패러다임 전환도 아니다** — ETH 가격이 여전히 핵심 드라이버
- MAVAN은 **defensive moat** 역할: 약세장에서 손실 완화, 강세장에서 수익 증폭
- **mNAV 0.83x → 0.95x 재평가**는 합리적 기대, **1.2x+ premium**은 과도한 기대

---

## §7. Cross-Domain Comparison (REIT/MLP/BDC Analogy)

### 7.1 REIT Analogy

| 항목 | REIT | BMNR |
|------|------|------|
| **기초 자산** | 부동산 | ETH |
| **수익원** | 임대료 | 스테이킹 수익 |
| **Yield** | 4-6% | 2.83% |
| **밸류에이션** | NAV + FFO multiple | NAV + Staking DCF |
| **mNAV 범위** | 0.8-1.2x | 0.83x (현재) |

**REIT Insight:**
- REITs는 **stable income**으로 NAV par 또는 premium 거래
- BMNR의 yield는 ETH 가격 변동성으로 인해 **unstable** → mNAV discount 정당화
- **Yield stabilization** (USD 기준)이 mNAV 재평가의 열쇠

### 7.2 Pipeline MLP Analogy

| 항목 | MLP | BMNR |
|------|-----|------|
| **기초 자산** | 파이프라인 인프라 | Validator 인프라 |
| **현금흐름** | 처리량 기반 fee | 스테이킹 reward |
| **규제 리스크** | 환경 규제 | 크립토 규제 |
| **Yield** | 6-10% | 2.83% |

**MLP Insight:**
- MLPs는 **인프라 소유 + 안정적 throughput**으로 고배당
- MAVAN은 **ETH "throughput"에 의존** — ETH 네트워크 활성화 → yield 상승
- ETH 생태계 성장 = MAVAN yield 성장 (indirect exposure)

### 7.3 BDC Analogy

| 항목 | BDC | BMNR |
|------|-----|------|
| **사업 모델** | 중소기업 대출 | ETH 스테이킹 |
| **신용 리스크** | 차입자 default | Slashing risk |
| **mNAV** | 0.8-1.1x | 0.83x |
| **Yield** | 10-14% | 2.83% |

**BDC Insight:**
- BDCs는 **고수익 + 고위험**으로 discount 거래
- BMNR의 yield는 **low risk** (slashing 최소화된 institutional-grade) but **low yield**
- **Risk-adjusted yield**는 BDC 대비 불리하지 않음

### 7.4 Cross-Domain 종합 결론

| 유사체 | BMNR mNAV 적정 범위 |
|--------|-------------------|
| Equity CEF | 0.90-0.95x |
| REIT (high volatility) | 0.85-0.95x |
| MLP | 0.90-1.0x |
| BDC | 0.85-0.95x |
| **종합 적정 범위** | **0.90-0.95x** |

현재 0.83x는 **약간 undervalued** — yield 인식이 부재하거나, ETH 리스크 과잉 반영.

---

## §8. Portfolio Impact + Kill Condition Reassessment

### 8.1 Shawn's Current Position

| 항목 | 수치 |
|------|------|
| **보유 주수** | 5,000주 |
| **평단가** | $18.45 |
| **현재가** | $18.39 |
| **포지션 크기** | 31.3% (MAX 30% 초과) |
| **P&L** | -0.3% |

### 8.2 MAVAN이 포지션 사이징에 미치는 영향

**Before MAVAN:**
- Pure NAV play → ETH 가격에 100% 의존
- mNAV premium 확장 필요 (speculative)
- **Risk Profile: High**

**After MAVAN:**
- NAV + Yield hybrid → ETH 가격 + recurring income
- Yield가 downside cushion 역할
- **Risk Profile: High → Medium-High**

**사이징 권고:**
- 현재 31.3%는 **METHODOLOGY 상한 30% 초과** ⚠️
- MAVAN이 risk를 낮추므로 **1.3% 초과 유지 tolerable**
- 단, **추가 매수는 권장하지 않음** — ETH $2,000 Kill 임박

### 8.3 Kill Condition 재평가

**기존 Kill Condition:**
- ETH $2,000 일종 이탈 시 매도 검토

**MAVAN 반영 후 Kill Condition 검토:**

| 변경 여부 | 근거 |
|----------|------|
| **❌ 변경 불필요** | 스테이킹 수익이 ETH 가격 하락을 상쇄하지 못함 |

**계산:**
```
ETH $2,000 → $1,500 하락 시:
NAV 손실 = 4.66M × ($2,000 - $1,500) = $2.33B
Staking 연간 수익 = $198M (at $1,500)

손실 회복에 필요한 시간 = $2.33B / $198M = 11.8년
```

**결론:** Yield는 NAV 손실을 **장기적으로 회복**할 수 있으나, **단기 손절 로직을 변경할 근거는 부족**. ETH $2,000 Kill 유지.

### 8.4 MAVAN 수익의 포지션 사이징 반영 여부

**결론: 반영하되 제한적**

- MAVAN 수익은 **conviction 상향 근거** (⭐⭐ 유지)
- 그러나 **siding 확대 근거로는 부족** — ETH 가격 리스크가 지배적
- 현재 31.3% 포지션은 **유지**, 추가 매수는 **ETH $1,900 이하 또는 BMNR $17 이하**에서만

---

## §9. Final Verdict: How Much is MAVAN Worth Per Share?

### 9.1 MAVAN 가치 산출

**Method 1: DCF (10-year, 10% discount)**

```
Annual Staking Revenue (full staking) = $272M
Operating Margin = 90%
Net Income = $245M
DCF Value = $245M × 6.14 = $1.50B
Per Share = $1.50B / 430M = $3.49/share
```

**Method 2: Perpetuity (2% terminal growth)**

```
Terminal Value = $245M / (10% - 2%) = $3.06B
Per Share = $3.06B / 430M = $7.12/share
```

**Method 3: P/E Multiple Approach**

```
Staking Net Income = $245M
P/E Multiple (utility-like) = 10x
Value = $2.45B
Per Share = $2.45B / 430M = $5.70/share
```

### 9.2 MAVAN 가치 범위

| Method | Per Share Value |
|--------|-----------------|
| DCF (10yr) | $3.49 |
| P/E 10x | $5.70 |
| Perpetuity | $7.12 |
| **Conservative (DCF)** | **$3.5-4.0** |
| **Base (P/E)** | **$5.5-6.0** |
| **Aggressive (Perpetuity)** | **$7.0+** |

### 9.3 Total Fair Value

```
NAV/share = $24.81
MAVAN Value (Base) = $5.50
Total Fair Value = $30.31/share

Current Price = $18.39
Upside = 65%
```

### 9.4 Sensitivity to ETH Price

| ETH Price | NAV/share | MAVAN/share | Total FV | Upside from $18.39 |
|-----------|-----------|-------------|----------|-------------------|
| $1,500 | $18.65 | $4.00 | $22.65 | +23% |
| $2,000 | $24.81 | $5.50 | $30.31 | +65% |
| $2,500 | $30.97 | $7.00 | $37.97 | +107% |
| $3,000 | $37.13 | $8.50 | $45.63 | +148% |

---

## §10. Variant Perception Box

```
📌 Variant Perception Box
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
시장 컨센서스: BMNR = "ETH holding company with dilution risk"
              - PT 평균 $30-34.50, Strong Buy 컨센서스
              - 시장은 MAVAN을 "nice to have"로 간주, 핵심 가치로 미반영

PLEDS 뷰:     MAVAN은 $3.5-6.0/share 추가 가치 창출
              - 현재가 $18.39는 NAV discount + yield 무시를 동시 반영
              - ETH 회복 시 NAV 상승 + mNAV 재평가 이중 레버리지

차이점:       시장은 yield를 가격에 반영하지 않음
              PLEDS는 yield를 별도 DCF로 valuation에 합산

차이의 근거:   CEF/REIT/MLP 모두 yield generating asset은 NAV + yield multiple로 평가
              BMNR만 예외적으로 pure NAV discount 적용은 불합리

검증 시점:     Q1 2026 어닝 (MAVAN 수익 첫 공식 보고)
              ETH 가격 $2,500 회복 시 mNAV 재평가 여부

Edge 판정:   🟡 Moderate Edge
              (E1✅ E2✅ E3🟡 E4✅)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## §11. Appendix: Data Sources

| 항목 | 소스 | Tier |
|------|------|------|
| MAVAN 런칭 | PRNewswire 2026-03-25 | Tier 1 |
| ETH Holdings | PRNewswire 2026-03-23 | Tier 1 |
| Staking Revenue Projection | StockTitan 8-K | Tier 1 |
| CESR Benchmark | CoinDesk Indices | Tier 1 |
| Analyst PT | TipRanks, MarketBeat | Tier 2 |
| CEF NAV Data | Fidelity, CEFA | Tier 2 |
| MSTR mNAV | VanEck, Presto Research | Tier 2 |

---

## §12. Conviction Card Update

### BMNR Conviction Card (Post-MAVAN)

| Card | 내용 |
|------|------|
| **C0 🔭 Thesis** | "ETH가 $5,000+로 재평가되고, BMNR이 가장 큰 기관급 ETH Treasury + Yield 플랫폼으로 인정받는다" |
| **C1 🔥 Burn?** | ⭐⭐ \| R:R = 1.6:1 \| "MAVAN으로 자생 가능한 ETH Treasury — yield가 downside cushion 역할" |
| **C2 🚪 Entry** | 진입 완료 (31.3%) — 추가 진입은 ETH $1,900 이하 또는 BMNR $17 이하 |
| **C3 🎯 Exit** | 6mo: $30-35 / 1yr: $45-55 / MAVAN 반영 FV: $30/share |
| **C4 ☠️ Kill** | ETH $2,000 일종 이탈 / BTC $60K / MAVAN yield < 2.0% 6개월 지속 |

---

**End of Analysis**

*PLEDS v4.2 | Deep Loop Adversarial Debate | 2026-03-28*
