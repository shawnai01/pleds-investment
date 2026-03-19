# 🔩 Bottleneck Thesis Scan #4: Nuclear Energy
**Date:** 2026-03-19  
**Analyst:** The Bottleneck Hunter (Goldratt + Munger)  
**Framework:** Constraint Chain Mapping → Constraint Owner → Conviction Card

---

## 1. 테마 정의

> "원자력 에너지가 AI 데이터센터 수요 등으로 10x 확장되려면 무엇이 막고 있는가?"

### 수요 측 드라이버
- **AI/데이터센터 전력 폭증**: 글로벌 데이터센터 전력 수요 ~50GW(2024) → 100-150GW(2030) [THESIS]
- **빅테크 원전 계약**: Microsoft-Three Mile Island(Constellation 재가동), Google-Kairos Power, Amazon-X Energy
- **탈탄소 기저부하**: 풍력/태양광은 간헐적 → 원전은 24/7 가동 (capacity factor ~93%)
- **정부 지원**: 미국 IRA 원전 생산세액공제(PTC), DOE $2.7B HALEU 투자(2026.1), 영국 £300M HALEU 지원

### 공급 측 현실
- [FACT] 글로벌 가동 원전: ~440기, 약 390GW
- [FACT] 건설중: ~60기 (대부분 중국, 인도, 러시아)
- [FACT] 미국: 93기 → 현재 ~93기 가동 (일부 재가동 포함)
- SMR: NuScale(NRC 첫 SMR 인증 획득, 2023), 그 외 대부분 2030년대 상용화 목표
- 기존 대형 원전 신규 건설: 10-15년 + $10-25B/기

---

## 2. Constraint Chain Mapping (순차적 병목 체인)

```
우라늄 채굴 → 전환(UF6) → 농축(SWU) → [HALEU 농축] → 핵연료 제조 
→ 원자로 설계/인허가 → 건설(인력/자재) → 그리드 연결 → 운영/유지보수
          ↓                    ↓
     폐기물 저장           냉각수/부지
```

### 2.1 우라늄 채굴/공급
- [FACT] 세계 우라늄 자원: 5.93M tU ($130/kg 이하, 2023 Red Book)
- [FACT] 연간 수요 ~60,000 tU vs 생산 ~58,000 tU (2024) — 근소한 적자
- [FACT] 카자흐스탄 43%, 캐나다 15%, 나미비아 11% (생산 기준)
- **병목 등급: 중간** — 자원 자체는 풍부하나, 신규 광산 개발 5-10년, 가격 $80-100/lb 이상에서 신규 공급 유인
- Cameco (CCJ): McArthur River/Cigar Lake 세계 최대급 고품위 광산 보유

### 2.2 전환 (UF6)
- 글로벌 전환 시설 제한적: Cameco(캐나다), Orano(프랑스), Rosatom(러시아), CNNC(중국)
- **병목 등급: 중상** — 전환 capacity 타이트, Cameco Port Hope 시설이 서방 핵심
- 2024-2025 전환 가격 급등 ($30→$60/kgU 수준) [미확인 — 정확한 최근 가격 확인 불가]

### 2.3 농축 (SWU) — ⚠️ 1차 병목 후보
- [FACT] 글로벌 농축 capacity (2025): ~62,900 천SWU/yr
  - Rosatom: 27,100 (43%) — **러시아 단일 최대**
  - Urenco: 17,900 (28%)
  - CNNC: 10,000 (16%)
  - Orano: 7,500 (12%)
- [FACT] 미국 러시아 우라늄 수입 금지법 (2024.5 제정) — 전환기 허용 후 단계적 금지
- **서방 농축 capacity = ~35,400 천SWU** (Rosatom, CNNC 제외)
- 수요 증가 시 서방 농축 capacity 부족 심화
- Orano: GBII 확장 +2.5M SWU 결정(2023), 미국 Oak Ridge 신규 시설 선정(2024.9)
- **병목 등급: 상 (1차 병목)** — 확장에 5-7년, 자본집약적, 기술 진입장벽 극도로 높음

### 2.4 HALEU 농축 — 🔴 최대 병목 (Critical Bottleneck)
- [FACT] HALEU (5-20% U-235): SMR/차세대 원자로의 ~2/3가 필요
- [FACT] 현재 상업적 HALEU 대규모 생산: **러시아 Tenex만 가능**
- [FACT] Centrus Energy (LEU): Piketon, Ohio 시범 캐스케이드에서 920kg 생산 (2023.10~2025 중반)
- [FACT] DOE $2.7B 10년 계약으로 국내 농축 확대 (2026.1)
- OKLO-Centrus JV: HALEU 서비스 합작 추진
- **병목 등급: 최상 (Primary Bottleneck)** 
  - 러시아 금지 → 서방 HALEU 공급 사실상 제로 (Centrus 시범 생산 제외)
  - 상업 규모 도달까지 3-5년 이상
  - SMR 전체 타임라인을 이 병목이 좌우

