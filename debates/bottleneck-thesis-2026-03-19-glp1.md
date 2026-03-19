# 🔩 Bottleneck Thesis #3: GLP-1 / Obesity
> Date: 2026-03-19 | Analyst: The Bottleneck Hunter (X-1)
> Framework: Theory of Constraints + Inversion Thinking

---

## Executive Summary

GLP-1 비만 치료제는 인류 역사상 가장 빠르게 성장하는 약물 카테고리다. 그러나 글로벌 비만 인구 10억+ 중 처방률 <5%에 불과하며, 30-50% 접근까지 **10x 확장**이 필요하다. **1차 병목은 펩타이드 API 제조 capacity**, **2차 병목은 가격/보험 접근성(Affordability)**이다. 진정한 비대칭 기회는 NVO/LLY가 아닌, 이들이 의존하는 **펩타이드 CDMO, 충진/디바이스 공급자, 원료 기업**에 있다.

**핵심 Constraint Owner**: Bachem (BANB.SW), PolyPeptide (PPGN.SW), West Pharmaceutical (WST), Thermo Fisher (TMO), Kindeva Drug Delivery

---

## Step 1: 테마 정의

### GLP-1 비만 치료 혁명이란?
GLP-1 수용체 작용제(semaglutide, tirzepatide 등)가 체중의 15-25%를 감량시키며, 비만을 "만성질환으로 약물 치료"하는 패러다임 전환.

### 현재 상태 (2026년 3월)
- [FACT] 글로벌 비만 인구: **10억+ 명** (WHO, 2024 발표 기준)
- [FACT] 현재 GLP-1 처방 환자: 전 세계 적격 인구 대비 **<5%** 추정
- [FACT] Novo Nordisk (NVO): Ozempic(당뇨), Wegovy(비만) — semaglutide 기반
- [FACT] Eli Lilly (LLY): Mounjaro(당뇨), Zepbound(비만) — tirzepatide (GLP-1/GIP 이중 작용)
- [FACT] 2024년 GLP-1 시장 규모: ~$50B+ (NVO+LLY 합산 매출 기준)
- [FACT] Novo Holdings가 Catalent을 ~$16.5B에 인수 → 제조 capacity 수직 통합
- [THESIS] 2030년 GLP-1 시장 전망: $100-150B (Goldman Sachs, Morgan Stanley 추정 기반)

### 목표 상태
적격 환자 30-50% 접근 → 현재 대비 **6-10x** 생산/유통/접근 확장 필요.

---

## Step 2: Constraint Chain Mapping

### 밸류체인 노드별 분석

| # | 밸류체인 노드 | 현재 Capacity | 10x 필요 Capacity | Gap (1-10) | 해소 속도 |
|---|---|---|---|---|---|
| 1 | **🧪 펩타이드 API 합성** | NVO/LLY 자체 + CDMO 풀가동 | 현재 대비 10x+ 필요 | **9** | **느림 (36-48개월)** |
| 2 | **💰 가격/보험 접근성** | 월 $1,000+ (미국), 보험 비적용 다수 | 월 $50-200 수준 필요 | **9** | **느림 (36-60개월)** |
| 3 | **🏭 충진/완제/디바이스** | 오토인젝터 펜 생산라인 한정 | 수십억 유닛/년 필요 | **7** | 중간 (24-36개월) |
| 4 | **🧊 콜드체인 유통** | 냉장 보관 필요 (2-8°C) | 글로벌 냉장 물류 확장 필요 | **6** | 중간 (24개월) |
| 5 | **👨‍⚕️ 처방 접근성** | 비만전문의 부족, 1차 의료 처방 저조 | 텔레메디신/디지털 처방 확대 | **5** | 빠름 (12-18개월) |
| 6 | **🧬 원료 (레진, 아미노산)** | 특수 아미노산/보호기 공급 제한적 | 원료 증산 필요 | **6** | 중간 (18-24개월) |
| 7 | **💊 경구제 전환** | Rybelsus(경구 semaglutide) 존재, 낮은 생체이용률(~1%) | 고용량 경구제 개발 중 | **5** | 중간 (24-36개월) |
| 8 | **📋 규제** | FDA/EMA 승인 완료, 글로벌 확대 중 | 신흥국 규제 승인 필요 | **4** | 중간 |
| 9 | **🔬 차세대 분자/바이오시밀러** | 바이오시밀러 2026-2028 출시 예정 | 가격 하락 촉매 | **3** | 진행 중 |

---

## Step 3: 병목 분석

