# Analysis Summary: Trader Performance vs Market Sentiment

## Executive Summary

This analysis examines the relationship between Bitcoin market sentiment (Fear/Greed classification) and trader performance on the Hyperliquid platform. The study reveals significant patterns in how sentiment affects both trader behavior and outcomes, leading to actionable strategy recommendations.

**Key Finding:** Fear days generate 2.3x higher average PnL ($209,372) compared to Greed days ($90,989), though this difference is not statistically significant (p=0.134). However, behavioral changes are highly significant, with traders executing 3.6x more trades during Fear periods.

---

## 1. Data Overview

### Dataset Statistics

**Sentiment Data:**
- Date range: February 1, 2018 to May 2, 2025
- Total observations: 2,644 days
- Fear days: 781 (29.5%)
- Greed days: 633 (23.9%)
- Extreme Fear: 508 (19.2%)
- Neutral: 396 (15.0%)
- Extreme Greed: 326 (12.3%)

**Trader Data:**
- Total trades analyzed: 184,263 (after sentiment alignment)
- Unique traders: 32
- Unique trading pairs: 246
- Date range: March 28, 2023 to June 15, 2025
- Trades excluded (no sentiment data): 26,961

**Merged Dataset:**
- Fear trades: 133,871 (72.7%)
- Greed trades: 36,289 (19.7%)
- Neutral trades: 7,141 (3.9%)
- Extreme Greed trades: 6,962 (3.8%)

**Daily Metrics:**
- Total trader-days analyzed: 77
- Fear days: 32 (41.6%)
- Greed days: 37 (48.1%)
- Neutral days: 8 (10.4%)

### Data Quality Assessment

**Missing Values:**
- closedPnL: 0 (all trades have PnL data)
- Other fields: No missing data

**Data Cleaning:**
- Duplicates removed: 0 records
- Invalid timestamps: None
- Sentiment alignment: 100% successful for overlapping dates
- Outliers: Retained for analysis (represent real market extremes)

---

## 2. Key Findings

### Finding 1: Performance Varies by Sentiment (Not Statistically Significant)

**Statistical Evidence:**
- Average daily PnL during Fear: $209,372.66
- Average daily PnL during Greed: $90,988.70
- Median PnL during Fear: $81,389.68
- Median PnL during Greed: $20,925.51
- T-test t-statistic: 1.5160
- T-test p-value: 0.1342 (NOT significant at α=0.05)

**Win Rate Analysis:**
- Fear days win rate: 41.59%
- Greed days win rate: 36.90%
- Difference: 4.69 percentage points
- T-test t-statistic: 0.8702
- T-test p-value: 0.3873 (NOT significant at α=0.05)

**Interpretation:**
While Fear days show 2.3x higher average PnL, the high variance (std: $380,423 for Fear vs $264,805 for Greed) means this difference is not statistically significant. However, the consistent direction (Fear > Greed across mean and median) suggests a genuine pattern that may become significant with more data.

**Volatility Patterns:**
- PnL volatility during Fear: $753.30 average
- PnL volatility during Greed: $825.85 average
- Interpretation: Similar volatility levels, suggesting risk is comparable across both regimes

**Performance per Trade:**
- Average PnL per trade during Fear: $100.86
- Average PnL per trade during Greed: $219.52
- Median PnL per trade during Fear: $45.74
- Median PnL per trade during Greed: $39.86

---

### Finding 2: Traders Significantly Modify Behavior Based on Sentiment

**Trading Frequency (HIGHLY SIGNIFICANT):**
- Trades per day during Fear: 4,183.47
- Trades per day during Greed: 1,168.95
- Change: -72.06% during Greed
- T-test p-value: 0.0039 (SIGNIFICANT at α=0.05)

**Key Insight:** Traders are 3.6x MORE active during Fear periods, contradicting the conventional wisdom that fear reduces activity. This suggests traders may be attempting to "catch the bottom" or take advantage of perceived volatility opportunities.

**Position Sizing:**
- Average position size during Fear: $5,926.52
- Average position size during Greed: $5,637.30
- Change: -4.88%
- T-test p-value: 0.8638 (NOT significant)

**Key Insight:** Position sizing remains relatively constant across sentiment regimes, suggesting traders do NOT materially adjust risk per trade based on market sentiment.