### 2.5 핵연료 제조
- Westinghouse (Cameco 자회사), Framatome (Orano), TVEL (Rosatom)
- HALEU 기반 연료 제조는 아직 R&D/파일럿 단계
- **병목 등급: 중** — HALEU 확보 후 2차 병목으로 부상 가능

### 2.6 원자로 설계/인허가 (NRC)
- [FACT] NuScale: NRC 최초 SMR 디자인 인증 (2023), 그러나 UAMPS 프로젝트 취소 후 루마니아로 선회
- OKLO: NRC에 Aurora 신청, 2024 한 차례 거부 후 재신청
- Kairos Power: Hermes 테스트 원자로 건설 허가 (2023), Google 계약
- X-Energy: Xe-100 설계, DOE ARDP 수혜
- **NRC 인허가 타임라인: 3-7년** (설계 인증 + 건설 허가 + 운영 허가)
- **병목 등급: 상** — NRC 인력 부족, 신기술 심사 프레임워크 미비, 정치적 의지는 있으나 제도적 속도 제한

### 2.7 건설 인력/전문 기술자
- 미국 원전 건설 경험 인력 대거 은퇴 (마지막 대규모 건설: Vogtle 3&4, 예산 2배 초과)
- [FACT] Vogtle 3&4: 당초 $14B → 최종 ~$35B, 7년 지연
- 핵급(nuclear-grade) 용접공, 콘크리트 전문가 극도로 부족
- **병목 등급: 상** — 해소 기간 5-10년, 교육/인증 체계 재건 필요

### 2.8 냉각수/부지
- 대형 원전은 대량 냉각수 필요 (해안/강변)
- SMR: 일부 설계 공랭식 가능 (Kairos 용융염, X-Energy 고온가스로)
- **병목 등급: 중하** — SMR가 이 병목을 완화

### 2.9 폐기물 처리/저장
- 미국: Yucca Mountain 정치적 교착, 사용후연료 현장 건식 저장
- 핀란드 Onkalo 유일한 영구 처분장 (운영 개시)
- **병목 등급: 중** — 기술적으로는 해결 가능하나 정치적 장벽

### 2.10 자본 조달
- 대형 원전: $10-25B/기, 건설 리스크 → 민간 자본 기피
- SMR: $1-3B/기 (이론적), 그러나 FOAK(First-of-a-Kind) 리스크 여전히 높음
- 빅테크 PPA/offtake 계약이 자본 조달 환경 극적 개선
- **병목 등급: 중** — 빅테크 계약이 이 병목을 빠르게 해소 중

---

## 3. 병목 분석 종합

### 🔴 1차 병목: HALEU 농축 (Critical Path)
| 항목 | 평가 |
|------|------|
| 현재 상태 | 러시아 외 상업적 공급 사실상 제로 |
| 해소 난이도 | 극도로 높음 (원심분리기 제조/설치/운영 기술, 안보 제약) |
| 해소 기간 | 3-7년 (Centrus 풀스케일 2028-2030, Orano 미국 신규 2030+) |
| 핵심 소유자 | **Centrus Energy (LEU)** — 유일한 미국 HALEU 생산자 |
| 파급 효과 | HALEU 없으면 SMR/차세대 원자로 연료 공급 불가 → 전체 원전 르네상스 지연 |

### 🟡 2차 병목: 서방 SWU 농축 전반 (기존 LEU 포함)
| 항목 | 평가 |
|------|------|
| 현재 상태 | Rosatom 43% 점유, 러시아 제재/금지 시 서방 용량 부족 |
| 해소 난이도 | 높음 (Urenco/Orano 확장 진행 중이나 느림) |
| 해소 기간 | 5-7년 |
| 핵심 소유자 | **Urenco** (비상장), **Orano** (프랑스 국영), **LEU** (SWU 중개+HALEU) |

### 🟡 3차 병목: NRC 인허가 + 건설 인력
| 항목 | 평가 |
|------|------|
| 해소 난이도 | 높음 (제도적/인적 자본 재건) |
| 해소 기간 | 5-10년 |
| 이 병목은 HALEU/농축 해결 후 표면화 예상 |

