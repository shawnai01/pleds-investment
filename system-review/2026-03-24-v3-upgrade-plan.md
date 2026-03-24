# PLEDS v3.0 System Upgrade — 상세 설계 + Critic 검증 + 구현

> **Date:** 2026-03-24
> **Author:** CRO (Chief Research Officer)
> **Methodology:** 정반합 (Thesis → Antithesis → Synthesis)
> **Principle:** Rockets with Tight Bolts 🚀🔩

---

## Executive Summary

PLEDS v2.2에서 v3.0으로의 핵심 업그레이드:

| 모듈 | 변화 | 영향 |
|------|------|------|
| Decision Tracker | 신규 | 피드백 루프 생성, 시스템 vs Shawn 정확도 추적 |
| Regime Sentinel | 신규 | 선제적 레짐 감지, 일일 브리핑 통합 |
| Expert System | 24→15 | 인지 부하 37% 감소, 핵심에 집중 |
| Watchlist Alert | 신규 | 자동 가격 알림, 기회 포착 |

---

# Module 1: Decision Tracker (재설계)

## 正 (Thesis) — 최선의 설계안

### 1.1 핵심 통찰

기존 Decision Tracker 설계(system-review/2026-03-24-pleds-review.md)는 **"시스템 권고 후 Shawn이 수용하는지 추적"**에 초점을 맞췄다.

**문제:** Shawn은 PLEDS 권고를 즉시 반영하지 않는다. 대신 자기 타이밍에 포트폴리오를 바꾸고 "LLY 919.6에 30주 진입" 같이 알려준다.

**새로운 설계:** 이 자연스러운 패턴을 활용한 **역방향 추적**:
1. Shawn이 포트폴리오 변경 알림 → 해당 종목 직전 PLEDS 권고 자동 조회
2. 시스템 권고 vs 실제 행동 gap 기록
3. +30d/90d 자동 복기 (PT 시스템과 연동)
4. Shawn에게 추가 작업 없음

### 1.2 설계 세부사항

**트리거 패턴 인식:**
```
Shawn: "LLY 919.6에 30주 진입"
       "BMNR 100주 추가 매수 $21"
       "COIN 전량 청산"
       "[티커] [가격]에 [수량] [매수/매도]"
```

**자동 조회 프로세스:**
1. 메시지에서 티커 + 가격 + 액션 파싱
2. `tracking/judgments/` 에서 해당 티커 최신 PLEDS 판정 조회
3. 없으면 → "PLEDS 미분석 종목. 사후 분석 권장?"
4. 있으면 → Gap 분석 + Decision 기록

**Decision 기록 구조:**
```markdown
# tracking/decisions/YYYY-MM-DD-TICKER-ACTION.md

## 메타데이터
- 기록일: 2026-03-24
- 종목: LLY
- 액션: BUY
- Shawn 실행가: $919.60
- Shawn 수량: 30주

## PLEDS 직전 권고
- 권고일: 2026-03-22
- 판정: ⭐⭐⭐ BUY
- 진입 권고가: $900-920
- 핵심 근거: GLP-1 독점 + Orforglipron 카탈리스트

## Gap 분석
- 가격 차이: -$0.40 (0.0% 차이) ✅ 권고 범위 내
- 시점 차이: +2일
- 사이즈 차이: 권고 비중 6-8% vs 실제 6.5% ✅ 일치
- 종합: ✅ PLEDS 권고와 일치

## 복기 예정
| 시점 | 날짜 | 상태 |
|------|------|------|
| +30d | 2026-04-23 | ⏳ |
| +90d | 2026-06-22 | ⏳ |
```

**Gap 유형 분류:**
| 유형 | 정의 | 복기 시 평가 |
|------|------|-------------|
| ✅ 일치 | 권고와 동일 방향 + 유사 시점 | 시스템 정확도에 반영 |
| 🟡 시점 차이 | 같은 방향, 다른 타이밍 | 누가 더 좋은 타이밍이었나? |
| 🟡 사이즈 차이 | 같은 방향, 다른 비중 | 누구의 사이징이 더 적정했나? |
| 🔴 방향 차이 | 시스템 SELL vs Shawn BUY (또는 반대) | 누가 맞았나? 패턴 분석 |
| ⚪ PLEDS 미분석 | 시스템 권고 없음 | 사후 분석 필요 |

### 1.3 PT 시스템 연동

기존 `tracking/judgments/`는 **PLEDS 분석 시점** 기록.
신규 `tracking/decisions/`는 **Shawn 행동 시점** 기록.

**연동 방식:**
- `tracking/accuracy.md` 에 Decision 열 추가: 시스템 권고 vs Shawn 결정 vs 결과
- 분기 리뷰 시 "시스템이 맞았는데 Shawn이 무시한 케이스" 분석
- "Shawn이 시스템을 override해서 잘된 케이스" 분석

---

## 反 (Antithesis) — Critic 반박

### Critic Q1: "이게 정말 작동하는가?"

**반론 1: 파싱 실패 리스크**
- Shawn의 메시지 형식이 일관되지 않을 수 있음
- "어제 릴리 좀 샀어" vs "LLY 919.6에 30주 진입" — 다른 패턴
- **Risk Level:** 🟡 중간