### 🔴 1차 병목: 펩타이드 API 제조 Capacity (Gap: 9/10)

**근거:**
- [THESIS] GLP-1 약물의 핵심 원료인 semaglutide/tirzepatide는 **복잡한 펩타이드 분자**. 소분자 의약품과 달리 제조가 극도로 어렵고, 설비 구축에 **3-5년** 소요.
- [FACT] 펩타이드 제조 방법 2가지:
  - **SPPS (Solid-Phase Peptide Synthesis)**: 화학적 합성, 현재 주력. 비용 높고 스케일업 난이도 높음
  - **발효 (Recombinant Fermentation)**: NVO가 자체 기술 보유. 대량 생산에 유리하나 기술 이전 어려움
- [FACT] Novo Nordisk: 2024-2028 CAPEX $18B+ 투입하여 제조 확장 (Kalundborg 덴마크, 미국 NC 등)
- [FACT] Novo Holdings가 Catalent(CDMO)을 $16.5B에 인수 → 펩타이드 충진 capacity 수직 통합
- [FACT] Eli Lilly: 2024-2026 제조 CAPEX $9B+, Research Triangle Park(NC), Concord(NC), Ireland 확장
- [THESIS] 그럼에도 2026년 현재 공급은 수요의 **30-50% 수준**에 불과. Wegovy/Zepbound 공급 부족 지속 중.

**역사적 유사 사례:**
- **인슐린 보급 (1920s-1980s)**: 동물 인슐린 → 재조합 인슐린 전환에 수십 년. 제조 기술 전환이 보급의 핵심 병목이었음. GLP-1도 유사하게 SPPS → 발효/하이브리드 전환이 진행 중.
- **스타틴 대중화 (1987-2006)**: Mevacor 출시(1987) → 제네릭 atorvastatin(2011). 특허 만료 + 제네릭이 가격 하락과 대중화를 촉진. **GLP-1도 바이오시밀러 출시가 대중화의 촉매가 될 것**.

**해소 난이도:** 기술적(상) × 자본적(상) × 시간적(상)
- 펩타이드 합성 설비는 반도체 fab 수준의 복잡성과 규제 요건
- GMP 인증, 공정 검증에 2-3년 추가 소요
- **병목 지속 추정: 2028-2030년까지** (NVO/LLY capex 효과 발현)

---

### 🟡 2차 병목: 가격/보험 접근성 (Gap: 9/10)

**근거:**
- [FACT] 미국 Wegovy 정가: ~$1,350/월 (보험 미적용 시)
- [FACT] 미국 Zepbound 정가: ~$1,060/월
- [THESIS] 미국 비만 인구 ~1억 명 × $12,000/년 = **$1.2T/년** → 어떤 보험 시스템도 감당 불가
- [FACT] Medicare는 2024년까지 비만 치료 목적 GLP-1 미적용 (Anti-Obesity Medication Act 계류 중)
- [FACT] 민간 보험: 커버리지 확대 중이나, 사전 승인(Prior Authorization) + 체중 기준 등 장벽 존재
- [THESIS] 가격 하락 경로 3가지:
  1. **경구제**: 고용량 oral semaglutide Phase 3 완료, 주사 대비 제조 비용 ↓
  2. **바이오시밀러**: semaglutide 특허 2031-2032 만료 예상, 조기 합의 가능
  3. **경쟁**: 40+ 개 GLP-1/GIP/Glucagon 복합 분자 파이프라인 → 공급 과잉 시 가격 경쟁

**해소 시점:** 바이오시밀러 + 경구제 → **2028-2032년 가격 50-70% 하락 예상**

---

### 🟢 3차 병목: 충진/완제/디바이스 (Gap: 7/10)

- [FACT] GLP-1 주사제는 프리필드 펜(오토인젝터)으로 투여
- [FACT] 주요 디바이스 공급: Ypsomed (스위스), Owen Mumford (UK), SHL Medical (대만/스위스)
- [FACT] 프리필드 시린지/바이알 유리: Schott, Gerresheimer, West Pharmaceutical (WST)
- [THESIS] 디바이스 제조는 API 합성보다 해소 빠름 (기존 인슐린 디바이스 라인 전환 가능), 그러나 수요 급증 시 24개월 이상 리드타임

---

## Step 4: Constraint Owner 식별

### 🧪 1차 병목 소유자: 펩타이드 API 제조