### 역사적 병목 사례 비교
| 사례 | 병목 | 결과 |
|------|------|------|
| 1970s 원전 붐 | 건설비 초과/TMI 사고 → 규제 강화 | 주문 취소 물결, 30년 정체 |
| 후쿠시마 (2011) | 안전 우려 → 정치적 셧다운 | 독일 탈원전, 일본 대거 정지, 우라늄 가격 폭락 |
| 2024-현재 | HALEU/농축 독점 → 러시아 의존 | 서방 공급망 재건 시작, Centrus 부상 |

---

## 4. Constraint Owner 식별 및 평가

### 4.1 주요 상장 기업 스크리닝

| 티커 | 기업 | 주가 | Mkt Cap | 병목 위치 | Constraint Premium |
|------|------|------|---------|----------|-------------------|
| **LEU** | Centrus Energy | $213.86 | $4.2B | 🔴 HALEU 유일 생산자 + SWU 중개 | ⭐⭐⭐ 극도로 높음 |
| **CCJ** | Cameco | $111.33 | $48.5B | 우라늄 채굴 + 전환 + Westinghouse | ⭐⭐ 높음 |
| **CEG** | Constellation Energy | $305.58 | $110.6B | 기존 원전 운영 (미국 최대 원전 fleet) | ⭐⭐ 높음 |
| **OKLO** | Oklo Inc. | $59.66 | $9.3B | SMR 개발 (Aurora, 사전매출) | ⭐ 내러티브 |
| **SMR** | NuScale Power | $12.05 | $3.8B | NRC 인증 SMR (유일), 프로젝트 리스크 | ⭐½ |
| **VST** | Vistra | $170.12 | [미확인] | 원전 운영 + 화력/재생 포트폴리오 | ⭐½ |
| **NNE** | NANO Nuclear | $25.07 | $1.3B | 마이크로리액터 + HALEU 연료 가공 | ⭐ 초기 |

### 4.2 Constraint Owner 심층 분석

#### **LEU (Centrus Energy) — 최대 병목 소유자** 🔴
- **포지션**: 미국 유일 HALEU 생산자, DOE $2.7B 계약 수혜
- **독점성**: HALEU 원심분리기 기술 보유 (American Centrifuge), NRC 라이선스
- **리스크**: 
  - 정부 의존도 극도로 높음 (DOE 계약 = 매출의 핵심)
  - 규모 확장 실행 리스크 (시범→상업 전환)
  - 경쟁: Orano 미국 진출 (Oak Ridge, 2030+)
  - 밸류에이션: P/E 54.8, 1년 수익률 +180% — 상당 부분 반영
- **Constraint Premium 평가**: 기술적 해자 + 정책적 독점 = 프리미엄 정당화, 그러나 52주 최고 $464 대비 54% 하락 — 단기 과열 해소 중
- [THESIS] HALEU가 SMR의 critical path인 한, LEU는 "삽을 파는 자"

#### **CCJ (Cameco) — 통합 공급자** 
- **포지션**: 세계 2위 우라늄 생산자 + 전환 + Westinghouse(원자로/연료) 수직통합
- **강점**: McArthur River 세계 최대 고품위 광산, 장기 계약 기반 안정 매출
- **밸류에이션**: P/E 112 — 원전 르네상스 기대 상당히 반영
- **이전 분석 재검증**: "가격 조건부" → 현재 $111 (52주 최저 $35, 최고 $135)
  - 우라늄 spot $80-90/lb 수준에서 안정적이나 $100+ 돌파 시 업사이드 제한적
  - Westinghouse 인수 완료로 밸류체인 확장은 긍정적
- [THESIS] CCJ는 "안전한 원전 베팅"이나 비대칭 기회는 제한적 — P/E 112가 이미 많은 것을 반영

#### **OKLO — 내러티브 vs 현실**
- **포지션**: Sam Altman 지원, Aurora 마이크로리액터, HALEU 연료 재활용 구상
- **현실 체크**:
  - [FACT] Pre-revenue, EPS -$0.56
  - [FACT] NRC 한 차례 거부 (2022), 재신청 진행 중
  - [FACT] Mkt Cap $9.3B — 매출 제로 기업치고 극도로 높음
  - Centrus JV는 긍정적이나 HALEU 자체 생산이 아닌 서비스 계약
- **이전 분석 재검증**: "내러티브 프리미엄 과다" → **재확인**
  - $9.3B 시가총액은 2030년대 매출 실현을 전제 — 실행 리스크 극도로 높음
  - 52주 고점 $193 → 현재 $59 (69% 하락) — 프리미엄 일부 소거되었으나 여전히 과도
