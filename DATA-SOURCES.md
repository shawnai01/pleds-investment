# PLEDS Data Sources — 데이터 소스 인프라

> 원칙: API > 스크래핑 > 추정(금지). 모든 데이터는 2개+ 소스 교차검증.

## 현재 상태 (2026-03-19 기준)

### ✅ 정상 작동

| 소스 | 커버리지 | 접근 방식 | 인증 |
|------|----------|----------|------|
| **CoinGecko API** | BTC, ETH, 크립토 전반, 24h 변동 | REST API (무료) | 불필요 |
| **Yahoo Finance v8 API** | 주식/ETF/지수 OHLCV, 당일 종가 | REST API (무료, rate limit 주의) | 불필요 |
| **SEC EDGAR** | 10-K, 10-Q, 8-K 원본 | web_fetch | 불필요 |

### ✅ API 키 확보 완료

| 소스 | 커버리지 | 상태 | 환경변수 |
|------|----------|------|----------|
| **FRED API** | FFR, 금리, CPI, M2, 실업률 등 매크로 | ✅ 작동 확인 | `FRED_API_KEY` |
| **Alpha Vantage** | 주식 시세, 기술지표 | ✅ 작동 확인 (25 req/day) | `ALPHAVANTAGE_API_KEY` |
| **Twelve Data** | 실시간 시세, OHLCV, 기술지표 | ✅ 작동 확인 (800 req/day) | `TWELVEDATA_API_KEY` |

### ⚠️ API 키 필요 (Shawn 인증 요청)

| 소스 | 커버리지 | 무료 티어 | 키 발급 URL |
|------|----------|----------|-------------|
| **Brave Search API** | 웹 검색 | 2000 req/mo | OpenClaw 설정 필요 |

### ❌ 접근 불가 (JS 렌더링 / 인증벽)

| 소스 | 문제 | 대안 |
|------|------|------|
| CNBC | JS 렌더링 필요 | browser 도구 사용 또는 RSS |
| Reuters | 401 인증 | browser 도구 사용 |
| MarketWatch | 401 인증 | browser 도구 사용 |
| ForexFactory | Cloudflare 차단 | browser 도구 사용 |

## 데이터 항목별 소스 매핑

| 데이터 항목 | 1차 소스 | 2차 소스 (교차검증) | 현재 상태 |
|------------|----------|-------------------|----------|
| BTC/ETH 가격 | CoinGecko API ✅ | Yahoo Finance | ✅ 가능 |
| 주식 시세 (SPY, QQQ 등) | Alpha Vantage (GLOBAL_QUOTE) | Yahoo Finance | ✅ 교차검증 가능 |
| FFR (기준금리) | **FRED API** (DFEDTARU/DFEDTARL) | Fed 프레스릴리즈 | ✅ 작동 |
| 2Y/10Y 금리 | FRED API (DGS2, DGS10) | Yahoo Finance (^TNX) | ✅ 작동 |
| VIX | **Yahoo v8 (^VIX, 당일)** | FRED VIXCLS (1일 지연) | ✅ Yahoo 우선 |
| DXY | Yahoo Finance (DX-Y.NYB) | Twelve Data | ⚠️ 키 필요 |
| MVRV | Glassnode / CoinMetrics | — | ❌ API 키 필요 (유료) |
| BTC Dominance | CoinGecko API ✅ | TradingView | ✅ 가능 |
| Funding Rates | CoinGecko derivatives API | Coinglass | ⚠️ 제한적 |
| 기업 재무 (EPS, EBITDA) | SEC EDGAR | Yahoo Finance | ✅ 가능 |
| FOMC 결정 | Fed 프레스릴리즈 | CNBC (browser) | ⚠️ 타이밍 주의 |
| 섹터 ETF | Yahoo Finance | — | ✅ 가능 |

## 우선 확보 요청 (Shawn)

### 🔴 필수 (매일 사용)
1. **FRED API Key** — 매크로 데이터의 근간. FFR, 금리, 인플레 등 모두 여기서 옴
   - 발급: https://fred.stlouisfed.org/docs/api/api_key.html (이메일 인증, 무료)

### 🟡 권장 (데이터 품질 향상)
2. **Alpha Vantage Key** — 주식 시세 교차검증 + FFR 백업
   - 발급: https://www.alphavantage.co/support/#api-key (무료, 25 req/day)
3. **Twelve Data Key** — 실시간 시세 + 기술지표
   - 발급: https://twelvedata.com/pricing (무료, 800 req/day)

### 🟢 있으면 좋음
4. **Brave Search API** — web_search 활성화 (현재 비활성)

## API 키 저장 위치

키를 받으면 환경변수로 설정:
```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export FRED_API_KEY="your_key_here"
export ALPHAVANTAGE_API_KEY="your_key_here"  
export TWELVEDATA_API_KEY="your_key_here"
```

또는 CRO에게 직접 알려주시면 PLEDS 크론잡 프롬프트에 내장합니다.
