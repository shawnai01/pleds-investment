# PLEDS System Index

> 읽기 순서와 문서 관계 가이드
> v5.0 (2026-03-28): Graveyard, Editorial Delta, Portfolio History, INCUBATE, Angles 추가

## 📕 헌법 문서 (서브에이전트 필독)

| 순서 | 파일 | 역할 | 언제 읽는가 |
|------|------|------|-----------|
| **1** | `METHODOLOGY.md` | 분석 철학과 모든 프레임워크 정의 | 항상 첫 번째 |
| **2** | `EXPERTS.md` | 19명 전문가 페르소나 | METHODOLOGY 읽은 후 |
| **3** | `WORKFLOW.md` | 실행 절차 — 언제, 무엇을, 어떤 순서로 | 실행 직전 |
| **4** | `PORTFOLIO.md` | 현재 포트폴리오 현황 | 분석 시작 전 |
| **5** | `DATA-SOURCES.md` | API/데이터 소스 매핑 | 데이터 수집 시 |

## 🔄 실행 모드

| 모드 | 트리거 | 참조 |
|------|--------|------|
| **Standard Day** | 일일 크론, Event 트리거 없음 | WORKFLOW.md 상단 |
| **Event Day** | 7개 기계적 트리거 중 1개+ | WORKFLOW.md 상단 |
| **Hypothesis Mode** | Shawn 가설 기반 요청 | WORKFLOW.md "Hypothesis Mode" |
| **3-Agent Triangulation** | 포지션 사이징 변경 판단 | WORKFLOW.md "삼각검증" |
| **Bottleneck Scan** | 신규 테마 탐색 | WORKFLOW.md "Bottleneck Thesis Scan" |

## 📊 산출물 폴더

| 폴더 | 내용 |
|------|------|
| `daily/` | 일일 브리핑 |
| `debates/` | PLEDS 분석 보고서 |
| `conviction/` | 종목별 Conviction Journal |
| `tracking/judgments/` | PT 판정 기록 |
| `tracking/decisions/` | 포트폴리오 변경 기록 |
| `tracking/graveyard/` 🆕 | 기각된 테시스 묘지 + Editorial Delta |
| `tracking/PORTFOLIO-HISTORY.md` 🆕 | 포트폴리오 변천사 + 패턴 분석 |
| `memory/angles.md` 🆕 | Shawn's Angle — 비선형 연결 프레임 |
| `audit/` | 시스템 감사 보고서 |
| `db/` | 적중률 DB (JSON) |
| `data/` | 자동화 스크립트 + 수집 데이터 |

## ⚙️ 크론잡

| 잡 | 스케줄 | 모델 |
|----|--------|------|
| 일일 브리핑 | 매일 09:00 KST | Opus |
| 모닝 마켓 스캔 | 평일 09:00 KST | Sonnet |
| TIMEFOLIO ETF | 평일 09:30 KST | Sonnet |
| 주간 전략 리뷰 | 일요일 10:00 KST | Opus |
| GitHub 아카이빙 | 매일 23:00 KST | Sonnet |