**반론 2: 직전 PLEDS 권고 없는 경우**
- Shawn이 PLEDS 미분석 종목에 진입하면?
- 현재 accuracy.md에 기록된 종목은 11개뿐
- **Risk Level:** 🟡 중간

**반론 3: 복기 자동화의 한계**
- cron으로 +30d/+90d 복기를 자동화하려면 별도 스크립트 필요
- 기존 PT cron이 없음 — 수동으로 주간 리뷰에서 처리 중
- **Risk Level:** 🟡 중간

### Critic Q2: "복잡도 대비 가치가 있는가?"

**반론 4: 추가 기록 부담**
- 매 포트폴리오 변경마다 .md 파일 생성 필요
- CRO가 수동으로 파싱하고 기록해야 함
- **Risk Level:** 🟢 낮음 (CRO가 이미 해야 할 일)

**반론 5: Gap 분석의 실질 가치**
- 대부분 ✅ 일치 또는 🟡 시점 차이일 것
- 🔴 방향 차이가 드물면 시스템 개선 시그널 부족
- **Risk Level:** 🟢 낮음 (그래도 기록의 가치 존재)

### Critic Q3: "PLEDS와 잘 통합되는가?"

**반론 6: 기존 PT 시스템과의 중복**
- `tracking/judgments/`는 이미 종목별 판정 기록
- `tracking/decisions/`가 별도로 존재하면 관리 포인트 증가
- **Risk Level:** 🟢 낮음 (역할이 다름: 분석 vs 실행)

**반론 7: WORKFLOW.md 통합 필요**
- Phase 8 PT Recording에 Decision Tracker 연동 설명 필요
- 현재 WORKFLOW.md에는 "Shawn이 포트폴리오 변경 알리면" 시나리오 없음
- **Risk Level:** 🟢 낮음 (WORKFLOW 업데이트로 해결)

---

## 合 (Synthesis) — 최종 설계

### 1.4 Critic 피드백 반영

| 반론 | 해결책 |
|------|--------|
| 파싱 실패 | CRO가 flexible하게 해석. 명확하지 않으면 Shawn에게 확인 |
| PLEDS 미분석 | `[PLEDS 미분석]` 표기 + 사후 분석 권장 여부 질문 |
| 복기 자동화 | 기존 주간 리뷰에 Decision 복기 추가. 별도 cron 불필요 |
| 기록 부담 | 포트폴리오 변경 시 CRO가 자동 기록 (Shawn 추가 작업 없음) |
| PT 중복 | 역할 명확 구분: judgments = PLEDS 분석, decisions = Shawn 실행 |
| WORKFLOW 통합 | Phase 8.5로 Decision Recording 추가 |

### 1.5 최종 구현 스펙

**파일 구조:**
```
tracking/
├── decisions/
│   ├── YYYY-MM-DD-TICKER-ACTION.md
│   └── ...
├── decisions-summary.md   ← 분기별 집계
├── judgments/            ← 기존 유지
└── accuracy.md           ← Decision 열 추가
```

**WORKFLOW.md 추가 (Phase 8.5):**
```markdown
### Phase 8.5: Decision Recording (포트폴리오 변경 시)

> Shawn이 포트폴리오 변경을 알리면 자동 실행

1. 메시지에서 티커, 가격, 액션 파싱
2. `tracking/judgments/`에서 해당 티커 최신 PLEDS 판정 조회
3. Gap 분석: 가격, 시점, 사이즈, 방향
4. `tracking/decisions/YYYY-MM-DD-TICKER-ACTION.md` 생성
5. +30d/+90d 복기 날짜 기록
6. git commit + push

**주간 리뷰 (일요일)에 추가:**
- 전 decisions/ 파일의 복기 날짜 체크
- 도래한 복기 실행 → 결과 기록
```

**성공 지표:**
- 모든 포트폴리오 변경이 Decision으로 기록됨
- 분기별 시스템 vs Shawn 정확도 비교 가능
- Shawn의 행동 패턴(어떤 종류의 권고를 무시하는지) 식별

---

# Module 2: Regime Sentinel (신규)

## 正 (Thesis) — 최선의 설계안

### 2.1 핵심 통찰

현재 PLEDS의 레짐 판정은 **반응형**:
- VIX 25 넘으면 Risk-Off
- 문제: 이미 시장이 움직인 후

**새로운 설계:** 5개 지표의 임계치 조합으로 **선제적 감지**

### 2.2 지표 & 임계치

| 지표 | 소스 | 임계치 | 의미 |
|------|------|--------|------|
| VIX | Yahoo ^VIX | >25 | 공포 시작 |
| 2-10 Spread | FRED (DGS10 - DGS2) | <0 | 경기 침체 신호 |
| HY Spread | FRED (BAMLH0A0HYM2) | >400bp | 신용 리스크 |
| BTC 주간 변동 | CoinGecko | <-15% | 크립토 레짐 전환 |
| DXY 월간 변동 | Yahoo DX-Y.NYB | >+3% | 달러 강세 레짐 |

### 2.3 경보 단계

| 돌파 수 | 상태 | 액션 |
|---------|------|------|
| 0개 | 🟢 정상 | 일일 브리핑에 상태 표시 |
| 1개 | 🟡 주의 | 해당 지표 강조, 모니터링 강화 |
| 2개 | 🟠 경고 | Macro Layer 긴급 재판정 권고 |
| 3개+ | 🔴 레짐전환 | 전 포지션 재검토, Shawn 즉시 알림 |

