# PLEDS Data Audit - 2026-03-19

## PHASE 0.5: DATA INTEGRITY AUDIT

### Confidence Legend
- ✅ Verified (2+ sources or API confirmed)
- ⚠️ Single-Source (1 reliable source)
- ❌ Unverified (access blocked/limited)

## Market Data Collection Status

| Asset/Metric | Value | Confidence | Source | Notes |
|--------------|-------|------------|--------|-------|
| **CRYPTO ASSETS** |
| Bitcoin (BTC) | $71,230 | ✅ | CoinGecko API | Retrieved 2026-03-19 00:05 UTC |
| Ethereum (ETH) | $2,203.74 | ✅ | CoinGecko API | Retrieved 2026-03-19 00:05 UTC |
| **MACRO INDICES** |
| SPY | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| QQQ | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| DXY | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| TLT | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| GLD | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| VIX | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| **SECTOR ETFS** |
| XLK (Tech) | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| XLF (Financial) | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| XLE (Energy) | [미확인] | ❌ | Yahoo Finance | Rate limited/blocked |
| **PORTFOLIO HOLDINGS** |
| BMNR | [미확인] | ❌ | Multiple sources | Unable to access current price |
| CRCL | [미확인] | ❌ | Multiple sources | Unable to access current price |
| COIN | [미확인] | ❌ | Multiple sources | Unable to access current price |
| SGOV | [미확인] | ❌ | Multiple sources | Unable to access current price |
| **RATES & YIELDS** |
| Fed Funds Rate | 3.50-3.75% | ⚠️ | Yahoo Finance snippet | From Fed March meeting |
| 2Y Treasury | [미확인] | ❌ | N/A | Unable to access |
| 10Y Treasury | [미확인] | ❌ | N/A | Unable to access |
| **CRYPTO METRICS** |
| BTC Dominance | [미확인] | ❌ | N/A | Unable to access |
| MVRV Ratio | [미확인] | ❌ | N/A | Unable to access |
| Funding Rates | [미확인] | ❌ | N/A | Unable to access |
| USDT Dominance | [미확인] | ❌ | N/A | Unable to access |

## Data Collection Challenges
1. **Web Search API**: Brave Search API key not configured
2. **Yahoo Finance**: Rate limiting and access restrictions
3. **MarketWatch**: Requires JavaScript/blocks automated access
4. **Real-time APIs**: Most require authentication

## Verified Information
- **Bitcoin**: $71,230 USD (확실한 데이터)
- **Ethereum**: $2,203.74 USD (확실한 데이터)  
- **Fed Policy**: Rates held at 3.50-3.75% range (March FOMC)

## Risk Assessment
⚠️ **HIGH RISK**: Limited real-time data availability significantly constrains analysis quality. Proceeding with expert consensus methodology using available crypto data and last known market conditions.

---
*Report generated: 2026-03-19 09:06 KST*
*Data collection time: 00:05-00:06 UTC*