| 기업 | 티커 | 역할 | 대체불가능성 (1-10) | 가격 전가력 | 병목 프리미엄 반영? |
|---|---|---|---|---|---|
| **Bachem** | **BANB.SW** (스위스) | 세계 최대 독립 펩타이드 CDMO | **9** | **매우 높음** | **부분 반영** |
| **PolyPeptide** | **PPGN.SW** (스위스) | 글로벌 #2 펩타이드 CDMO, GLP-1 대형 노출 | **8** | 높음 | **미반영** ⭐ |
| **Novo Nordisk** | **NVO** | 자체 발효 기반 API + Catalent 인수 | **10** (자체용) | 독점적 | 대부분 반영 |
| **Eli Lilly** | **LLY** | 자체 SPPS + CDMO 의존 | 9 (자체용) | 독점적 | 대부분 반영 |
| **Corden Pharma** | Private | 펩타이드 CDMO (유럽) | 7 | 높음 | N/A |

**비대칭 기회 분석:**

#### ⭐ 숨겨진 곡괭이 #1: Bachem (BANB.SW)
- [FACT] 스위스 상장, 세계 최대 독립 펩타이드 CDMO
- [FACT] GLP-1 관련 매출 비중 추정 50%+, 2024-2025 수주잔고(backlog) 사상 최대
- [THESIS] NVO/LLY가 자체 설비 확장해도, 나머지 40+ 개 GLP-1 파이프라인 기업은 **모두 Bachem 같은 CDMO에 의존**
- [THESIS] "GLP-1 골드러시에서 곡괭이를 파는 자" — 누가 이기든 Bachem은 수혜
- 리스크: 스위스 상장(유동성), NVO/LLY 내재화 가속 시 CDMO 물량 감소 가능

#### ⭐ 숨겨진 곡괭이 #2: West Pharmaceutical Services (WST)
- [FACT] NYSE 상장, 프리필드 시린지 및 약물 전달 시스템 글로벌 #1
- [FACT] 엘라스토머 컴포넌트(고무 마개, 플런저) 시장 과점
- [THESIS] 모든 GLP-1 주사제는 WST의 컴포넌트를 사용. API가 늘어나면 WST 수요는 비례 증가
- [THESIS] 시장은 WST를 "boring packaging company"로 인식. GLP-1 10x 확장의 필수 부품 공급자로는 미반영
- **Constraint Premium**: 대체불가능성 8 × 주사제 물량 비례 성장 = 높은 제약 프리미엄

#### 숨겨진 곡괭이 #3: Thermo Fisher Scientific (TMO)
- [FACT] NYSE 상장, 펩타이드 합성 원료(아미노산, 레진, 보호기) + 분석 장비 + CDMO 서비스(Patheon)
- [THESIS] 펩타이드 밸류체인의 "삽과 청바지" — 원료부터 분석까지 전 구간 커버
- 이미 대형주로 시장 인식, 그러나 GLP-1 특화 프리미엄은 미반영

---

### 💰 2차 병목 소유자: 가격/접근성 해소자

| 기업 | 티커 | 역할 | 대체불가능성 | 노트 |
|---|---|---|---|---|
| **Teva** | **TEVA** | 바이오시밀러 강자, GLP-1 바이오시밀러 추진 | 6 | 2028-2030 출시 시 수혜 |
| **Sandoz** | **SDZ** (스위스) | Novartis 분사, 바이오시밀러 전문 | 6 | GLP-1 바이오시밀러 파이프라인 |
| **Hims & Hers** | **HIMS** | 텔레헬스, 복합 GLP-1(compounding) 판매 중 | 4 | FDA 규제 리스크 높음, 공급 부족 해소 시 사업 모델 위험 |
| **Viking Therapeutics** | **VKTX** | 차세대 경구 GLP-1 (VK2735) | 7 | Phase 2 성공, 경구 전환 촉매 |
| **Structure Therapeutics** | **GPCR** | 소분자 경구 GLP-1 (GSBR-1290) | 7 | 소분자 = 제조 용이 + 가격 ↓↓ |

**비대칭 기회:**

#### ⭐ 소분자 경구 GLP-1: Structure Therapeutics (GPCR) / Viking (VKTX)
- [THESIS] **진정한 게임체인저**: 소분자 경구 GLP-1이 성공하면 펩타이드 제조 병목 자체가 무력화됨
- 소분자 = 기존 제약 공장에서 대량 생산 가능, 원가 $5-20/월 수준
- [THESIS] 이것이 "병목을 우회(bypass)하는" 경로. 스타틴이 심장 수술의 필요를 줄인 것처럼.
- 리스크: Phase 2-3 임상 실패 가능성, 효능이 주사제의 80-100% 도달하는지 미확인

