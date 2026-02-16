# Trader Performance vs Market Sentiment Analysis

## 📋 Project Overview

This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed) and trader performance on Hyperliquid. The analysis uncovers actionable patterns that can inform smarter trading strategies.

## 🎯 Objectives

1. **Performance Analysis**: Determine if trader PnL, win rates, and risk metrics differ between Fear and Greed market days
2. **Behavioral Analysis**: Identify how traders adjust their behavior (leverage, frequency, position sizing) based on sentiment
3. **Segmentation**: Categorize traders into meaningful segments and analyze their sentiment-specific performance
4. **Strategy Development**: Generate actionable trading rules based on data-driven insights
5. **Predictive Modeling** (Bonus): Build a model to predict next-day trader profitability

## 📊 Datasets

### 1. Bitcoin Market Sentiment
- **Columns**: Date, Classification (Fear/Greed)
- **Source**: [Google Drive Link](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing)

### 2. Historical Trader Data (Hyperliquid)
- **Columns**: account, symbol, executionPrice, size, side, time, startPosition, event, closedPnL, leverage, etc.
- **Source**: [Google Drive Link](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing)

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download this repository**
```bash
git clone <repository-url>
cd trader-sentiment-analysis
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Download the datasets**
   - Download both CSV files from the Google Drive links above
   - Place them in the project root directory
   - Rename them to:
     - `bitcoin_sentiment.csv`
     - `trader_data.csv`

### Required Python Packages
```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
scipy>=1.11.0
jupyter>=1.0.0
```

## 🚀 How to Run

### Option 1: Jupyter Notebook (Recommended)
```bash
jupyter notebook trader_sentiment_analysis.ipynb
```
Then run all cells sequentially (Cell → Run All)

### Option 2: Python Script
```bash
python trader_sentiment_analysis.py
```

## 📁 Project Structure

```
trader-sentiment-analysis/
│
├── trader_sentiment_analysis.ipynb    # Main analysis notebook
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── ANALYSIS_SUMMARY.md               # Detailed findings and insights
├── DASHBOARD_README.md
├── dashboard.py                      # Streamlit dashboard
│
├── charts/                           # Generated visualizations
│   ├── chart1_performance_by_sentiment.png
│   ├── chart2_behavior_by_sentiment.png
│   ├── chart3_segment_analysis.png
│   ├── chart4_temporal_patterns.png
│   └── chart5_predictive_model.png
│
└── data/                             # Data files (not included)
    ├── bitcoin_sentiment.csv         # Download from Google Drive
    └── trader_data.csv               # Download from Google Drive
```

## 📈 Analysis Workflow

### Part A: Data Preparation
1. Load and inspect both datasets
2. Document data quality (missing values, duplicates, data types)
3. Convert timestamps and align datasets by date
4. Create key trading metrics:
   - Daily PnL per trader
   - Win rate
   - Trade frequency
   - Leverage distribution
   - Long/short ratio
   - Position sizes

### Part B: Core Analysis
1. **Performance Comparison**: Statistical analysis of PnL, win rates, and volatility across Fear vs Greed days
2. **Behavioral Changes**: Examination of leverage usage, trading frequency, and risk-taking patterns
3. **Trader Segmentation**: Identification of 3 key segments:
   - High leverage vs Low leverage traders
   - Frequent vs Infrequent traders
   - Consistent winners vs Inconsistent traders
4. **Visual Insights**: 4+ comprehensive charts showing key patterns

### Part C: Strategy Development
1. Sentiment-based leverage adjustment rules
2. Adaptive trading frequency recommendations
3. Segment-specific strategy guidelines
4. Implementation framework

### Bonus Features
1. **Predictive Model**: Random Forest classifier to predict next-day profitability
2. **Feature Importance Analysis**: Identify key drivers of trading success
3. **Temporal Pattern Analysis**: Track performance trends over time

## 🔍 Key Insights

### Performance Patterns
- Quantified PnL differences between Fear and Greed days
- Statistical significance testing of performance metrics
- Win rate analysis across sentiment regimes

### Behavioral Adaptations
- Leverage usage varies significantly by sentiment
- Trading frequency shows clear sentiment-based patterns
- Position sizing strategies differ between Fear and Greed

### Segment-Specific Findings
- High-leverage traders show distinct sentiment sensitivity
- Frequent traders outperform in specific sentiment conditions
- Consistent winners maintain edge through adaptation

## 💡 Actionable Strategies

### Strategy 1: Sentiment-Based Leverage Management
- **Fear Days**: Reduce leverage to 50-70% of normal levels
- **Greed Days**: Maintain or slightly increase leverage
- **Target**: Optimize risk-adjusted returns

### Strategy 2: Adaptive Trading Frequency
- **Fear Days**: Reduce trade count by 30-40%, focus on high-conviction setups
- **Greed Days**: Normal/increased frequency acceptable with discipline
- **Target**: Avoid overtrading and capitalize on opportunities

## 📊 Visualizations

All charts are saved in high resolution (300 DPI) in the `charts/` directory:

1. **Performance by Sentiment**: Distribution of PnL, win rates, and volatility
2. **Behavioral Changes**: Leverage, frequency, and position sizing patterns
3. **Segment Analysis**: Performance breakdown by trader segments
4. **Temporal Patterns**: Time-series analysis of market behavior
5. **Predictive Model**: Feature importance and model performance

## 🎓 Methodology

### Statistical Approach
- Independent t-tests for group comparisons
- Confidence intervals for performance metrics
- Non-parametric tests where distributions are skewed

### Machine Learning
- Random Forest for classification
- Cross-validation for model robustness
- Feature importance analysis for interpretability

### Data Quality
- Comprehensive missing value handling
- Duplicate detection and removal
- Outlier analysis and treatment

## 🎨 Interactive Dashboard

An interactive Streamlit dashboard is included for exploring the analysis results.

### Quick Start
```bash
pip install streamlit plotly
streamlit run dashboard.py
```

See [DASHBOARD_README.md](DASHBOARD_README.md) for detailed features and customization options.

## 🔧 Troubleshooting

### Common Issues

**Issue**: "File not found" error
- **Solution**: Ensure CSV files are in the correct location and properly named

**Issue**: Package import errors
- **Solution**: Run `pip install -r requirements.txt` again

**Issue**: Memory errors with large datasets
- **Solution**: Process data in chunks or increase available RAM

**Issue**: Plots not displaying
- **Solution**: Ensure matplotlib backend is configured correctly

## 📧 Contact

For questions or issues with this analysis, please contact:
- **Email**: battulapoojitha61@gmail.com
- **GitHub**: Poojitha47672

---
