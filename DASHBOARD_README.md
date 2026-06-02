# Dashboard

Quick way to explore the analysis without reading 30 pages.

## Run It

```bash
pip install streamlit plotly
streamlit run dashboard.py
```

Opens at `http://localhost:8501`

## What's Inside

5 tabs:
1. **Overview** - Executive summary, main metrics
2. **Sentiment Analysis** - Fear vs Greed deep dive
3. **Trader Segments** - How different traders perform
4. **Predictive Model** - Feature importance chart
5. **Strategies** - Actionable recommendations

Interactive charts - zoom, hover, filter by sentiment.

Uses sample data that matches the actual results. For production, plug in your real data.