---

### 🏭 디바이스/유통 (3차 수혜)

| 기업 | 티커 | 역할 |
|---|---|---|
| **West Pharmaceutical** | **WST** | 프리필드 시린지 컴포넌트, 엘라스토머 |
| **Becton Dickinson** | **BDX** | 주사 디바이스, 펜 니들 |
| **Ypsomed** | **YPSN.SW** | 오토인젝터 플랫폼 (NVO/LLY 공급) |
| **Gerresheimer** | **GXI.DE** | 유리 시린지/바이알 |

---

## Step 5: 투자 가설

### 가설 1: 펩타이드 CDMO = GLP-1 골드러시의 곡괭이

> [THESIS] "NVO/LLY가 이기든, Viking이 이기든, 40+ 파이프라인이 모두 펩타이드 CDMO에 의존한다. Bachem/PolyPeptide는 그 병목을 소유한다."

| 시나리오 | 확률 | 논거 |
|---|---|---|
| **Bull** | 25% | GLP-1 시장 $150B+ 도달, CDMO 수주잔고 5년+, 가격 전가력으로 마진 확장. BANB/PPGN 주가 3-5x |
| **Base** | 50% | GLP-1 시장 $100B, CDMO 꾸준한 성장이나 NVO/LLY 내재화 가속으로 독립 CDMO 성장률 제한. 2x |
| **Bear** | 25% | 소분자 경구 GLP-1 성공 → 펩타이드 수요 피크아웃, CDMO 과잉 설비. 주가 -30-50% |

### 가설 2: West Pharmaceutical (WST) = 모든 주사제의 필수 부품

> [THESIS] "GLP-1이 인슐린처럼 만성질환 약이 되면, 수십억 개의 프리필드 펜이 필요. 모든 펜에 WST 부품이 들어간다."

| 시나리오 | 확률 | 논거 |
|---|---|---|
| **Bull** | 25% | GLP-1 + 기타 펩타이드 바이오 약물 10x 성장, WST 매출 CAGR 15%+ 달성 |
| **Base** | 50% | GLP-1 성장 지속, WST 안정적 고성장 (CAGR 8-12%) |
| **Bear** | 25% | 경구제 전환 가속 → 주사 디바이스 수요 피크아웃 |

### 가설 3: 소분자 경구 GLP-1 = 병목 우회(Bypass) 전략

> [THESIS] "병목을 소유하는 것이 최선이지만, 병목을 우회하는 자가 궁극의 승자. 소분자 경구 GLP-1은 펩타이드 제조 + 콜드체인 + 디바이스 병목을 한 번에 제거한다."

| 시나리오 | 확률 | 논거 |
|---|---|---|
| **Bull** | 20% | Structure/Viking 경구제 Phase 3 성공 + FDA 승인, 월 $50 가격대. GLP-1 접근 인구 5x 확대, 해당 기업 주가 10x+ |
| **Base** | 40% | 경구제 부분 성공, 주사제 대비 효능 70-80%. 보조적 역할로 시장 공존 |
| **Bear** | 40% | 경구 GLP-1 임상 실패 또는 효능 부족, 주사제 패러다임 유지 |

---

### 🧠 "100배 똑똑한 Shawn이라면?"

1. **NVO/LLY는 이미 "컨센서스 롱"** — 시장이 이미 GLP-1 성장을 가격에 반영. 여기서 비대칭은 제한적. P/E 30-40x 수준에서 실망은 하방, 기대 충족은 이미 가격에 포함.

2. **CDMO(Bachem)를 "GLP-1 인프라 롱"으로 검토** — 스위스 상장이 허들이지만, 누가 이기든 수혜받는 구조. ADR 또는 해외 브로커 경유.

3. **WST를 "보험성 곡괭이"로 소량 포지션** — 이미 미국 상장, 유동성 좋음. GLP-1 외에도 모든 바이오/주사제 성장 수혜. "지루하지만 필수적인" 기업.

4. **Structure Therapeutics (GPCR)를 "콜옵션"으로 관찰** — 소분자 경구 GLP-1이 성공하면 게임 체인지. 실패하면 0에 수렴. 전형적 비대칭 바이오 베팅.

5. **HIMS는 피하라** — Compounding GLP-1은 FDA 단속 + 공급 부족 해소 시 사업 모델 붕괴. 구조적으로 병목을 소유하지 않고, 병목의 틈새에서 임시 수혜받는 구조.