- [THESIS] OKLO는 2030+의 옵션 가치, 현재 가격에서 Risk:Reward 불리

#### **CEG (Constellation Energy) — 기존 원전 Fleet 가치**
- **포지션**: 미국 최대 원전 운영사 (21GW+), Microsoft Three Mile Island 재가동 계약
- **강점**: 즉각적 전력 공급 가능 (신규 건설 불필요), 빅테크 PPA로 장기 매출 확보
- **밸류에이션**: Mkt Cap $110B, YTD -17.6% (조정 중)
- [THESIS] 기존 원전 Fleet 소유자는 "즉시 사용 가능한 기저부하" 병목의 소유자
  - 신규 원전 10-15년 걸리는 동안, 기존 fleet 가치 재평가
  - 그러나 $110B 시가총액이 이미 상당 부분 반영

#### **NuScale (SMR) — 유일 NRC 인증 SMR, 그러나...**
- UAMPS 프로젝트 취소, 루마니아로 선회
- 52주 고점 $57 → $12 (79% 하락) — 시장이 실행 리스크를 심각하게 재평가
- [THESIS] SMR의 "첫 주자" 프리미엄은 사라짐, FOAK 실행이 관건

---

## 5. Conviction Cards

---

### LEU (Centrus Energy) — Conviction Card

**C1 🔥 Burn?**  
⭐⭐½ | Risk:Reward = 1:2.5 | "미국 유일 HALEU 생산자, DOE $2.7B 계약, SMR 전체의 critical path를 소유"

**C2 🚪 Entry**  
- 현재 $213 — 52주 고점 $464 대비 54% 조정, 진입 고려 가능 구간
- 이상적 진입: $180-200 (추가 조정 시) 또는 DOE 계약 확대/Orano 대비 기술 우위 확인 시
- 트리거: Piketon 풀스케일 확장 승인 발표

**C3 🎯 Exit**  
- 6mo: $250-280 (HALEU 수요 가시화)
- 1yr: $300-350 (상업 규모 생산 마일스톤)
- 3yr: $500+ (HALEU 독점 프리미엄 본격 반영, SMR 상용화 시작)

**C4 ☠️ Kill**  
- Orano 미국 HALEU 시설 조기 가동 (독점 해소)
- DOE 계약 축소/취소
- HALEU 불필요 SMR 설계가 시장 주도권 장악
- 가격: $140 이하 (hard stop)
- 기한: 2028-06

**Bull (30%)**: HALEU 독점 3-5년 유지, SMR 상용화 가속, DOE 추가 계약 → $500+  
**Base (50%)**: 점진적 확장, 경쟁 출현에도 선점 우위 유지 → $280-350  
**Bear (20%)**: 규모 확장 실패, Orano/Urenco 조기 진입, SMR 지연 → $120-180

**"100배 똑똑한 Shawn이라면?"**  
LEU의 핵심은 "시간"이다. HALEU 독점 창이 3-5년인데, 그 사이 Orano가 얼마나 빨리 오는지가 관건. 미국 정부의 에너지 안보 의지가 지속되는 한 LEU는 보호받지만, 이것은 "정책 베팅"이기도 하다. 정권 교체 리스크를 반드시 고려. 현재 가격($213, P/E 55)은 합리적이나 "저렴"하지는 않다. 분할 진입이 현명.

---

### CCJ (Cameco) — Conviction Card

**C1 🔥 Burn?**  
⭐⭐ | Risk:Reward = 1:1.8 | "원전 밸류체인 수직통합 완성, 그러나 P/E 112가 많은 것을 반영"

**C2 🚪 Entry**  
- 현재 $111 — 합리적이나 흥분할 가격은 아님
- 이상적 진입: $90-100 (우라늄 spot 조정 시)
- 트리거: 우라늄 spot $100/lb 돌파 + 신규 장기 계약 발표

**C3 🎯 Exit**  
- 6mo: $120-130
- 1yr: $140-160 (우라늄 슈퍼사이클 확인 시)
- 3yr: $180-220

**C4 ☠️ Kill**  
- 우라늄 spot $60/lb 이하 장기 지속
- Westinghouse 통합 시너지 미실현
- 가격: $80 이하 (hard stop)

**Bull (25%)**: 우라늄 $150+/lb, 원전 르네상스 본격화 → $200+  
**Base (55%)**: 점진적 수요 증가, $80-100/lb 유지 → $130-160  
**Bear (20%)**: 원전 기대 후퇴, 우라늄 가격 하락 → $70-90

