# PLEDS Methodology — 확률 결합 방법론

## 1. Layer별 확률 산출

각 Layer는 독립적으로 **방향성 확률**을 산출합니다:

| Layer | 산출물 | 스케일 |
|-------|--------|--------|
| L1 Macro | Regime 확률 (Risk-On / Neutral / Risk-Off) | 각 0-100% (합=100%) |
| L2 Sector | 산업별 매력도 스코어 | 1-10 |
| L3 Value Chain | 밸류체인 내 위치 적합도 | 1-10 |
| L4 Company | 기업 확신도 | 1-10 |
| L5 Chart | 기술적 타이밍 등급 | Strong Buy ~ Strong Sell (1-5) |

## 2. 전문가 토론 → 합의 프로세스

### Step 1: 개별 판정
각 전문가가 독립적으로 의견 제시 (anchoring bias 방지)

### Step 2: 토론
사회자가 이끄는 정반합 토론:
- **정(Thesis):** 가장 강한 Bull 논거
- **반(Antithesis):** 의무적 Bear Case (Forensic Accountant / Contrarian)
- **합(Synthesis):** 양측 논거를 통합한 확률적 판단

### Step 3: 투표
각 전문가가 최종 확률/등급 투표 → 가중 평균 (동일 가중)
**불일치 플래그:** 전문가 간 표준편차가 2 이상이면 "High Disagreement" 표시 → Allocator 주의

## 3. Layer 간 확률 결합

### 3.1 조건부 가중 곱셈

```
Final Score = w₁·P(Macro) × w₂·P(Sector) × w₃·P(ValueChain) × w₄·P(Company) × w₅·P(Chart)
```

**기본 가중치:**
| Layer | 가중치 | 근거 |
|-------|--------|------|
| Macro | 0.25 | 모든 배가 함께 오르내림 |
| Sector | 0.20 | 산업 선택이 종목 선택보다 중요 |
| Value Chain | 0.10 | 정성적 보완 |
| Company | 0.30 | 개별 기업이 최종 수익 결정 |
| Chart | 0.15 | 타이밍은 중요하나 과도 의존 금지 |

### 3.2 Regime-Adjusted 가중치
Macro Regime에 따라 가중치 동적 조정:

| Regime | Macro↑ | Company↑ | Chart↑ |
|--------|--------|----------|--------|
| Risk-On (강세) | 0.15 | 0.35 | 0.20 |
| Neutral | 0.25 | 0.30 | 0.15 |
| Risk-Off (약세) | 0.40 | 0.20 | 0.10 |

→ 약세장에서는 매크로가 모든 것을 지배, 강세장에서는 종목 선택이 핵심

## 4. 포지션 사이징 — Modified Kelly Criterion

```
Kelly % = (p × b - q) / b
  p = Final Score (승률)
  b = Expected Reward / Expected Risk (보상 배율)
  q = 1 - p

Half-Kelly = Kelly% / 2  (보수적 적용)
Max Position = 25% (단일 종목 상한)
Min Threshold = 0.10 (이 이하면 투자 안 함)
```

### 사이징 매트릭스

| Final Score | 확신도 | 포지션 % |
|-------------|--------|---------|
| 0.30+ | ⭐⭐⭐ 최고 | 15-25% |
| 0.20-0.30 | ⭐⭐ 높음 | 8-15% |
| 0.10-0.20 | ⭐ 보통 | 3-8% |
| <0.10 | 낮음 | 0% (관망) |

## 5. 시나리오 프레임워크

모든 투자 결정에 3가지 시나리오 수반:

### Bull Scenario (확률 X%)
- 전제 조건
- 목표가
- 트리거 이벤트

### Base Scenario (확률 Y%)
- 전제 조건
- 예상 범위
- 시간 프레임

### Bear Scenario (확률 Z%)
- 전제 조건
- 하방 목표
- **손절 트리거 (Hard Stop)**
- 최대 손실 허용폭

### 시나리오별 대응 계획
```
IF Bull 트리거 발동 → 포지션 유지/확대, 익절 라인 설정
IF Base 유지 → 포지션 유지, 다음 리뷰까지 대기
IF Bear 트리거 발동 → 즉시 손절/축소, 현금 확대
```

## 6. 성과 추적 (Track Record)

### 6.1 판정 기록
모든 토론 결과를 `debates/` 폴더에 저장:
- 날짜, 참여 전문가, 각 투표, 최종 판정
- 6개월 후 실제 결과와 비교

### 6.2 전문가 적중률
`db/expert-accuracy.json`에 각 전문가의:
- 방향 적중률
- 수익 기여도
- Brier Score (확률 정확도)
→ 적중률 높은 전문가의 가중치 점진적 상향

### 6.3 Layer 적중률
어느 Layer가 수익에 가장 기여하는지 추적
→ 가중치 연간 재조정

## 7. 리스크 관리 규칙 (Hard Rules)

1. **단일 종목 MAX 25%** (현재 BMNR 35%는 시스템 적용 시 재조정 검토)
2. **단일 테마 MAX 40%** (크립토 전체 = BMNR+CRCL+COIN = 50% → 재조정 검토)
3. **현금 최소 10%** (기회 포착용)
4. **Bear 시나리오 트리거 시 48시간 내 실행** (미루지 않기)
5. **매주 일요일 포트폴리오 리뷰** (드리프트 체크)
6. **모든 매수에 사전 손절 라인 설정** (진입 전 정의)
