# Trader Sentiment Analysis

## What This Is

I analyzed 184,263 trades from 32 traders to see if Bitcoin market sentiment 
(Fear vs Greed) affects trading performance. Spoiler: it does.

## Quick Setup

1. Download CSVs from the Google Drive links in the assignment
2. `pip install -r requirements.txt`
3. Put CSVs in project folder: `bitcoin_sentiment.csv` and `trader_data.csv`
4. `jupyter notebook trader_sentiment_analysis.ipynb` and run all cells

Done. Takes ~10 minutes.

## What You'll Find

**Main findings:**
- Fear days: 2.3x higher returns ($209K vs $91K daily)
- Traders trade 3.6x more during Fear (counterintuitive!)
- Frequent traders win: 3.3x advantage
- Sentiment is the best predictor of profitable days

**Deliverables:**
- Jupyter notebook with full analysis
- 5 charts showing patterns
- 2 actionable trading strategies
- ML model for predicting profitable days
- Interactive Streamlit dashboard

## Files

- `trader_sentiment_analysis.ipynb` - The main analysis. Run this.
- `ANALYSIS_SUMMARY.md` - Detailed findings if you want more depth
- `dashboard.py` - Interactive Streamlit app (`streamlit run dashboard.py`)
- `charts/` - 5 visualizations
- `requirements.txt` - Python packages

## One Important Thing

The model has 100% accuracy on the test set, but that's because the test set was 
tiny (14 samples). Probably overfitted. Don't trust it blindly.

Same with the 2.3x performance difference. It's directional and interesting, but 
not statistically significant. Need more data to be sure.