**"100배 똑똑한 Shawn이라면?"**  
CCJ는 "원전 인덱스"다. 나쁜 선택은 아니지만 비대칭 기회는 아니다. P/E 112는 완벽한 실행을 전제한 가격. 조정 시 소량 진입은 괜찮으나, 포트폴리오의 핵심 베팅으로는 LEU가 더 날카롭다.

---

### CEG (Constellation Energy) — Conviction Card

**C1 🔥 Burn?**  
⭐⭐ | Risk:Reward = 1:1.5 | "기존 원전 fleet = 즉시 사용 가능한 기저부하, 빅테크 PPA"

**C2 🚪 Entry**  
- 현재 $305 — YTD -17.6% 조정 중
- 이상적 진입: $260-280
- 트리거: 추가 빅테크 PPA 체결 발표

**C3 🎯 Exit**  
- 1yr: $380-420 (전력 가격 재평가)
- 3yr: $500+ (원전 fleet 희소성 프리미엄)

**C4 ☠️ Kill**  
- FERC/규제 기관 원전-데이터센터 직접 PPA 제한
- $220 이하 (hard stop)

**"100배 똑똑한 Shawn이라면?"**  
CEG는 "지금 당장 작동하는 원전"의 가치. SMR이 10년 걸리는 동안 CEG가 혜택. 그러나 $110B 시가총액 유틸리티가 2-3x 하기는 어렵다. 안정적이지만 비대칭은 아님.

---

### OKLO — Conviction Card

**C1 🔥 Burn?**  
⭐ | Risk:Reward = 1:5 (극도의 이진 결과) | "비전은 최고, 현실은 제로 매출 + NRC 리스크"

**C2 🚪 Entry**  
- 현재 $59 — 52주 고점 대비 69% 하락, 그러나 여전히 $9.3B (매출 0)
- 진입 조건: NRC 건설 허가 획득 확인 후 → 시장가 진입
- 또는 $25-35 (극단적 비관 시) 소량 옵션 진입

**C3 🎯 Exit**  
- NRC 승인 + 첫 상용 원자로 → $150+
- 3yr-5yr 관점

**C4 ☠️ Kill**  
- NRC 두 번째 거부
- 자금 소진 (현금 런웨이 확인 필요)
- $15 이하 (hard stop)

**"100배 똑똑한 Shawn이라면?"**  
OKLO에 $9.3B 지불? 아니다. NRC 승인이라는 바이너리 이벤트 전에는 프리미엄이 과하다. Sam Altman 후광 할인 필요. $25-35면 옵션으로 소량, 현재 가격은 패스.

---

## 6. 종합 판단

### 🏆 최우선 Constraint Owner: **LEU (Centrus Energy)**
- HALEU = 원전 르네상스의 #1 병목
- LEU = 미국 유일 HALEU 생산자 = 병목 소유자
- 시장이 인식하고 있으나 (1yr +180%), 독점 창의 기간을 과소평가할 가능성
- **비대칭 기회 존재 (C1 ⭐⭐½)**

### 💡 핵심 인사이트
1. **HALEU가 모든 것을 막고 있다**: SMR이 아무리 좋은 설계를 가져도 연료가 없으면 무용지물
2. **시간 = 해자**: Centrus의 HALEU 독점은 기술이 아닌 "시간"이 만든 해자. Orano 미국 시설 2030+ → 3-5년 독점 창
3. **기존 원전 Fleet (CEG, VST)이 중기 승자**: 신규 원전 10-15년 걸리는 동안 기존 fleet이 가장 빠른 공급 응답
4. **SMR 퓨어플레이(OKLO, NuScale)는 시기상조**: 기술 리스크 + 규제 리스크 + HALEU 공급 리스크 = 삼중 불확실성

### ⚠️ 주요 리스크/모니터링 변수
- DOE 정책 방향 (정권 교체 시 원전 지원 지속 여부)
- Orano 미국 HALEU 시설 타임라인
- 우라늄 spot 가격 ($100/lb 돌파 여부)
- NRC SMR 인허가 속도
- 러시아-서방 에너지 관계 변화
- 중국 원전 건설 속도 (글로벌 수급 영향)

---

*Disclaimer: This analysis is for PLEDS internal research purposes only. Not investment advice.*
*All [FACT] items sourced from World Nuclear Association, Yahoo Finance, DOE public data (2026-03-19 기준)*
*[미확인] items marked where precise recent data could not be independently verified*
