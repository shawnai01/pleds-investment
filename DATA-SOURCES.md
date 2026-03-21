# PLEDS Data Sources — 데이터 소스 인프라

> 원칙: API > 스크래핑 > 추정(금지). 모든 데이터는 2개+ 소스 교차검증.  
> v2.1: Information Source Tier 체계 적용

---

## Information Source Tier 체계 (METHODOLOGY §3-2)

### Tier 1 — 최고 신뢰 (1차 데이터)
> **`[FACT]` 태그 허용**

| 소스 | 커버리지 | 용도 |
|------|----------|------|
| **SEC EDGAR** | 10-K, 10-Q, 8-K, DEF 14A proxy, Form 4 | 기업 재무, 내부자 거래 |
| **FRED (Federal Reserve)** | FFR, 금리, CPI, M2, 실업률 | 매크로 데이터 |
| **BLS / Census** | 고용, 소비, 인구 통계 | 매크로 데이터 |
| **기업 IR 페이지** | Earnings transcript, Investor presentation | 기업 분석 |
| **USPTO / Google Patents** | 특허 출원 | 기술 경쟁력 분석 |
| **CoinGecko API** | 크립토 가격, 시총, 온체인 지표 | 크립토 데이터 |
| **Twelve Data API** | 주식 가격, OHLCV, 기술지표 | 가격/차트 데이터 |

### Tier 2 — 높은 신뢰 (전문 분석)
> **`[FACT]` 태그 허용**

| 소스 | 커버리지 | 용도 |
|------|----------|------|
| **Google Scholar / arXiv / SSRN** | 학술 논문 | 기술/산업 심층 분석 |
| **IEA, WHO, FAO, IMF, World Bank** | 국제기구 보고서 | 산업/매크로 전망 |
| **Fed, ECB, BOJ working papers** | 중앙은행 발간물 | 통화정책 분석 |
| **Reuters, Bloomberg** | 전문 미디어 (발췌) | 뉴스/이벤트 |

### Tier 3 — 참고 (2차 해석)
> **`[THESIS]` 또는 `[REFERENCE]` 태그만 허용, 편향 인지 필수**

| 소스 | 커버리지 | 주의사항 |
|------|----------|---------|
| **Seeking Alpha** | 투자 리서치 | Long/Short 편향 인지 |
| **Motley Fool** | 투자 리서치 | 낙관 편향 인지 |
| **YouTube / 팟캐스트** | 전문가 인터뷰 | 발언자 신원 확인 |
| **X (Twitter)** | 실시간 센티먼트 | **팩트로 사용 금지** — 지표용만 |
| **Reddit** | 커뮤니티 센티먼트 | **팩트로 사용 금지** — 지표용만 |

### Tier 4 — 경계 (노이즈)
> **PLEDS 입력 금지. 참고 시 `[Tier 4 — 미검증]` 명시**

| 소스 | 커버리지 | 위험 |
|------|----------|------|
| 익명 게시판 | 루머 | 검증 불가 |
| 출처 불명 텔레그램 채널 | 루머 | 조작 가능성 |
| "내부자 정보" 주장 | — | 법적 리스크 |

---

## ⚠️ 주식 시세 수집 필수 규칙

1. **1차**: Twelve Data API (`time_series`, 800 req/day) — 가장 안정적
2. **2차**: Alpha Vantage API (`GLOBAL_QUOTE`, 25 req/day) — 교차검증용
3. **3차(백업)**: Yahoo v8 API — 소형주 페이지 로드 불안정, 최후 수단
4. **금지**: Yahoo 웹스크래핑(web_fetch)으로 주가 수집 시도 — 소형주/ETF 실패율 높음
5. **규칙**: 1차 실패 시 반드시 2차 시도. 양쪽 실패 시 "[수집 실패]" 명시. 절대 생략 금지.

---

## 현재 상태 (2026-03-21 기준)

### ✅ 정상 작동

| 소스 | Tier | 커버리지 | 접근 방식 | 인증 |
|------|------|----------|----------|------|
| **CoinGecko API** | 1 | BTC, ETH, 크립토 전반, 24h 변동 | REST API (무료) | 불필요 |
| **Yahoo Finance v8 API** | 1 | 주식/ETF/지수 OHLCV, 당일 종가 | REST API (무료, rate limit 주의) | 불필요 |
| **SEC EDGAR** | 1 | 10-K, 10-Q, 8-K 원본 | web_fetch | 불필요 |

### ✅ API 키 확보 완료

| 소스 | Tier | 커버리지 | 상태 | 환경변수 |
|------|------|----------|------|----------|
| **FRED API** | 1 | FFR, 금리, CPI, M2, 실업률 등 매크로 | ✅ 작동 확인 | `FRED_API_KEY` |
| **Alpha Vantage** | 1 | 주식 시세, 기술지표 | ✅ 작동 확인 (25 req/day) | `ALPHAVANTAGE_API_KEY` |
| **Twelve Data** | 1 | 실시간 시세, OHLCV, 기술지표 | ✅ 작동 확인 (800 req/day) | `TWELVEDATA_API_KEY` |

### ⚠️ API 키 필요 (Shawn 인증 요청)

