# Streamlit Dashboard - Quick Start

## 🚀 Running the Dashboard

### Installation
```bash
pip install streamlit plotly
```

### Launch Dashboard
```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## 📊 Dashboard Features

### 5 Interactive Pages:

1. **📈 Overview** - Executive summary with key metrics and trends
2. **🔍 Sentiment Analysis** - Deep dive into Fear vs Greed performance
3. **👥 Trader Segments** - Segment-specific performance analysis
4. **🤖 Predictive Model** - Feature importance and model insights
5. **💡 Strategies** - Actionable trading recommendations

### Interactive Elements:

- **Live filtering** by sentiment and trader segment
- **Hover tooltips** for detailed information
- **Dynamic charts** using Plotly
- **Metric cards** with color-coded insights
- **Responsive layout** for all screen sizes

## 📝 Notes

- Dashboard uses **sample data** representative of the analysis results
- All metrics match the actual analysis findings
- For production use, connect to your actual data files
- Charts are fully interactive (zoom, pan, export)

## 🎨 Customization

To use your actual data instead of sample data:
1. Load your processed CSV files in the `load_sample_data()` function
2. Update the date ranges and distributions
3. Connect to your saved model for predictions

Enjoy exploring the insights! 📊