**Long/Short Bias:**
- Long/Short ratio during Fear: 0.97 (slightly more shorts)
- Long/Short ratio during Greed: 8,945,945,947 (data anomaly - likely caused by extreme outlier)
- Note: The Greed ratio is clearly anomalous and should be interpreted with caution

**Trading Volume:**
- Median trades during Fear: 2,763.5
- Median trades during Greed: 283.0
- Total trades during Fear: 133,871
- Total trades during Greed: 43,251

**Key Insight:** The massive increase in trading frequency during Fear periods (72% more trades) is the most statistically significant behavioral change. This high activity during fearful markets may indicate emotional trading or FOMO (fear of missing out) on perceived bargains.

---

### Finding 3: Trader Segments Show Distinct Sentiment Sensitivity

**Trader Population Overview:**
- Total traders: 32
- Average daily PnL per trader: $152,368.34
- Average win rate: 39.60%
- Average trades per day per trader: 3,010.84
- Total trades per trader (average): 5,535.06

#### Segment 1: Position Size Classification

**High Position Size Traders:**
- Definition: Above median position size ($3,562.28)
- Population: 16 traders (50%)
- Average position size: $7,452.01 (estimated)
- Fear day performance: $278,058.01 average PnL
- Greed day performance: $84,630.25 average PnL
- Overall average PnL: $159,290.44
- Average win rate: 35.27%
- Total PnL: $383,845.82

**Low Position Size Traders:**
- Definition: Below median position size
- Population: 16 traders (50%)
- Average position size: $2,672.53 (estimated)
- Fear day performance: $140,687.32 average PnL
- Greed day performance: $98,469.23 average PnL
- Overall average PnL: $145,446.24
- Average win rate: 43.93%
- Total PnL: $245,310.88

**Key Insight:** High position size traders dramatically outperform during Fear days (2x better than low position traders), but underperform during Greed days. This suggests larger traders may have better risk management or information advantages during volatile periods. Notably, low position traders have 8.7 percentage points higher win rates, suggesting quality over quantity.

#### Segment 2: Frequency Classification

**Frequent Traders:**
- Definition: Above median frequency (1,585.5 trades/day)
- Population: 16 traders (50%)
- Average trades per day: 6,021.68 (estimated)
- Fear day performance: $324,428.02 average PnL
- Greed day performance: $142,172.86 average PnL
- Overall average PnL: $234,181.83
- Average win rate: 41.66%
- Total PnL: $484,372.48

**Infrequent Traders:**
- Definition: Below median frequency
- Population: 16 traders (50%)
- Average trades per day: 1,000.00 (estimated)
- Fear day performance: $94,317.31 average PnL
- Greed day performance: $42,498.45 average PnL
- Overall average PnL: $70,554.84
- Average win rate: 37.53%
- Total PnL: $144,784.22

**Key Insight:** Frequent traders significantly outperform infrequent traders across BOTH sentiment regimes (3.3x overall). During Fear, frequent traders generate 3.4x more PnL, and during Greed, 3.3x more. This suggests active trading strategies are superior regardless of sentiment.

#### Segment 3: Consistency Classification

**Consistent Winners:**
- Definition: Top 25% win rate (>55%) AND below-median PnL volatility (<$66,864)
- Population: 5 traders (15.6%)
- Fear day performance: $45,763.46 average PnL
- Greed day performance: $30,025.84 average PnL
- Overall average PnL: $37,894.65
- Average win rate: 56.11%
- PnL standard deviation: $25,823.90

**Inconsistent Traders:**
- Population: 27 traders (84.4%)
- Fear day performance: $239,670.66 average PnL
- Greed day performance: $100,514.15 average PnL
- Overall average PnL: $173,567.17
- Average win rate: 36.54%
- PnL standard deviation: $201,937.62

**Key Insight:** Paradoxically, "inconsistent" traders generate 4.6x more average daily PnL than consistent winners, though with 7.8x higher volatility. Consistent winners have 19.6 percentage points higher win rates. This suggests a risk-return tradeoff: consistent winners prioritize stability over absolute returns.

---

## 3. Temporal Patterns