| 소스 | Tier | 커버리지 | 무료 티어 | 키 발급 URL |
|------|------|----------|----------|-------------|
| **Brave Search API** | — | 웹 검색 | 2000 req/mo | OpenClaw 설정 필요 |

### ❌ 접근 불가 (JS 렌더링 / 인증벽)

| 소스 | Tier | 문제 | 대안 |
|------|------|------|------|
| CNBC | 2 | JS 렌더링 필요 | browser 도구 사용 또는 RSS |
| Reuters | 2 | 401 인증 | browser 도구 사용 |
| MarketWatch | 3 | 401 인증 | browser 도구 사용 |
| ForexFactory | 3 | Cloudflare 차단 | browser 도구 사용 |

---

## 데이터 항목별 소스 매핑

| 데이터 항목 | Tier | 1차 소스 | 2차 소스 (교차검증) | 현재 상태 |
|------------|------|----------|-------------------|----------|
| BTC/ETH 가격 | 1 | CoinGecko API ✅ | Yahoo Finance | ✅ 가능 |
| 주식 시세 (SPY, QQQ 등) | 1 | **Twelve Data** (800/day) | Alpha Vantage (25/day) | ✅ 교차검증 가능 |
| FFR (기준금리) | 1 | **FRED API** (DFEDTARU/DFEDTARL) | Fed 프레스릴리즈 | ✅ 작동 |
| 2Y/10Y 금리 | 1 | FRED API (DGS2, DGS10) | Yahoo Finance (^TNX) | ✅ 작동 |
| VIX | 1 | **Yahoo v8 (^VIX, 당일)** | FRED VIXCLS (1일 지연) | ✅ Yahoo 우선 |
| DXY | 1 | Yahoo Finance (DX-Y.NYB) | Twelve Data | ⚠️ 키 필요 |
| MVRV | 1 | Glassnode / CoinMetrics | — | ❌ API 키 필요 (유료) |
| BTC Dominance | 1 | CoinGecko API ✅ | TradingView | ✅ 가능 |
| **기술지표 (RSI/MACD/BB/EMA/ADX/Stoch/ATR/OBV)** | 1 | **Twelve Data API** | — | ✅ 작동 확인 |
| **기술지표 시계열 (로컬)** | 1 | `data/indicators/*.json` (Twelve Data 적재) | 일 1회 자동 수집 | ✅ 로컬 축적 |
| Funding Rates | 1 | CoinGecko derivatives API | Coinglass | ⚠️ 제한적 |
| 기업 재무 (EPS, EBITDA) | 1 | SEC EDGAR | Yahoo Finance | ✅ 가능 |
| FOMC 결정 | 1 | Fed 프레스릴리즈 | CNBC (browser) | ⚠️ 타이밍 주의 |
| 섹터 ETF | 1 | Yahoo Finance | — | ✅ 가능 |

---

## 우선 확보 요청 (Shawn)

### 🔴 필수 (매일 사용)
1. **FRED API Key** — ✅ 확보 완료

### 🟡 권장 (데이터 품질 향상)
2. **Alpha Vantage Key** — ✅ 확보 완료
3. **Twelve Data Key** — ✅ 확보 완료

### 🟢 있으면 좋음
4. **Brave Search API** — web_search 활성화 (현재 비활성)

---

## API 키 저장 위치

키를 받으면 환경변수로 설정:
```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export FRED_API_KEY="your_key_here"
export ALPHAVANTAGE_API_KEY="your_key_here"  
export TWELVEDATA_API_KEY="your_key_here"
```

또는 CRO에게 직접 알려주시면 PLEDS 크론잡 프롬프트에 내장합니다.

---

## Data Source Health Check (METHODOLOGY §3-1)

**일일 점검 항목:**

| 소스 | 점검 항목 | 주기 | 장애 시 |
|------|----------|------|--------|
| FRED API | API 응답 정상, 데이터 최신일 | 매일 | Alpha Vantage 대체 |
| Twelve Data | Rate limit 잔여, 데이터 갭 | 매일 | Alpha Vantage 대체 |
| Alpha Vantage | API 키 유효, 응답 지연 | 주간 | Yahoo v8 대체 |
| CoinGecko | 가격 일치, 온체인 지표 | 매일 | Yahoo Finance 대체 |
| Yahoo v8 | 엔드포인트 변경 여부 | 주간 | browser 도구 |
| SEC EDGAR | 파싱 정상 | 이벤트시 | 수동 확인 |

**장애 발생 시:**
```
[DATA SOURCE ALERT]
소스: [소스명]
장애 유형: [timeout/401/parsing error/...]
발생 시각: YYYY-MM-DD HH:MM KST
대체 소스: [대체 소스명]
Shawn 알림: ✅/❌
```

**상태 기록:** `audit/data-source-health.md`

---

## 신규 소스 등록 절차

1. **Tier 분류**: 1차 데이터 vs 2차 분석 vs 참고 vs 노이즈
2. **신뢰도 검증**: 기존 소스와 교차검증 (최소 10건)
3. **접근성 확인**: API 유무, Rate limit, 비용
4. **등록**: 이 파일에 추가 + `audit/` 폴더에 검증 기록