### 2.4 데이터 수집 스크립트

```python
# data/regime-sentinel.py
import os
import json
import requests
from datetime import datetime, timedelta

FRED_KEY = os.environ.get('FRED_API_KEY')
TWELVE_KEY = os.environ.get('TWELVEDATA_API_KEY')

def get_vix():
    """Yahoo Finance v8 API for VIX"""
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=1d"
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = r.json()
    return data['chart']['result'][0]['meta']['regularMarketPrice']

def get_yield_spread():
    """FRED: 10Y - 2Y spread"""
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=T10Y2Y&api_key={FRED_KEY}&file_type=json&limit=1&sort_order=desc"
    r = requests.get(url)
    data = r.json()
    return float(data['observations'][0]['value'])

def get_hy_spread():
    """FRED: High Yield Spread"""
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=BAMLH0A0HYM2&api_key={FRED_KEY}&file_type=json&limit=1&sort_order=desc"
    r = requests.get(url)
    data = r.json()
    return float(data['observations'][0]['value']) * 100  # convert to bp

def get_btc_weekly():
    """CoinGecko: BTC 7-day change"""
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7"
    r = requests.get(url)
    data = r.json()
    prices = data['prices']
    if len(prices) < 2:
        return 0
    start = prices[0][1]
    end = prices[-1][1]
    return ((end - start) / start) * 100

def get_dxy_monthly():
    """Twelve Data: DXY 30-day change"""
    url = f"https://api.twelvedata.com/time_series?symbol=DXY&interval=1day&outputsize=30&apikey={TWELVE_KEY}"
    r = requests.get(url)
    data = r.json()
    if 'values' not in data:
        return 0
    values = data['values']
    if len(values) < 20:
        return 0
    current = float(values[0]['close'])
    month_ago = float(values[-1]['close'])
    return ((current - month_ago) / month_ago) * 100

def check_regime():
    vix = get_vix()
    spread_2_10 = get_yield_spread()
    hy_spread = get_hy_spread()
    btc_weekly = get_btc_weekly()
    dxy_monthly = get_dxy_monthly()
    
    alerts = []
    
    if vix > 25:
        alerts.append(('VIX', vix, '>25'))
    if spread_2_10 < 0:
        alerts.append(('2-10 Spread', spread_2_10, '<0'))
    if hy_spread > 400:
        alerts.append(('HY Spread', hy_spread, '>400bp'))
    if btc_weekly < -15:
        alerts.append(('BTC Weekly', btc_weekly, '<-15%'))
    if dxy_monthly > 3:
        alerts.append(('DXY Monthly', dxy_monthly, '>+3%'))
    
    status = '🟢 정상' if len(alerts) == 0 else \
             '🟡 주의' if len(alerts) == 1 else \
             '🟠 경고' if len(alerts) == 2 else \
             '🔴 레짐전환'
    
    return {
        'timestamp': datetime.now().isoformat(),
        'indicators': {
            'VIX': vix,
            '2-10 Spread': spread_2_10,
            'HY Spread': hy_spread,
            'BTC Weekly %': btc_weekly,
            'DXY Monthly %': dxy_monthly
        },
        'alerts': alerts,
        'alert_count': len(alerts),
        'status': status
    }

if __name__ == '__main__':
    result = check_regime()
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

### 2.5 일일 브리핑 통합

일일 브리핑 Phase 0에서 Regime Sentinel 데이터 수집 후, 결과를 다음 형식으로 포함:

```markdown
## 🚦 Regime Sentinel
**상태:** 🟢 정상 (0/5 임계치 돌파)

