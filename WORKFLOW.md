# PLEDS Workflow — Step by Step

## 일일 브리핑 워크플로우 (매일 09:00 KST)

### Phase 0: 데이터 수집 (자동/크론, ~08:30)
```
수집 항목:
├── Macro: 전일 종가 — SPY, QQQ, DXY, TLT, GLD, USO, VIX, BTC, ETH
├── Macro: 금리 — FFR, 2Y, 10Y, 2-10 spread, HY spread
├── Macro: Fed/ECB 발언 스캔
├── Sector: 섹터 ETF 성과 (XLK, XLF, XLE, XLV, XLI, XLC, XLU, XLRE, XLB, XLP, XLY)
├── Company: 전일 어닝 서프라이즈, 내부자 거래, 13F 업데이트
├── Chart: 워치리스트 종목 가격/거래량
├── Crypto: BTC, ETH, MVRV, BTC.D, USDT.D, funding rates
└── News: 주요 헤드라인 10개
```

### Phase 1: Layer 1 — Macro Debate (~15분)

**참여:** The Machine, The Liquidity Hawk, The Cycle Sentinel, The Contrarian Catalyst, Macro Moderator

**절차:**
1. 각 전문가가 1-2문장으로 현재 뷰 제시 (독립적)
2. Contrarian이 컨센서스의 반대 논거 제시 (의무)
3. Moderator가 핵심 분기점(fork) 식별
4. 토론 (2-3 라운드)
5. **투표:** Regime (Risk-On / Neutral / Risk-Off) + 확률 %
6. **산출물:** `layers/L1-macro/regime-tracker.md` 업데이트

### Phase 2: Layer 2 — Sector Scan (~10분)

**참여:** The Disruptor, The Value Mapper, The Theme Hunter, Sector Moderator

**절차:**
1. Macro regime을 전달받고 산업 영향 분석
2. 각 전문가가 유망/역풍 산업 3개씩 제시
3. 비컨센서스 테마 1개 이상 의무 발굴 (Theme Hunter)
4. **투표:** 산업 매력도 Top 5 + 회피 산업
5. **산출물:** `layers/L2-sector/sector-rankings.md` 업데이트

### Phase 3: Layer 3 — Value Chain Analysis (~5분)

**참여:** The Strategist, The Network Thinker, Value Chain Moderator

**절차:**
1. Phase 2에서 선정된 유망 산업의 밸류체인 매핑
2. 가치 집중 노드 식별 (곡괭이, 플랫폼, 톨게이트)
3. **산출물:** `layers/L3-valuechain/frameworks.md` 업데이트

### Phase 4: Layer 4 — Company Deep Dive (~15분)

**참여:** The Compounder, The Catalyst Hunter, The Forensic Accountant, Company Moderator

**절차:**
1. 워치리스트 + 현재 보유 종목 리뷰
2. 신규 종목 후보 검토 (Phase 2-3에서 도출)
3. Forensic Accountant가 모든 매수 후보에 Bear Case 제시 (의무)
4. **투표:** 종목별 확신도 (1-10) + 적정가 + 액션
5. **산출물:** `layers/L4-company/watchlist.md` + `active-positions.md` 업데이트

### Phase 5: Layer 5 — Chart & Timing (~15분)

**참여:** The Momentum Master, The Accumulation Reader, The Wave Counter, The Quant Signal, Chart Moderator

**절차:**
1. Phase 4 통과 종목의 차트 분석
2. 크립토: BTC, ETH 파동 카운트 + MVRV/도미넌스 분석 (Wave Counter 전담)
3. 진입/청산 타이밍 토론
4. **투표:** 기술적 등급 + 진입 구간 + 손절 라인
5. **산출물:** `layers/L5-chart/signals.md` 업데이트

### Phase 6: Synthesis — Final Verdict (~10분)

**참여:** The Allocator (수석 투자 책임자)

**절차:**
1. 5개 Layer 결과 종합
2. 확률 가중 계산 (METHODOLOGY.md 공식)
3. 포지션 사이징 결정
4. 시나리오별 대응 계획 수립
5. **산출물:**
   - `synthesis/action-list.md` — 오늘의 투자 액션
   - `synthesis/probability-matrix.md` — Layer별 확률 종합
   - `daily/YYYY-MM-DD.md` — 일일 브리핑 전문

### Phase 7: Delivery (~09:00 KST)

**Shawn에게 텔레그램 브리핑 전송:**
```
🔎 PLEDS 일일 브리핑 [날짜]

📊 Macro Regime: [Risk-On/Neutral/Risk-Off] (확률 X%)
🏭 유망 산업: [Top 3]
📈 투자 액션:
  - [종목] [BUY/SELL/HOLD] [사이즈%] [근거 1줄]
  - ...
⚠️ 리스크 알림: [있으면]
🔗 상세: [파일 링크]
```

---

## 주간 Full Debate (매주 일요일 10:00 KST)

### 추가 절차:
1. **주간 성과 리뷰** — 포트폴리오 수익률 vs 벤치마크
2. **전문가 적중률 업데이트** — 지난주 판정 vs 실제
3. **신규 테마 브레인스토밍** — Theme Hunter 주도
4. **포지션 재조정 토론** — 드리프트 체크
5. **다음 주 핵심 이벤트 프리뷰** — 어닝, FOMC, CPI 등

---

## 이벤트 트리거 워크플로우 (수시)

| 트리거 | 대응 |
|--------|------|
| 보유 종목 ±5% 일일 변동 | Chart + Company 긴급 리뷰 |
| VIX 25+ 돌파 | Macro 긴급 Regime 재판정 |
| FOMC/CPI 발표 | Macro 즉시 업데이트 |
| 어닝 발표 (보유 종목) | Company + Chart 즉시 리뷰 |
| BTC ±10% 일일 변동 | Crypto 전문가 긴급 토론 |

---

## 파일럿 런 체크리스트 (내일 오전)

- [ ] 현재 포트폴리오 기준: BMNR 35%, CRCL 10%, COIN 5%, SGOV 30%, USD 20%
- [ ] Macro: 현 레짐 판정
- [ ] Sector: 크립토/핀테크/인프라 산업 평가
- [ ] Company: BMNR, CRCL, COIN 재평가 + 신규 후보
- [ ] Chart: BTC, ETH 파동 분석 + MVRV/도미넌스
- [ ] Synthesis: 포트폴리오 조정 제안
- [ ] 결과 텔레그램 전송
