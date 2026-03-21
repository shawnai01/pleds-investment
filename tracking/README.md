# PT (Prospective Tracking) — PLEDS 메타 시스템

> "과거 판단을 미래 시점에 복기하여, 시스템의 개선 시그널을 추출한다."

## 목적
PLEDS가 내리는 모든 판단을 기록하고, 실제 시장 결과와 대조하여 시스템의 체계적 편향과 개선점을 발견한다.

## 아키텍처
```
PT System
├── Recorder (기록) — PLEDS 분석 시 자동 기록
├── Tracker (추적) — 주간 시장 데이터 수집, Kill 체크
└── Analyzer (분석) — 분기별 개선 시그널 추출
```

## 폴더 구조
```
tracking/
├── README.md              ← 이 파일
├── judgments/              ← PLEDS 판단 기록 (분석마다 자동)
│   └── YYYY-MM-DD-TICKER.md
├── reviews/                ← Checkpoint 리뷰 (30d/90d/180d/1yr)
│   └── YYYY-MM-DD-TICKER-XXd.md
├── signals/                ← 분기별 Feedback Signal Report
│   └── YYYY-QX-feedback.md
└── accuracy.md             ← 누적 적중률 대시보드
```

## 운영 규칙
| 시점 | 행동 | 자동/수동 |
|------|------|----------|
| PLEDS 분석 실행 시 | judgments/ 에 기록 생성 | 자동 (Phase 8) |
| 주간 (일요일) | 전 종목 주가 수집, Kill/Catalyst 체크 | 자동 |
| 30d/90d/180d/1yr | Checkpoint 리뷰 | 자동 감지 |
| 분기 1회 | Feedback Signal Report → Shawn과 리뷰 | 반자동 |

## Judgment 기록 필수 항목
1. 인풋: Shawn의 질문/맥락
2. 판단 시점 데이터: 주가, VIX, 매크로 regime
3. 각 Layer 판단 (L1-L5) + Critic 반론 결과 (survive/revise/abandon)
4. Conviction Card (C1-C4)
5. 최종 Action
6. Checkpoints (30d/90d/180d/1yr 날짜)

## 분석 차원 (Analyzer)
1. **방향 적중률** — BUY 중 실제 상승 비율
2. **Layer별 기여도** — 어떤 Layer가 맞혔고 틀렸는가
3. **Critic 효과** — abandon된 논거가 실제로 틀렸는가
4. **시간축 정확도** — 목표가 vs 실제, 체계적 과대/과소 추정
5. **노이즈 필터링** — 30일(참고) → 90일(초기시그널) → 180일(확정)

## 개선 시그널 → 피드백 루프
- PT는 PLEDS를 관찰하는 시스템이지, 수정하는 시스템이 아님
- 발견한 시그널은 Shawn과 협의 후 METHODOLOGY.md에 반영
- 적중률 60% 미만 Layer → 가중치 재검토 트리거
- Critic 과잉 비율 40%+ → Critic 기준 완화 권고