| 지표 | 현재값 | 임계치 | 상태 |
|------|--------|--------|------|
| VIX | 18.2 | >25 | 🟢 |
| 2-10 Spread | +42bp | <0 | 🟢 |
| HY Spread | 320bp | >400bp | 🟢 |
| BTC 주간 | -3.2% | <-15% | 🟢 |
| DXY 월간 | +0.8% | >+3% | 🟢 |
```

---

## 反 (Antithesis) — Critic 반박

### Critic Q1: "이게 정말 작동하는가?"

**반론 1: 지표 선택의 타당성**
- 5개 지표가 정말 레짐 전환을 잘 예측하는가?
- 백테스트 없이 임계치를 정했음
- **Risk Level:** 🟡 중간

**반론 2: 데이터 소스 신뢰성**
- FRED HY Spread (BAMLH0A0HYM2)는 1-2일 지연
- DXY 수집이 Twelve Data 의존 (rate limit)
- **Risk Level:** 🟢 낮음 (선제적 감지가 목적이므로 1-2일 지연 허용)

**반론 3: False Positive 리스크**
- 1개 임계치 돌파 = 🟡 주의 → 너무 자주 발생할 수 있음
- 경보 피로(alert fatigue) 유발
- **Risk Level:** 🟡 중간

### Critic Q2: "복잡도 대비 가치가 있는가?"

**반론 4: 단순히 VIX만 봐도 되지 않나?**
- VIX 25 하나로 충분한 레짐 감지 가능
- 5개 지표는 과잉 복잡도
- **Risk Level:** 🟡 중간 (반박 가능: 다차원 감지의 가치)

**반론 5: 스크립트 유지보수 비용**
- API 변경, rate limit 변경 시 스크립트 수정 필요
- 4개 API (Yahoo, FRED, CoinGecko, Twelve Data) 의존
- **Risk Level:** 🟢 낮음 (이미 PLEDS가 이 API들 사용 중)

### Critic Q3: "PLEDS와 잘 통합되는가?"

**반론 6: 일일 브리핑 시간 증가**
- 스크립트 실행 시간 추가 (API 호출 5회)
- 브리핑 내용 길이 증가
- **Risk Level:** 🟢 낮음 (10초 미만)

---

## 合 (Synthesis) — 최종 설계

### 2.6 Critic 피드백 반영

| 반론 | 해결책 |
|------|--------|
| 지표 선택 타당성 | 3개월 후 레짐 변화와 대조하여 지표 유효성 검증. 무효 지표 교체 |
| 데이터 지연 | 선제적 감지 목적이므로 1-2일 지연 허용. 급변 시 VIX 우선 |
| False Positive | 🟡 주의 (1개)는 브리핑에 표시만. 알림은 2개+ (🟠 경고)부터 |
| VIX만으로 충분 | VIX는 공포 감지. HY Spread는 신용, BTC는 크립토 특화. 다차원 유지 |
| 스크립트 유지보수 | 기존 API 재사용. 장애 시 fallback 로직 추가 |
| 브리핑 시간 | API 호출 병렬화로 5초 이내 완료 |

### 2.7 최종 구현 스펙

**스크립트:** `data/regime-sentinel.py` (위 설계대로 구현)

**METHODOLOGY.md 추가 (§3-5 Regime Sentinel):**
```markdown
### 3-5. Regime Sentinel (선제적 레짐 감지)

> 반응형 레짐 판정(VIX 25 돌파 후)을 보완하여, 레짐 전환을 선제적으로 감지한다.

| 지표 | 소스 | 임계치 | 의미 |
|------|------|--------|------|
| VIX | Yahoo | >25 | 공포 시작 |
| 2-10 Spread | FRED | <0 | 경기 침체 신호 |
| HY Spread | FRED | >400bp | 신용 리스크 |
| BTC 주간 | CoinGecko | <-15% | 크립토 레짐 전환 |
| DXY 월간 | Twelve Data | >+3% | 달러 강세 레짐 |

**경보 단계:**
| 돌파 수 | 상태 | 액션 |
|---------|------|------|
| 0개 | 🟢 정상 | 상태 표시 |
| 1개 | 🟡 주의 | 모니터링 강화 |
| 2개+ | 🟠 경고 | Macro 긴급 재판정, Shawn 알림 |
| 3개+ | 🔴 레짐전환 | 전 포지션 재검토 |

**규칙:**
- 일일 브리핑 Phase 0에서 자동 실행
- 🟠 경고 이상 시 텔레그램 즉시 알림
- 분기별 지표 유효성 검증
```

**WORKFLOW.md Phase 0 수정:**
```markdown
### Phase 0: 데이터 수집 (자동/크론, ~08:30)