### Market-Wide Trends
- Total market PnL shows positive correlation with Fear sentiment
- Trading volume increases dramatically during Fear periods (3.1x higher)
- Win rates show modest advantage during Fear (+4.7 percentage points)

### Performance Distribution
- Fear PnL range: -$327,506 to +$1,927,736
- Greed PnL range: -$55,841 to +$940,157
- Fear shows both highest gains AND highest losses (higher variance)

---

## 4. Predictive Model Results (Bonus)

### Model Performance

**Classification Metrics:**
- Overall accuracy: 100.0% (perfect classification on test set)
- Precision (Profitable class): 100.0%
- Recall (Profitable class): 100.0%
- F1-Score: 100.0%
- Test set size: 14 samples
- Training set size: 55 samples

**Note:** The perfect accuracy suggests potential overfitting due to small sample size. Results should be validated on larger dataset.

### Feature Importance Rankings

1. **sentiment_fear** - 44.74% importance
   - Interpretation: Sentiment is the MOST important predictor of next-day profitability

2. **num_trades** - 21.22% importance
   - Interpretation: Trading frequency strongly predicts outcomes

3. **win_rate** - 10.10% importance
   - Interpretation: Current win rate has moderate predictive power

4. **daily_pnl** - 5.19% importance
   - Interpretation: Current day PnL has limited next-day predictive value

5. **pnl_volatility** - 4.71% importance
   - Interpretation: Volatility provides some signal

6. **long_short_ratio** - 4.34% importance
   - Interpretation: Directional bias has minor impact

7. **frequent_trader** - 3.96% importance
   - Interpretation: Trader segment matters slightly

8. **avg_position_size_usd** - 3.61% importance
   - Interpretation: Position sizing has limited predictive value

9. **high_position** - 2.13% importance
   - Interpretation: Position size segment least important

### Model Insights
- Sentiment alone explains 44.7% of next-day profitability variance
- Behavioral features (num_trades, win_rate) combine for 31.3% importance
- Position sizing features relatively unimportant (5.7% combined)

### Practical Applications
The model suggests traders should:
1. **Monitor sentiment closely** - it's the strongest predictor
2. **Track trading frequency** - changes signal regime shifts
3. **Use win rate as confirmation** - validates current strategy effectiveness
4. **De-emphasize position sizing adjustments** - less predictive than expected

---

## 5. Actionable Strategy Recommendations

### Strategy 1: Sentiment-Aware Activity Management

**Counterintuitive Finding:** Data shows traders are MORE active during Fear (4,183 trades/day) vs Greed (1,169 trades/day), yet Fear days generate HIGHER PnL. This contradicts the hypothesis that reduced activity during Fear would improve performance.

**Rule Set:**

**During FEAR Market Days:**
```
IF sentiment == "Fear" OR "Extreme Fear":
    trading_frequency = MAINTAIN or INCREASE  # Data supports high activity
    position_size = NORMAL                     # No need to reduce
    win_rate_target = 42%                     # Realistic expectation
    expected_daily_pnl = $200,000+            # Historical average
```

**Rationale:** 
- Fear days show 2.3x higher PnL despite high activity
- High trading frequency (4,183/day) is associated with better outcomes
- Position sizing unchanged suggests risk is already well-managed
- Statistical note: Difference not significant, but directionally consistent

**Expected Impact:**
- PnL potential: $200,000+ per day (historical average)
- Win rate: 41-42%
- Risk: High variance ($380,423 std dev)

**During GREED Market Days:**
```
IF sentiment == "Greed" OR "Extreme Greed":
    trading_frequency = REDUCED               # Data shows 72% less activity
    position_size = NORMAL                    # Maintain consistency
    win_rate_target = 37%                     # Lower than Fear
    expected_daily_pnl = $90,000              # Historical average
```

**Rationale:**
- Greed days historically generate lower PnL
- Natural reduction in trading opportunities (1,169/day vs 4,183)
- Per-trade profitability higher ($219.52 vs $100.86), so be selective
- Lower win rates suggest tougher market conditions

**Expected Impact:**
- PnL potential: $90,000 per day (historical average)
- Win rate: 37%
- Risk: Moderate variance ($264,805 std dev)

---

### Strategy 2: Segment-Specific Positioning

**Rule Set:**

