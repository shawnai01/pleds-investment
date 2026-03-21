# PLEDS Audit — 감사 절차 및 산출물

> "PLEDS가 세상과 연결되어 있는가?"  
> Reality Grounding Layer (METHODOLOGY §3)의 실행 기록을 보관한다.

---

## 폴더 구조

```
audit/
├── README.md                    # 이 파일 — 감사 절차 요약
├── data-source-health.md        # 데이터 소스 상태 (상시 업데이트)
├── YYYY-WW-weekly-audit.md      # 주간 감사 (매주 일요일)
├── YYYY-MM-reality-audit.md     # 월간 현실 감사 (매월 첫째 주)
└── YYYY-QQ-data-infra.md        # 분기 데이터 인프라 감사
```

---

## 1. Data Source Health Check (일일)

**목적:** 모든 데이터 소스의 활력 상태 점검

**점검 항목:**

| 소스 | 유형 | 점검 항목 | 주기 |
|------|------|----------|------|
| FRED API | 매크로 | API 응답 정상, 데이터 최신일 확인 | 매일 |
| Twelve Data | 가격/지표 | Rate limit 잔여, 데이터 갭 여부 | 매일 |
| Alpha Vantage | 백업 가격 | API 키 유효, 응답 지연 | 주간 |
| CoinGecko | 크립토 | 가격 일치, 온체인 지표 범위 | 매일 |
| Yahoo v8 | 백업 | 엔드포인트 변경 여부 | 주간 |
| SEC EDGAR | 공시 | 10-K/10-Q 파싱 정상 | 이벤트시 |
| web_search | 뉴스/정성 | 결과 품질, 편향 체크 | 수시 |

**장애 발생 시:**
1. `[DATA SOURCE ALERT]` 발행
2. 대체 소스 자동 전환
3. Shawn 알림

**산출물:** `data-source-health.md` (상시 업데이트)

---

## 2. Weekly Reality Audit (주간 — 매주 일요일)

**목적:** 시스템의 현실 인식 정합성 점검

**점검 항목:**

| # | 항목 | 내용 | 조치 |
|---|------|------|------|
| 1 | 예측 vs 실제 | 지난 7일 PLEDS 판정 vs 실제 시장 | 적중률 기록 |
| 2 | Stale Thesis | 30일+ 업데이트 없는 conviction | 재검토 플래그 |
| 3 | Echo Chamber | Bull/Bear 비율 80/20+ | 경고 발행 |
| 4 | Model Drift | 밸류에이션 전제 vs 현실 | 모델 조정 검토 |

**산출물 템플릿:**

```markdown
# Weekly Audit — YYYY-WW

## 1. 예측 vs 실제
| 날짜 | 종목 | 판정 | 실제 | 적중 |
|------|------|------|------|------|
| ... | ... | ... | ... | ✅/❌ |

**주간 적중률:** XX%

## 2. Stale Thesis Detection
- [ ] BMNR — 마지막 업데이트: YYYY-MM-DD (X일 전)
- ...

## 3. Echo Chamber Check
**최근 5건 분석 Bull/Bear 비율:** XX/YY
**경고:** [있음/없음]

## 4. Model Drift
**금리 전제:** X% (현실: Y%)
**성장률 전제:** X% (현실: Y%)
**괴리 여부:** [있음/없음]
```

---

## 3. Monthly Reality Audit (월간 — 매월 첫째 일요일)

**목적:** 시스템 메타 레벨 점검 + Blind Spot Scan

**점검 항목:**

| # | 항목 | 내용 |
|---|------|------|
| 1 | 30일 적중률 | 방향 적중률 계산. **60% 미만 시 시스템 재검토 트리거** |
| 2 | Blind Spot Scan | "우리가 보지 못하고 있는 리스크는?" (의무 실행) |
| 3 | 데이터 인프라 | 모든 소스 정상 작동, Rate limit 상태 |
| 4 | Information Source | 새로운 Tier 1-2 소스 발굴, 기존 소스 품질 평가 |

**Blind Spot Scan 질문 리스트:**
1. 현재 포트폴리오를 깨뜨릴 수 있는 시나리오는?
2. 우리가 과소평가하고 있는 매크로 리스크는?
3. 경쟁자/대안 기술 중 무시하고 있는 것은?
4. 시장이 알고 우리가 모르는 것은?
5. 우리의 정보 원천에 구조적 편향이 있는가?

**산출물:** `YYYY-MM-reality-audit.md`

---

## 4. Quarterly Data Infrastructure Audit (분기)

**목적:** 데이터 인프라 전면 점검

**점검 항목:**
1. 모든 API 키 유효성
2. Rate limit 사용 패턴 분석
3. 데이터 품질 (결측치, 이상치 비율)
4. 신규 소스 도입 필요성 검토
5. 비용 대비 효용 분석

**산출물:** `YYYY-QQ-data-infra.md`

---

## Information Source Tier 체계

전문가 토론에서 인용 시 **Tier 표기 의무**:

| Tier | 신뢰도 | 예시 | 태그 허용 |
|------|--------|------|----------|
| **Tier 1** | 최고 (1차 데이터) | SEC EDGAR, FRED, IR 페이지 | `[FACT]` |
| **Tier 2** | 높음 (전문 분석) | 학술 논문, 국제기구, 중앙은행 | `[FACT]` |
| **Tier 3** | 참고 (2차 해석) | Seeking Alpha, 팟캐스트, SNS | `[THESIS]` `[REFERENCE]` |
| **Tier 4** | 경계 (노이즈) | 익명 게시판, 루머 | **입력 금지** |

상세: `DATA-SOURCES.md` 참조

---

## 감사 실행 주체

- **일일 Health Check:** Data Auditor (자동화 목표)
- **주간 Audit:** PLEDS 시스템 (주간 Full Debate 중)
- **월간 Audit:** PLEDS 시스템 + Shawn 리뷰
- **분기 Audit:** Shawn + PLEDS 공동

---

## 트리거 조건

| 조건 | 트리거 액션 |
|------|------------|
| 데이터 소스 장애 | `[DATA SOURCE ALERT]` + 대체 소스 전환 |
| 주간 적중률 50% 미만 | Shawn 알림 + 원인 분석 |
| 월간 적중률 60% 미만 | 시스템 가중치/절차 재검토 |
| Stale Thesis 30일+ | 자동 재검토 플래그 |
| Echo Chamber 80/20+ | 강제 Bear-First 분석 |