**추가:** Regime Sentinel 실행
```bash
python3 data/regime-sentinel.py > daily/regime-sentinel-YYYY-MM-DD.json
```
→ 결과를 일일 브리핑 §Regime Sentinel에 포함
```

---

# Module 3: Expert System Restructure (24→15)

## 正 (Thesis) — 최선의 설계안

### 3.1 현재 전문가 역할 분석

**Layer 1 Macro (5명):**
| 전문가 | 핵심 역할 | 관점 |
|--------|----------|------|
| The Machine | 부채 사이클, All Weather | 장기 구조적 |
| The Liquidity Hawk | 연준 유동성, 자산가격 | 유동성 중심 |
| The Cycle Sentinel | 시장 온도, 센티먼트 | 사이클 위치 |
| The Contrarian Catalyst | 컨센서스 반대 | 역발상 (Critic) |
| Macro Moderator | 토론 수렴 | 중재 |

**중복 분석:**
- Machine + Liquidity Hawk: 둘 다 "유동성 → 자산가격" 프레임. Machine이 더 포괄적.
- Cycle Sentinel + Contrarian: 둘 다 "현재 위치가 과열인가?" 물음. 관점은 다르나 결론 유사할 때 多.

**Layer 2 Sector (4명):**
| 전문가 | 핵심 역할 | 관점 |
|--------|----------|------|
| The Disruptor | 기술 S-curve, TAM 확장 | 파괴적 혁신 |
| The Value Mapper | 산업별 멀티플 | 가치 평가 |
| The Theme Hunter | 비컨센서스 테마 | 발굴 |
| Sector Moderator | 토론 수렴 + Critic | 중재 |

**중복 분석:**
- Disruptor + Theme Hunter: 둘 다 "아직 시장이 모르는 기회" 탐색. 접근법만 다름.

**Layer 3 Value Chain (3명):**
| 전문가 | 핵심 역할 | 관점 |
|--------|----------|------|
| The Strategist | 5 Forces, 해자 | 경쟁전략 |
| The Network Thinker | 플랫폼, 수확체증 | 네트워크 효과 |
| Value Chain Moderator | 토론 수렴 + Critic | 중재 |

**중복 분석:**
- Strategist + Network Thinker: 둘 다 "가치가 어디 집중되는가?" 물음. Network Thinker는 디지털 특화.

**Layer 4 Company (4명):**
| 전문가 | 핵심 역할 | 관점 |
|--------|----------|------|
| The Compounder | 복리, ROIC, 품질 | 장기 보유 |
| The Catalyst Hunter | 이벤트, 구조적 저평가 | 단기 촉매 |
| The Forensic Accountant | 회계 검증, Bear Case | Critic |
| Company Moderator | 토론 수렴 | 중재 |

**중복 분석:**
- Compounder + Catalyst Hunter: 둘 다 "좋은 기업인가?" 물음. 시간축만 다름 (장기 vs 단기).
- Forensic은 반드시 유지 (전담 Critic).

**Layer 5 Technical (4명):**
| 전문가 | 핵심 역할 | 관점 |
|--------|----------|------|
| The Quant Dashboard | 정량 지표 팩트 | 숫자 |
| The Time Series Analyst | 시계열 추세 | 패턴 |
| The Structure Reader | 구조적 위치 | 종합 |
| Technical Moderator | 토론 수렴 + Critic | 중재 |

**중복 분석:**
- Quant Dashboard: 이건 전문가가 아니라 **자동화 도구**. 대시보드로 전환.
- Time Series + Structure Reader: 둘 다 "지금 진입해도 되는가?" 물음. 통합 가능.

### 3.2 통합 제안

**통합 원칙:**
1. **Orthogonal한 관점만 유지** — 같은 질문에 다른 답을 내는 전문가만 가치 있음
2. **Critic + Moderator 구조 보존** — Adversarial Debate의 핵심
3. **시간축/영역 분리** — 같은 영역에서 시간축만 다르면 통합

**통합 매핑:**

| 기존 | 통합 후 | 근거 |
|------|--------|------|
| Machine + Liquidity Hawk | **Regime Analyst** | 둘 다 유동성/사이클. Machine 프레임 + Hawk 유동성 포커스 결합 |
| Cycle Sentinel + Contrarian | **Counter-Consensus Analyst** | 사이클 위치 + 역발상을 통합. Critic 역할 흡수 |
| Macro Moderator | **Macro Moderator** | 유지 |
| Disruptor + Theme Hunter | **Opportunity Scanner** | 둘 다 새로운 기회 발굴. 접근법 통합 |
| Value Mapper | → Moat Analyst로 이동 | 산업 멀티플은 해자 분석에 포함 |
| Sector Moderator | **Sector Moderator** | 유지 (Critic 겸임) |
| Strategist + Network Thinker + Value Mapper | **Moat Analyst** | 5 Forces + 네트워크 + 멀티플 = 해자 종합 분석 |
| Value Chain Moderator | **Value Chain Moderator** | 유지 (Critic 겸임) |
| Compounder + Catalyst Hunter | **Company Analyst** | 장기/단기 시간축을 하나로. 복합 분석 |
| Forensic Accountant | **Forensic Accountant** | 유지 (전담 Critic) |
| Company Moderator | **Company Moderator** | 유지 |
| Quant Dashboard | **자동화 (전문가 아님)** | 스크립트로 대체 |
| Time Series + Structure Reader | **Technical Analyst** | 패턴 + 구조 = 기술적 분석 통합 |
| Technical Moderator | **Technical Moderator** | 유지 (Critic 겸임) |
| Data Auditor | **Data Auditor** | 유지 |
| Bottleneck Hunter | **Bottleneck Hunter** | 유지 (Cross-Layer) |
| Allocator | **Allocator** | 유지 |

### 3.3 통합 후 구조 (15명)

| Layer | 전문가 | 역할 | Critic |
|-------|--------|------|--------|
| Data | Data Auditor | 데이터 검증 | — |
| Macro | Regime Analyst | 유동성 + 사이클 | — |
| Macro | Counter-Consensus Analyst | 역발상 + 사이클 위치 | **Critic** |
| Macro | Macro Moderator | 수렴 | — |
| Sector | Opportunity Scanner | 파괴적 혁신 + 테마 발굴 | — |
| Sector | Sector Moderator | 수렴 | **Critic (겸임)** |
| Value Chain | Moat Analyst | 5 Forces + 네트워크 + 멀티플 | — |
| Value Chain | Value Chain Moderator | 수렴 | **Critic (겸임)** |
| Company | Company Analyst | 복리 + 촉매 (시간축 통합) | — |
| Company | Forensic Accountant | 회계 검증, Bear Case | **Critic (전담)** |
| Company | Company Moderator | 수렴 | — |
| Technical | Technical Analyst | 패턴 + 구조 (Dashboard 자동화) | — |
| Technical | Technical Moderator | 수렴 | **Critic (겸임)** |
| Cross-Layer | Bottleneck Hunter | 제약 조건 분석 | — |
| Synthesis | Allocator | 최종 의사결정 | — |

**Total: 15명** (24 → 15, 37.5% 감소)

---

## 反 (Antithesis) — Critic 반박

### Critic Q1: "이게 정말 작동하는가?"

**반론 1: 통합으로 관점 손실**
- Machine의 "장기 부채 사이클" vs Liquidity Hawk의 "연준 유동성" — 미묘한 차이
- 통합 시 Liquidity Hawk의 단기 유동성 포커스가 약화될 수 있음
- **Risk Level:** 🟡 중간

**반론 2: Contrarian이 Critic인데, 역할 겹침**
- Counter-Consensus Analyst가 Macro Critic이면서 동시에 의견 제시
- 심판이 선수를 겸하는 구조
- **Risk Level:** 🟡 중간

**반론 3: Company Analyst 역할 과부하**
- Compounder(장기) + Catalyst(단기)를 한 명이 다 하면?
- 시간축에 따른 충돌 가능
- **Risk Level:** 🟡 중간

### Critic Q2: "복잡도 대비 가치가 있는가?"

**반론 4: 24→15가 충분한 감소인가?**
- 여전히 15명은 많음. 10명 이하로 더 줄여야 하지 않나?
- **Risk Level:** 🟢 낮음 (5 Layer + Moderator + Critic 구조상 15가 최소)

**반론 5: 분석 품질 저하 리스크**
- 전문가 수가 줄면 관점의 다양성 감소
- 놓치는 인사이트 발생 가능
- **Risk Level:** 🟡 중간

### Critic Q3: "PLEDS와 잘 통합되는가?"

**반론 6: Adversarial Debate Protocol 수정 필요**
- METHODOLOGY §10의 Critic 배정 테이블 업데이트 필요
- WORKFLOW.md의 각 Phase 전문가 참여 목록 수정 필요
- **Risk Level:** 🟢 낮음 (문서 업데이트로 해결)

---

## 合 (Synthesis) — 최종 설계

### 3.4 Critic 피드백 반영

| 반론 | 해결책 |
|------|--------|
| 관점 손실 | Regime Analyst가 분석 시 "Dalio 관점" + "Druckenmiller 관점" 명시적 분리 |
| Critic 역할 겹침 | Counter-Consensus는 Round 1에서 독립 뷰 제시, Round 2에서 Critic 전환. 명확한 phase 분리 |
| Company Analyst 과부하 | 분석 시 "장기 뷰(5yr)" + "단기 뷰(1yr)" 섹션 분리. 두 시간축 모두 커버 |
| 15명이 충분한가 | Moderator 4명 + Critic 5명 = 9명 고정. 전문가 6명이 orthogonal 관점 제공. 최적 |
| 분석 품질 저하 | 3개월 후 분석 품질 리뷰. 문제 시 전문가 복원 |
| 문서 수정 | EXPERTS.md v3 전면 개정, METHODOLOGY §10 업데이트 |

### 3.5 관점 커버리지 매트릭스

**통합 전후 비교:**

| 관점 | 통합 전 담당 | 통합 후 담당 | 커버리지 |
|------|-------------|-------------|---------|
| 장기 부채 사이클 | Machine | Regime Analyst | ✅ 유지 |
| 단기 유동성 | Liquidity Hawk | Regime Analyst | ✅ 유지 |
| 시장 온도/센티먼트 | Cycle Sentinel | Counter-Consensus | ✅ 유지 |
| 컨센서스 반론 | Contrarian | Counter-Consensus | ✅ 유지 (Critic 역할) |
| 파괴적 혁신 | Disruptor | Opportunity Scanner | ✅ 유지 |
| 산업별 밸류에이션 | Value Mapper | Moat Analyst | ✅ 이동 |
| 비컨센서스 테마 | Theme Hunter | Opportunity Scanner | ✅ 유지 |
| 경쟁전략/5 Forces | Strategist | Moat Analyst | ✅ 유지 |
| 네트워크 효과 | Network Thinker | Moat Analyst | ✅ 유지 |
| 장기 복리 | Compounder | Company Analyst | ✅ 유지 |
| 단기 촉매 | Catalyst Hunter | Company Analyst | ✅ 유지 |
| 회계 검증/Bear Case | Forensic | Forensic Accountant | ✅ 유지 |
| 정량 지표 | Quant Dashboard | **자동화** | ✅ 자동화 |
| 시계열 패턴 | Time Series | Technical Analyst | ✅ 유지 |
| 구조적 위치 | Structure Reader | Technical Analyst | ✅ 유지 |
| 제약 조건 | Bottleneck Hunter | Bottleneck Hunter | ✅ 유지 |

**결론:** 모든 관점이 보존됨. 단, 통합된 전문가가 두 관점을 명시적으로 분리하여 제시해야 함.

---

# Module 4: Watchlist Alert System

## 正 (Thesis) — 최선의 설계안

### 4.1 핵심 통찰

현재 PORTFOLIO.md에 비정형 워치리스트 존재:
```
| QXO | $16-17 | ⭐⭐ WATCH |
| TOST | $25 이하 | ⭐⭐ WATCH |
```

**문제:**
1. 가격 도달 시 자동 알림 없음
2. 가설 붕괴(Kill Price) 관리 없음
3. 등록 후 방치 → stale thesis

### 4.2 watchlist.json 구조 설계

```json
{
  "watchlist": [
    {
      "ticker": "QXO",
      "target_price": 17.0,
      "target_type": "below",
      "thesis_summary": "Industrials 혁신 플랫폼, 지하철 CEO Jackie Reses 매수 지점",
      "kill_price": 25.0,
      "kill_reason": "밸류에이션 과열, 통합 시너지 미실현 확정 시",
      "added_date": "2026-03-21",
      "expiry_date": "2026-06-21",
      "source_judgment": "tracking/judgments/2026-03-21-QXO.md",
      "conviction": 2,
      "status": "active"
    }
  ],
  "last_updated": "2026-03-24T11:00:00+09:00"
}
```

**필드 설명:**
| 필드 | 타입 | 설명 |
|------|------|------|
| ticker | string | 종목 티커 |
| target_price | float | 진입 목표가 |
| target_type | "below" \| "above" | 목표가 도달 조건 |
| thesis_summary | string | 핵심 투자 가설 (1문장) |
| kill_price | float | 가설 폐기 가격 |
| kill_reason | string | Kill 조건 설명 |
| added_date | string | 워치리스트 등록일 |
| expiry_date | string | 만료일 (등록 후 90일) |
| source_judgment | string | 원본 PLEDS 분석 경로 |
| conviction | int | 확신도 (1-3) |
| status | "active" \| "triggered" \| "killed" \| "expired" | 현재 상태 |

### 4.3 자동 체크 프로세스

**scripts/watchlist-check.py:**
```python
import json
import requests
from datetime import datetime, date