6. **모니터링 트리거**:
   - NVO/LLY 분기 실적: 제조 capacity 가이던스, 대기자 명단 추이
   - Oral semaglutide 고용량 Phase 3 결과 (NVO)
   - Structure Therapeutics (GPCR) Phase 2b/3 데이터
   - Medicare 비만약 커버리지 법안 (Anti-Obesity Medication Act)
   - Semaglutide 바이오시밀러 첫 FDA 승인 시점
   - Bachem/PolyPeptide 분기 수주잔고(backlog) 추이

---

## Constraint Chain 요약 다이어그램

```
GLP-1 비만 치료 10x 보급
        │
        ▼
[1차 병목] 🧪 펩타이드 API 제조 ◄── Bachem, PolyPeptide, NVO/LLY 자체
        │  (SPPS/발효 설비, GMP 인증, 3-5년 구축)
        │  해소 예상: 2028-2030
        ▼
[2차 병목] 💰 가격/보험 접근성 ◄── 바이오시밀러(Teva, Sandoz), 경구제(GPCR, VKTX), 정책
        │  (월 $1,000+ → $50-200 필요)
        │  해소 예상: 2029-2032
        ▼
[3차 병목] 🏭 디바이스/충진/콜드체인 ◄── WST, BDX, Ypsomed
        │  (프리필드 펜, 냉장 유통)
        │  해소 예상: 2027-2028
        ▼
[우회 경로] 💊 소분자 경구 GLP-1 ◄── Structure(GPCR), Viking(VKTX)
        │  (병목 1+2+3 동시 우회)
        │  실현 시점: 2028-2030 (임상 성공 시)
        ▼
  🚀 적격 환자 30-50% 접근 달성
```

---

## 핵심 비대칭 기회 순위

| 순위 | 기업 | 티커 | 논리 | 리스크 | 비대칭 등급 |
|---|---|---|---|---|---|
| 1 | **Bachem** | BANB.SW | 펩타이드 CDMO 독점, 누가 이기든 수혜 | 스위스 상장, 소분자 전환 리스크 | ⭐⭐⭐ |
| 2 | **Structure Therapeutics** | GPCR | 병목 우회자, 성공 시 게임체인지 | Phase 2 바이오, 고위험 | ⭐⭐⭐ |
| 3 | **West Pharmaceutical** | WST | 모든 주사제의 필수 부품, 지루한 독점 | 경구제 전환 시 성장 둔화 | ⭐⭐ |
| 4 | **PolyPeptide** | PPGN.SW | CDMO #2, 턴어라운드 가능 | 스위스 상장, Bachem 대비 열위 | ⭐⭐ |
| 5 | **Viking Therapeutics** | VKTX | 경구+주사 GLP-1, 인수 타겟 | 임상 리스크 | ⭐⭐ |

---

## Risk & Caveats

1. **소분자 경구 GLP-1 성공 시 펩타이드 CDMO 투자 테시스 무력화** — 가장 큰 리스크. Bachem/PolyPeptide 포지션과 GPCR/VKTX 포지션은 **내추럴 헤지** 관계.
2. **NVO/LLY 내재화 가속** — Catalent 인수처럼 대형사가 CDMO를 흡수하면 독립 CDMO 물량 감소
3. **GLP-1 안전성 이슈** — 장기 부작용 발견 시 시장 전체 위축 (갑상선암, 근육 감소 등 모니터링)
4. **규제 리스크** — FDA의 compounding 단속, Medicare 커버리지 지연
5. [미확인] Bachem/PolyPeptide의 정확한 GLP-1 매출 비중 — IR 확인 필요
6. [미확인] Structure Therapeutics Phase 2b 최종 데이터 — 공개 대기 중
7. [미확인] Semaglutide 특허 정확한 만료 일정 — 복수 특허로 구성, 2031-2036 범위 추정

---

## 데이터 소스

- WHO: 글로벌 비만 인구 10억+ (2024 발표)
- Wikipedia: Semaglutide, GLP-1 receptor agonist 문서
- Novo Holdings/Catalent 인수: $16.5B (공개 자료)
- PolyPeptide Group 공식 사이트: 펩타이드 CDMO, GLP-1 노출
- West Pharmaceutical Services: NYSE WST 공개 자료
- Novo Nordisk/Eli Lilly CAPEX 계획: 연간 보고서 및 IR 프레젠테이션 기반 [미확인 — 정확 수치 교차검증 필요]

---

*Generated by PLEDS Bottleneck Hunter (X-1) | 2026-03-19*
