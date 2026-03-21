# PLEDS Audit — Reality Coherence Records

> "현실 인식 자체의 정합성을 점검한다."

## 목적
PLEDS 시스템이 현실과 괴리되지 않았는지 메타 레벨에서 추적하는 기록 저장소.

## 파일 규칙
- `YYYY-MM-reality-audit.md` — 월간 Reality Coherence Audit
- `YYYY-QQ-data-infra.md` — 분기별 데이터 인프라 감사

## 점검 항목 (주간, 일요일 리뷰)
1. **예측 vs 실제 괴리** — 30일 PLEDS 판정 vs 실제 결과
2. **Stale Thesis Detection** — 30일+ 업데이트 없는 conviction
3. **Echo Chamber Check** — Bull/Bear 편향도
4. **Model Drift** — 밸류에이션 전제와 현실 괴리

## 점검 항목 (월간)
5. **Blind Spot Scan** — "우리가 보지 못하는 리스크"

## 경고 트리거
- 적중률 60% 미만 → 시스템 가중치/절차 재검토
- Echo Chamber 80/20 이상 → 강제 Bear-First 리뷰
- Stale Thesis 3건+ → Conviction Journal 일괄 재검토