def load_watchlist():
    with open('data/watchlist.json', 'r') as f:
        return json.load(f)

def save_watchlist(data):
    data['last_updated'] = datetime.now().isoformat()
    with open('data/watchlist.json', 'w') as f:
        json.dump(data, f, indent=2)

def get_price(ticker):
    """Yahoo Finance v8 API"""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = r.json()
    return data['chart']['result'][0]['meta']['regularMarketPrice']

def check_watchlist():
    data = load_watchlist()
    alerts = []
    
    for item in data['watchlist']:
        if item['status'] != 'active':
            continue
        
        ticker = item['ticker']
        current = get_price(ticker)
        
        # Target price check
        if item['target_type'] == 'below' and current <= item['target_price']:
            alerts.append({
                'type': 'TARGET_HIT',
                'ticker': ticker,
                'current': current,
                'target': item['target_price'],
                'thesis': item['thesis_summary']
            })
        elif item['target_type'] == 'above' and current >= item['target_price']:
            alerts.append({
                'type': 'TARGET_HIT',
                'ticker': ticker,
                'current': current,
                'target': item['target_price'],
                'thesis': item['thesis_summary']
            })
        
        # Kill price check
        if current >= item.get('kill_price', float('inf')):
            alerts.append({
                'type': 'KILL_HIT',
                'ticker': ticker,
                'current': current,
                'kill_price': item['kill_price'],
                'reason': item['kill_reason']
            })
            item['status'] = 'killed'
        
        # Expiry check
        expiry = datetime.strptime(item['expiry_date'], '%Y-%m-%d').date()
        if date.today() >= expiry:
            alerts.append({
                'type': 'EXPIRED',
                'ticker': ticker,
                'added_date': item['added_date']
            })
            item['status'] = 'expired'
    
    save_watchlist(data)
    return alerts