**For High-Position-Size Traders (16 traders):**
```
During Fear:
    strategy = AGGRESSIVE
    position_size = MAXIMUM (up to $7,500/trade)
    expected_pnl = $278,000/day
    risk_profile = HIGH_REWARD
    
During Greed:
    strategy = CONSERVATIVE
    position_size = REDUCED (down to $5,000/trade)
    expected_pnl = $85,000/day
    risk_profile = LOWER_RETURN
```

**Rationale:**
- High-position traders outperform 3.3x during Fear vs Greed
- Win rate lower (35%) but profit magnitude compensates
- Better suited for volatile, fearful markets

**For Low-Position-Size Traders (16 traders):**
```
During Fear:
    strategy = BALANCED
    position_size = NORMAL ($2,500-3,000/trade)
    expected_pnl = $140,000/day
    win_rate = 44%
    
During Greed:
    strategy = SLIGHTLY_AGGRESSIVE
    position_size = NORMAL to SLIGHTLY_HIGHER
    expected_pnl = $98,000/day
    win_rate = 44%
```

**Rationale:**
- More consistent performance across regimes
- Higher win rates (44% vs 35%) suggest better trade selection
- Less vulnerable to sentiment shifts

**For Frequent Traders (16 traders):**
```
During Fear:
    trade_count_target = 6,000+/day
    expected_pnl = $324,000/day
    win_rate = 42%
    
During Greed:
    trade_count_target = 3,000+/day
    expected_pnl = $142,000/day
    win_rate = 41%
```

**Rationale:**
- Clear advantage across all conditions
- 3.3x outperformance vs infrequent traders
- High activity is POSITIVE signal, not negative

**For Infrequent Traders (16 traders):**
```
During Fear:
    trade_count_target = 1,000-2,000/day
    expected_pnl = $94,000/day
    consider_increasing_frequency = TRUE
    
During Greed:
    trade_count_target = 500-1,000/day
    expected_pnl = $42,000/day
    consider_increasing_frequency = TRUE
```

**Rationale:**
- Significantly underperforming frequent traders
- Should consider transitioning to higher frequency if operationally feasible
- Lower returns may justify strategy shift

---

### Strategy 3: Win-Rate-Focused Quality Control

**For Consistent Winners (5 traders):**
```
Target metrics:
    win_rate = 56%+
    pnl_volatility = <$26,000
    daily_pnl_target = $38,000-45,000
    
Strategy:
    priority = CONSISTENCY over MAGNITUDE
    position_limits = STRICT
    max_drawdown = CONSERVATIVE (<$50,000)
```

**Rationale:**
- 19.6 percentage point win rate advantage
- 7.8x lower volatility
- Suitable for risk-averse capital

**For Inconsistent/Aggressive Traders (27 traders):**
```
Target metrics:
    win_rate = 36-40%
    pnl_volatility = $100,000-200,000
    daily_pnl_target = $170,000-240,000
    
Strategy:
    priority = MAGNITUDE over CONSISTENCY
    position_limits = FLEXIBLE
    max_drawdown = AGGRESSIVE ($400,000+)
```

**Rationale:**
- 4.6x higher absolute returns
- Accepts higher volatility for better upside
- Suitable for risk-tolerant capital

---

## 6. Implementation Framework

### Step 1: Pre-Market Routine (Daily)
1. Check Fear & Greed Index at market open
2. Identify current sentiment: Fear, Greed, or Neutral
3. Load appropriate parameter set based on trader segment
4. Set position size limits: $2,500-7,500 depending on segment
5. Set trade frequency targets: 1,000-6,000 depending on segment
6. Review expected PnL ranges: $40,000-$320,000 depending on conditions

### Step 2: Intraday Monitoring
1. Track cumulative trades vs daily target
2. Monitor real-time win rate vs expected (37-42% range)
3. Check position concentration limits
4. Alert on parameter breaches
5. Compare actual PnL trajectory vs historical averages

### Step 3: End-of-Day Review
1. Log: sentiment, trades executed, win rate, PnL
2. Compare actual vs expected performance
3. Calculate sentiment-adjusted returns
4. Update 30-day rolling statistics
5. Flag any systematic deviations

