import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Debug mode
DEBUG = True

if DEBUG:
    st.sidebar.write("🔧 Debug Mode: ON")
    st.sidebar.write("Loading libraries...")

# Set page configuration
st.set_page_config(
    page_title="Trader Sentiment Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .fear-metric {
        border-left-color: #d62728;
    }
    .greed-metric {
        border-left-color: #2ca02c;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">📊 Trader Performance vs Market Sentiment Dashboard</p>', unsafe_allow_html=True)
st.markdown("**Analysis Period:** March 2023 - June 2025 | **32 Traders** | **184,263 Trades**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    
    # Navigation
    page = st.radio(
        "Navigate to:",
        ["📈 Overview", "🔍 Sentiment Analysis", "👥 Trader Segments", "🤖 Predictive Model", "💡 Strategies"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 Key Statistics")
    st.metric("Total Trades", "184,263")
    st.metric("Traders Analyzed", "32")
    st.metric("Analysis Days", "77")
    
    st.markdown("---")
    st.info("**Assignment:** Data Science Intern - Primetrade.ai")

# Sample data (in production, load from actual CSV or processed pickle)
# For demo, creating representative data based on your analysis results

@st.cache_data
def load_sample_data():
    """Create sample data matching your analysis results"""
    np.random.seed(42)
    
    # Simplified: Create 100 sample days instead of full date range
    n_samples = 100
    
    data = []
    for i in range(n_samples):
        # Assign sentiment (weighted to match your distribution)
        sentiment_choice = np.random.choice(
            ['Fear', 'Greed'],
            p=[0.73, 0.27]  # Simplified to just Fear/Greed
        )
        
        # Generate metrics based on sentiment
        if sentiment_choice == 'Fear':
            daily_pnl = np.random.normal(209373, 100000)
            win_rate = np.random.normal(41.59, 5)
            num_trades = int(np.random.normal(4183, 500))
            position_size = np.random.normal(5926, 1000)
        else:  # Greed
            daily_pnl = np.random.normal(90989, 80000)
            win_rate = np.random.normal(36.90, 5)
            num_trades = int(np.random.normal(1169, 300))
            position_size = np.random.normal(5637, 1000)
        
        data.append({
            'date': pd.Timestamp('2024-01-01') + pd.Timedelta(days=i),
            'sentiment': sentiment_choice,
            'daily_pnl': daily_pnl,
            'win_rate': max(0, min(100, win_rate)),
            'num_trades': max(1, num_trades),
            'avg_position_size': max(100, position_size)
        })
    
    return pd.DataFrame(data)

# Load data with error handling
try:
    df = load_sample_data()
    st.sidebar.success("✅ Data loaded successfully")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Filter to Fear and Greed only for main analysis
df_fear_greed = df[df['sentiment'].isin(['Fear', 'Greed'])].copy()

# =============================================================================
# PAGE: OVERVIEW
# =============================================================================
if page == "📈 Overview":
    st.header("📈 Executive Summary")
    
    # Key metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card fear-metric">', unsafe_allow_html=True)
        st.metric("Fear Day Avg PnL", "$209,373", delta="↑ 130% vs Greed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card greed-metric">', unsafe_allow_html=True)
        st.metric("Greed Day Avg PnL", "$90,989", delta="↓ vs Fear")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Fear Win Rate", "41.6%", delta="↑ 4.7pp")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Statistical Sig.", "p = 0.134", delta="Not significant")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main findings
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Key Findings")
        st.markdown("""
        1. **Fear days generate 2.3x higher PnL** ($209K vs $91K)
        2. **Trading activity 3.6x higher during Fear** (4,183 vs 1,169 trades/day)
        3. **Frequent traders outperform 3.3x** across all conditions
        4. **Sentiment is top predictor** (44.7% feature importance)
        """)
        
        st.info("⚠️ **Note:** Performance difference not statistically significant (p=0.134) due to small sample size (77 trader-days)")
    
    with col2:
        st.subheader("💡 Strategic Implications")
        st.markdown("""
        **Counterintuitive Discovery:**
        - Traders are MORE active during Fear (not less)
        - This high activity is associated with BETTER outcomes
        - Contradicts conventional "reduce activity during fear" wisdom
        
        **Recommended Actions:**
        1. Maintain/increase activity during Fear days
        2. Transition to frequent trading strategies (3.3x advantage)
        3. Use sentiment as primary next-day predictor
        """)
    
    # Interactive time series
    st.markdown("---")
    st.subheader("📊 Performance Over Time")
    
    # Aggregate by date and sentiment
    daily_agg = df_fear_greed.groupby(['date', 'sentiment']).agg({
        'daily_pnl': 'mean',
        'win_rate': 'mean',
        'num_trades': 'sum'
    }).reset_index()
    
    # Create interactive plot
    fig = go.Figure()
    
    for sentiment in ['Fear', 'Greed']:
        data = daily_agg[daily_agg['sentiment'] == sentiment]
        color = 'red' if sentiment == 'Fear' else 'green'
        
        fig.add_trace(go.Scatter(
            x=data['date'],
            y=data['daily_pnl'],
            mode='lines+markers',
            name=sentiment,
            line=dict(color=color, width=2),
            marker=dict(size=4)
        ))
    
    fig.update_layout(
        title="Daily PnL by Market Sentiment",
        xaxis_title="Date",
        yaxis_title="Average Daily PnL ($)",
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: SENTIMENT ANALYSIS
# =============================================================================
elif page == "🔍 Sentiment Analysis":
    st.header("🔍 Sentiment Impact Analysis")
    
    # Comparison table
    st.subheader("📊 Performance Comparison: Fear vs Greed")
    
    fear_data = df_fear_greed[df_fear_greed['sentiment'] == 'Fear']
    greed_data = df_fear_greed[df_fear_greed['sentiment'] == 'Greed']
    
    comparison_df = pd.DataFrame({
        'Metric': ['Average Daily PnL', 'Win Rate (%)', 'Trades per Day', 'Avg Position Size ($)'],
        'Fear': [
            f"${fear_data['daily_pnl'].mean():,.2f}",
            f"{fear_data['win_rate'].mean():.2f}%",
            f"{fear_data['num_trades'].mean():,.0f}",
            f"${fear_data['avg_position_size'].mean():,.2f}"
        ],
        'Greed': [
            f"${greed_data['daily_pnl'].mean():,.2f}",
            f"{greed_data['win_rate'].mean():.2f}%",
            f"{greed_data['num_trades'].mean():,.0f}",
            f"${greed_data['avg_position_size'].mean():,.2f}"
        ],
        'Difference': [
            f"{((fear_data['daily_pnl'].mean() / greed_data['daily_pnl'].mean() - 1) * 100):+.1f}%",
            f"{(fear_data['win_rate'].mean() - greed_data['win_rate'].mean()):+.2f}pp",
            f"{((fear_data['num_trades'].mean() / greed_data['num_trades'].mean() - 1) * 100):+.1f}%",
            f"{((fear_data['avg_position_size'].mean() / greed_data['avg_position_size'].mean() - 1) * 100):+.1f}%"
        ]
    })
    
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Interactive visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 PnL Distribution")
        
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=fear_data['daily_pnl'],
            name='Fear',
            marker_color='red',
            opacity=0.7,
            nbinsx=30
        ))
        
        fig.add_trace(go.Histogram(
            x=greed_data['daily_pnl'],
            name='Greed',
            marker_color='green',
            opacity=0.7,
            nbinsx=30
        ))
        
        fig.update_layout(
            barmode='overlay',
            xaxis_title='Daily PnL ($)',
            yaxis_title='Frequency',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Win Rate Distribution")
        
        fig = go.Figure()
        
        fig.add_trace(go.Box(
            y=fear_data['win_rate'],
            name='Fear',
            marker_color='red',
            boxmean='sd'
        ))
        
        fig.add_trace(go.Box(
            y=greed_data['win_rate'],
            name='Greed',
            marker_color='green',
            boxmean='sd'
        ))
        
        fig.update_layout(
            yaxis_title='Win Rate (%)',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Behavioral changes
    st.markdown("---")
    st.subheader("🔄 Behavioral Changes by Sentiment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Trading frequency
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=['Fear', 'Greed'],
            y=[fear_data['num_trades'].mean(), greed_data['num_trades'].mean()],
            marker_color=['red', 'green'],
            text=[f"{fear_data['num_trades'].mean():,.0f}", f"{greed_data['num_trades'].mean():,.0f}"],
            textposition='auto'
        ))
        
        fig.update_layout(
            title='Average Trades per Day',
            yaxis_title='Number of Trades',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.metric(
            "Activity Difference",
            f"{((fear_data['num_trades'].mean() / greed_data['num_trades'].mean() - 1) * 100):+.1f}%",
            delta="Fear vs Greed",
            help="Traders are 3.6x more active during Fear periods"
        )
    
    with col2:
        # Position sizing
        fig = go.Figure()
        
        fig.add_trace(go.Violin(
            y=fear_data['avg_position_size'],
            name='Fear',
            fillcolor='red',
            opacity=0.6,
            box_visible=True,
            meanline_visible=True
        ))
        
        fig.add_trace(go.Violin(
            y=greed_data['avg_position_size'],
            name='Greed',
            fillcolor='green',
            opacity=0.6,
            box_visible=True,
            meanline_visible=True
        ))
        
        fig.update_layout(
            title='Position Size Distribution',
            yaxis_title='Average Position Size ($)',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: TRADER SEGMENTS
# =============================================================================
elif page == "👥 Trader Segments":
    st.header("👥 Trader Segment Analysis")
    
    st.info("📊 **Segmentation Approach:** Traders classified by position size, trading frequency, and consistency")
    
    # Segment performance comparison
    segments_data = {
        'Segment': ['High Position', 'Low Position', 'Frequent', 'Infrequent', 'Consistent', 'Inconsistent'],
        'Avg Daily PnL ($)': [159290, 145446, 234182, 70555, 37895, 173567],
        'Win Rate (%)': [35.3, 43.9, 41.7, 37.5, 56.1, 36.5],
        'Fear PnL ($)': [278058, 140687, 324428, 94317, 45763, 239671],
        'Greed PnL ($)': [84630, 98469, 142173, 42498, 30026, 100514],
        'Category': ['Position Size', 'Position Size', 'Frequency', 'Frequency', 'Consistency', 'Consistency']
    }
    
    segments_df = pd.DataFrame(segments_data)
    
    # Segment selector
    category = st.selectbox(
        "Select Segment Category:",
        ['All', 'Position Size', 'Frequency', 'Consistency']
    )
    
    if category != 'All':
        display_df = segments_df[segments_df['Category'] == category]
    else:
        display_df = segments_df
    
    st.markdown("---")
    
    # Performance by segment
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Average Daily PnL by Segment")
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=display_df['Segment'],
            y=display_df['Avg Daily PnL ($)'],
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][:len(display_df)],
            text=display_df['Avg Daily PnL ($)'].apply(lambda x: f"${x:,.0f}"),
            textposition='auto'
        ))
        
        fig.update_layout(
            yaxis_title='Average Daily PnL ($)',
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Win Rate by Segment")
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=display_df['Segment'],
            y=display_df['Win Rate (%)'],
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][:len(display_df)],
            text=display_df['Win Rate (%)'].apply(lambda x: f"{x:.1f}%"),
            textposition='auto'
        ))
        
        fig.update_layout(
            yaxis_title='Win Rate (%)',
            height=400,
            xaxis_tickangle=-45
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Sentiment performance
    st.markdown("---")
    st.subheader("📊 Segment Performance by Sentiment")
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Fear Days',
        x=display_df['Segment'],
        y=display_df['Fear PnL ($)'],
        marker_color='red',
        text=display_df['Fear PnL ($)'].apply(lambda x: f"${x:,.0f}"),
        textposition='auto'
    ))
    
    fig.add_trace(go.Bar(
        name='Greed Days',
        x=display_df['Segment'],
        y=display_df['Greed PnL ($)'],
        marker_color='green',
        text=display_df['Greed PnL ($)'].apply(lambda x: f"${x:,.0f}"),
        textposition='auto'
    ))
    
    fig.update_layout(
        barmode='group',
        yaxis_title='Average Daily PnL ($)',
        height=500,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    st.markdown("---")
    st.subheader("💡 Key Insights by Segment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🎯 Position Size**")
        st.markdown("""
        - High position traders: **3.3x better during Fear**
        - Low position traders: **Higher win rates** (43.9% vs 35.3%)
        - Position sizing matters more in volatile markets
        """)
    
    with col2:
        st.markdown("**⚡ Frequency**")
        st.markdown("""
        - Frequent traders: **3.3x outperformance overall**
        - Advantage holds in both Fear and Greed
        - High activity = competitive edge
        """)
    
    with col3:
        st.markdown("**✅ Consistency**")
        st.markdown("""
        - Consistent winners: **56% win rate**
        - Lower absolute returns but stable
        - 7.8x lower volatility
        """)

# =============================================================================
# PAGE: PREDICTIVE MODEL
# =============================================================================
elif page == "🤖 Predictive Model":
    st.header("🤖 Next-Day Profitability Prediction")
    
    st.markdown("""
    **Model:** Random Forest Classifier  
    **Target:** Binary classification (Profitable / Unprofitable next day)  
    **Features:** Sentiment, trading metrics, behavioral patterns
    """)
    
    st.markdown("---")
    
    # Model performance
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "100.0%", help="Perfect classification on test set")
    
    with col2:
        st.metric("Precision", "100.0%", help="No false positives")
    
    with col3:
        st.metric("Recall", "100.0%", help="No false negatives")
    
    with col4:
        st.metric("F1-Score", "100.0", help="Harmonic mean of precision and recall")
    
    st.warning("⚠️ **Note:** Perfect accuracy suggests potential overfitting due to small test set (14 samples). Requires validation on larger dataset.")
    
    st.markdown("---")
    
    # Feature importance
    st.subheader("📊 Feature Importance Analysis")
    
    features = ['sentiment_fear', 'num_trades', 'win_rate', 'daily_pnl', 'pnl_volatility', 
                'long_short_ratio', 'frequent_trader', 'avg_position_size_usd', 'high_position']
    importance = [0.447369, 0.212189, 0.101005, 0.051923, 0.047127, 0.043404, 0.039587, 0.036142, 0.021253]
    
    feature_df = pd.DataFrame({
        'Feature': features,
        'Importance': importance
    }).sort_values('Importance', ascending=True)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=feature_df['Importance'],
        y=feature_df['Feature'],
        orientation='h',
        marker_color='#1f77b4',
        text=feature_df['Importance'].apply(lambda x: f"{x:.1%}"),
        textposition='auto'
    ))
    
    fig.update_layout(
        title='Feature Importance for Next-Day Profitability',
        xaxis_title='Importance Score',
        yaxis_title='Feature',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Key Findings")
        st.markdown("""
        1. **Sentiment is #1 predictor** (44.7% importance)
        2. **Trading frequency matters** (21.2% importance)
        3. **Win rate provides signal** (10.1% importance)
        4. **Position sizing less important** (3.6% importance)
        
        **Implication:** Focus on sentiment monitoring and activity levels for next-day predictions.
        """)
    
    with col2:
        st.subheader("💡 Practical Applications")
        st.markdown("""
        **Use this model to:**
        - Flag high-risk trading days
        - Adjust position sizing based on predicted outcomes
        - Optimize strategy selection for expected regime
        - Set realistic PnL expectations
        
        **Next steps:**
        - Validate on larger dataset (1000+ samples)
        - Add cross-validation
        - Test with real-time data
        """)

# =============================================================================
# PAGE: STRATEGIES
# =============================================================================
elif page == "💡 Strategies":
    st.header("💡 Actionable Trading Strategies")
    
    # Strategy selector
    strategy = st.selectbox(
        "Select Strategy to Explore:",
        ["Strategy 1: Sentiment-Aware Activity", "Strategy 2: Segment-Specific Positioning"]
    )
    
    st.markdown("---")
    
    if strategy == "Strategy 1: Sentiment-Aware Activity":
        st.subheader("📊 Strategy 1: Sentiment-Aware Activity Management")
        
        st.success("**Key Insight:** Traders are 3.6x MORE active during Fear, and this high activity is associated with BETTER outcomes.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 😨 During FEAR Days")
            st.markdown("""
            **Expected Performance:**
            - Average Daily PnL: **$209,373**
            - Win Rate: **41.6%**
            - Trading Volume: **4,183 trades/day**
            
            **Recommended Actions:**
            - ✅ MAINTAIN or INCREASE trading frequency
            - ✅ Normal position sizing
            - ✅ Expect higher volatility
            - ✅ Target 42% win rate
            
            **Rationale:**
            - Fear days generate 2.3x higher PnL
            - High activity correlated with better outcomes
            - Contradicts "reduce activity" conventional wisdom
            """)
        
        with col2:
            st.markdown("### 😁 During GREED Days")
            st.markdown("""
            **Expected Performance:**
            - Average Daily PnL: **$90,989**
            - Win Rate: **36.9%**
            - Trading Volume: **1,169 trades/day**
            
            **Recommended Actions:**
            - ⚠️ REDUCE trading frequency by 72%
            - ⚠️ Be more selective
            - ⚠️ Higher per-trade profit ($219 vs $101)
            - ⚠️ Target 37% win rate
            
            **Rationale:**
            - Fewer quality opportunities
            - Lower overall PnL potential
            - Focus on high-conviction setups
            """)
        
        st.markdown("---")
        
        # Implementation guide
        st.subheader("🛠️ Implementation Framework")
        
        st.markdown("""
        **Daily Routine:**
        1. Check Fear & Greed Index at market open
        2. Adjust trade frequency targets accordingly
        3. Set realistic PnL expectations
        4. Monitor performance vs benchmarks
        
        **Risk Management:**
        - Stop loss: 2x historical volatility ($760K Fear, $530K Greed)
        - Max daily loss: $500,000
        - Position concentration: 20% max per symbol
        """)
    
    else:  # Strategy 2
        st.subheader("📊 Strategy 2: Segment-Specific Positioning")
        
        st.info("**Approach:** Match trading strategy to trader profile for optimal risk-adjusted returns")
        
        # Segment selector
        segment = st.radio(
            "Select Your Trader Profile:",
            ["High Position Size", "Low Position Size", "Frequent Trader", "Infrequent Trader", "Consistent Winner"]
        )
        
        st.markdown("---")
        
        if segment == "High Position Size":
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 😨 Fear Days")
                st.markdown("""
                **Strategy:** AGGRESSIVE
                - Position size: MAXIMUM ($7,500/trade)
                - Expected PnL: **$278,000/day**
                - Win rate: 35%
                - Risk: HIGH REWARD
                
                **Why:** 3.3x outperformance during Fear vs Greed
                """)
            
            with col2:
                st.markdown("### 😁 Greed Days")
                st.markdown("""
                **Strategy:** CONSERVATIVE
                - Position size: REDUCED ($5,000/trade)
                - Expected PnL: **$85,000/day**
                - Win rate: 35%
                - Risk: LOWER RETURN
                
                **Why:** Reduced advantage in trending markets
                """)
        
        elif segment == "Frequent Trader":
            st.success("🌟 **Best Overall Performance:** Frequent traders outperform 3.3x across ALL conditions")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 😨 Fear Days")
                st.markdown("""
                **Target:** 6,000+ trades/day
                - Expected PnL: **$324,000/day**
                - Win rate: 42%
                - Status: ✅ OPTIMAL CONDITIONS
                """)
            
            with col2:
                st.markdown("### 😁 Greed Days")
                st.markdown("""
                **Target:** 3,000+ trades/day
                - Expected PnL: **$142,000/day**
                - Win rate: 41%
                - Status: ✅ STILL ADVANTAGEOUS
                """)
        
        elif segment == "Consistent Winner":
            st.markdown("""
            ### ✅ Consistent Winner Profile
            
            **Characteristics:**
            - Win rate: **56%** (highest)
            - Volatility: **$25,824** (lowest - 7.8x less than others)
            - Average PnL: **$37,895/day** (stable)
            
            **Strategy:**
            - Priority: CONSISTENCY over MAGNITUDE
            - Position limits: STRICT
            - Max drawdown: CONSERVATIVE (<$50,000)
            - Suitable for: Risk-averse capital
            
            **Performance by Sentiment:**
            - Fear: $45,763/day
            - Greed: $30,026/day
            - Maintains edge in both regimes
            """)
        
        else:
            st.markdown(f"""
            ### Profile: {segment}
            
            See the **👥 Trader Segments** page for detailed analysis of this profile.
            """)
    
    st.markdown("---")
    
    # Expected outcomes
    st.subheader("📈 Expected Outcomes")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Optimistic Scenario", "$300,000+/day", help="Frequent trader, Fear day")
    
    with col2:
        st.metric("Base Case", "$150,000/day", help="Balanced approach")
    
    with col3:
        st.metric("Conservative", "$50,000/day", help="Low activity, Greed day")

# Footer
st.markdown("---")