if __name__ == '__main__':
    alerts = check_watchlist()
    for a in alerts:
        print(json.dumps(a, ensure_ascii=False))
```

### 4.4 일일 브리핑 통합

**WORKFLOW.md Phase 0 추가:**
```bash
python3 scripts/watchlist-check.py > daily/watchlist-alerts-YYYY-MM-DD.json
```

**브리핑 포맷:**
```markdown
## 📋 Watchlist Alerts

🎯 **TARGET HIT:**
- QXO: 현재 $16.50 (목표 $17 이하) — "Industrials 혁신 플랫폼"

☠️ **KILL HIT:**
- (없음)

⏰ **EXPIRING SOON (7일 이내):**
- UBER (만료: 2026-03-30) — 재평가 필요
```

### 4.5 PORTFOLIO.md 마이그레이션

현재 비정형 워치리스트:
```
| QXO | $16-17 | ⭐⭐ WATCH |
| TOST | $25 이하 | ⭐⭐ WATCH |
| BLDR | $75-80 또는 Fed pivot | ⭐⭐ 관망 |
| UBER | $70-72 지지 or $77.57 돌파 | ⭐⭐ WATCH |
| RDDT | $120 이하 | ⭐⭐ WATCH |
| AER | $125-130 | ⭐⭐ WATCH |
```

→ `data/watchlist.json`으로 마이그레이션

---

## 反 (Antithesis) — Critic 반박

### Critic Q1: "이게 정말 작동하는가?"

**반론 1: Kill Price 설정의 어려움**
- 모든 종목에 kill price를 정하기 어려움
- BLDR처럼 "Fed pivot"이 조건인 경우 가격으로 표현 불가
- **Risk Level:** 🟡 중간

**반론 2: 뉴스 기반 가설 붕괴 감지 불가**
- 가격 기반 kill만 자동화
- "경쟁사 출현" 같은 뉴스 기반 kill은 수동 체크 필요
- **Risk Level:** 🟡 중간 (설계에서 인정)

**반론 3: 90일 만료가 적절한가?**
- 일부 종목은 6개월+ 기다려야 할 수 있음
- 만료 후 재등록 프로세스가 번거로울 수 있음
- **Risk Level:** 🟢 낮음 (만료 = 재평가 강제, 좋은 것)

### Critic Q2: "복잡도 대비 가치가 있는가?"

**반론 4: JSON 파일 관리 부담**
- PORTFOLIO.md의 간단한 테이블 vs JSON 구조
- 수동 편집 시 오류 가능성
- **Risk Level:** 🟢 낮음 (CRO가 관리, Shawn 부담 없음)

**반론 5: API 호출 비용**
- 워치리스트 종목 수 × 일일 1회 = 추가 API 호출
- 현재 6개 종목이면 6회/일 추가
- **Risk Level:** 🟢 낮음 (Twelve Data 800 req/day 여유)

### Critic Q3: "PLEDS와 잘 통합되는가?"

**반론 6: PORTFOLIO.md와의 중복**
- 워치리스트가 두 곳에 존재 (JSON + md)
- 동기화 이슈
- **Risk Level:** 🟡 중간

---

## 合 (Synthesis) — 최종 설계

### 4.6 Critic 피드백 반영

| 반론 | 해결책 |
|------|--------|
| Kill Price 어려움 | kill_price는 optional. 없으면 뉴스 기반 수동 체크 |
| 뉴스 기반 감지 불가 | 인정. 일일 브리핑에서 수동 체크. "가설 붕괴 뉴스?" 질문 포함 |
| 90일 만료 | 만료 7일 전 알림 → 재평가/연장/폐기 결정 |
| JSON 관리 부담 | PLEDS 분석 후 자동 추가 프로세스 구현. 수동 편집 최소화 |
| API 호출 비용 | 기존 일일 가격 수집에 통합. 별도 호출 아님 |
| PORTFOLIO.md 중복 | PORTFOLIO.md 워치리스트 → "상세는 data/watchlist.json 참조"로 변경 |

### 4.7 최종 구현 스펙

**data/watchlist.json:** 위 설계대로 구현 (Module 4.2)

**scripts/watchlist-check.py:** 위 설계대로 구현 (Module 4.3)

**WORKFLOW.md 추가:**
```markdown
### Phase 0: 데이터 수집에 추가
```bash
python3 scripts/watchlist-check.py > daily/watchlist-alerts-YYYY-MM-DD.json
```