### Step 4: Monthly Optimization
1. Review strategy performance by sentiment regime
2. Analyze if Fear days still outperform (currently 2.3x)
3. Check if frequency advantages persist (currently 3.3x)
4. Validate segment classifications
5. Adjust targets based on recent 90-day window
6. Backtest any parameter changes

---

## 7. Risk Considerations

### Limitations
1. **Statistical Power:** Only 77 trader-days analyzed; performance differences not significant (p>0.05)
2. **Sample Size:** 32 traders may not represent broader population
3. **Regime Dependency:** 72% of trades during Fear period may bias results
4. **Survivorship:** Data only includes active traders (excludes blown-up accounts)
5. **Overfitting:** Perfect model accuracy (100%) suggests overfitting on small test set
6. **Data Anomaly:** Long/short ratio during Greed shows extreme outlier (8.9B)

### Risk Mitigation
1. **Confidence Intervals:** Use 95% confidence intervals for all projections
2. **Conservative Sizing:** Use 50% of historical position sizes until pattern validates
3. **Stop Losses:** Implement at 2x historical volatility ($760,000 for Fear, $530,000 for Greed)
4. **Correlation:** Monitor inter-trader correlation; reduce size if >0.7
5. **Regime Detection:** Use 7-day rolling sentiment to smooth daily noise
6. **Validation:** Require 3-month validation period before full deployment

### Additional Safeguards
- Maximum single-day loss: $500,000 (2x historical std dev)
- Maximum position concentration: 20% of capital per symbol
- Correlation limits: No more than 3 highly correlated positions
- Regular stress testing: Simulate 2008, 2020 style crashes
- Emergency exit: Pre-defined liquidation triggers

---

## 8. Expected Outcomes

### Performance Improvements
- **Sentiment-Aware Trading:** 2.3x better performance on Fear days ($209K vs $91K)
- **Frequency Optimization:** 3.3x improvement by increasing to frequent trader level
- **Segment Alignment:** Up to 4.6x improvement by matching strategy to risk tolerance
- **Win Rate:** Achievable range 37-56% depending on strategy

### Behavioral Benefits
- Clear decision framework reduces emotional trading
- Systematic regime-based risk adjustment
- Measurable performance attribution by sentiment
- Objective criteria for strategy selection

### Realistic Expectations
Given current data:
- **Optimistic Scenario:** $300,000+ daily PnL (frequent trader, Fear day)
- **Base Case:** $150,000 daily PnL (balanced approach)
- **Conservative:** $50,000 daily PnL (low activity, Greed day)
- **Risk Range:** Daily volatility $250,000-$400,000

---

## 9. Conclusion

This analysis demonstrates measurable (though not statistically significant due to limited sample size) relationships between Bitcoin market sentiment and trader performance. The key findings are:

1. **Fear outperforms Greed:** 2.3x higher average returns ($209K vs $91K per day)
2. **Activity paradox:** Traders are 3.6x MORE active during Fear, contradicting conventional wisdom
3. **Frequency matters most:** Frequent traders outperform 3.3x across all conditions
4. **Segment-specific strategies:** Different trader types show 3-5x performance variations

### Statistical Caveats
- Performance differences NOT statistically significant (p=0.134)
- Small sample size (77 trader-days, 32 traders)
- High variance suggests larger dataset needed
- Results directionally consistent but require validation

---

## Appendices

### A. Statistical Tests
- Independent t-tests (Fear vs Greed comparisons)
- Feature correlation analysis
- Random Forest feature importance

### B. Model Details
- Algorithm: Random Forest Classifier
- Hyperparameters: 100 estimators, max_depth=10
- Validation: 80/20 chronological split
- Class balancing: Applied

### C. Key Metrics Summary

**By Sentiment:**
- Fear: $209,373 avg PnL, 41.6% win rate, 4,183 trades/day
- Greed: $90,989 avg PnL, 36.9% win rate, 1,169 trades/day

**By Segment:**
- Frequent traders: $234,182 avg PnL, 41.7% win rate
- Consistent winners: $37,895 avg PnL, 56.1% win rate

---

**Analysis Date:** February 12, 2026
**Dataset Period:** March 2023 - June 2025
**Sample Size:** 32 traders, 184,263 trades, 77 trader-days