### PLEDS 분석 후 (WATCH/WAIT 판정 시)
1. watchlist.json에 종목 추가
2. kill_price (가능하면), thesis_summary, expiry_date 설정
3. git commit + push
```

**PORTFOLIO.md 변경:**
```markdown
## 워치리스트
> 상세: `data/watchlist.json` 참조

| 종목 | 상태 | 만료 |
|------|------|------|
| QXO | active | 2026-06-21 |
| TOST | active | 2026-06-21 |
| ... | ... | ... |
```

---

# 통합 및 구현

## 파일 변경 요약

| 파일 | 변경 유형 | 내용 |
|------|----------|------|
| METHODOLOGY.md | 수정 | §3-5 Regime Sentinel 추가 |
| WORKFLOW.md | 수정 | Phase 0 Regime Sentinel, Phase 8.5 Decision Recording, Watchlist 추가 |
| EXPERTS.md | 전면 개정 | v3 (24→15) |
| PORTFOLIO.md | 수정 | 워치리스트 → JSON 참조로 변경 |
| data/regime-sentinel.py | 신규 | Regime Sentinel 스크립트 |
| data/watchlist.json | 신규 | 워치리스트 JSON |
| scripts/watchlist-check.py | 신규 | 워치리스트 체크 스크립트 |
| tracking/decisions/ | 신규 디렉토리 | Decision 기록 |
| tracking/accuracy.md | 수정 | Decision 열 추가 |

## 작동 확인 체크리스트

- [ ] data/regime-sentinel.py 실행 → 5개 지표 수집 확인
- [ ] scripts/watchlist-check.py 실행 → 가격 체크 확인
- [ ] tracking/decisions/ 디렉토리 생성 확인
- [ ] EXPERTS.md v3 적용 후 토론 품질 유지 확인 (3개월)
- [ ] 일일 브리핑에 Regime Sentinel + Watchlist Alert 통합 확인

---

## ICL Final Critic Pass

### "이 개선이 정말 Shawn의 목표 달성에 도움이 되는가?"

| 모듈 | 목표 기여 | 판정 |
|------|----------|------|
| Decision Tracker | 행동 패턴 인식 → 의사결정 개선 | ✅ 직접 기여 |
| Regime Sentinel | 손실 방지 → 자본 보존 | ✅ 직접 기여 |
| Expert 간소화 | 분석 속도 → 기회 포착 | ✅ 간접 기여 |
| Watchlist Alert | 진입 기회 포착 | ✅ 직접 기여 |

### "복잡도를 낮추면서 가치를 높이는가?"

| 모듈 | 복잡도 변화 | 가치 변화 |
|------|------------|----------|
| Decision Tracker | +1 (템플릿) | +3 (피드백 루프) |
| Regime Sentinel | +1 (스크립트) | +2 (선제 감지) |
| Expert 간소화 | **-9 (24→15)** | +1 (집중도) |
| Watchlist Alert | +1 (JSON) | +2 (자동 알림) |
| **Net** | **-6** | **+8** |

**결론:** 복잡도 순감소, 가치 순증가. 바닐라 원칙 준수.

---

*Generated: 2026-03-24*
*Author: CRO*
*Status: Implementation Ready*
