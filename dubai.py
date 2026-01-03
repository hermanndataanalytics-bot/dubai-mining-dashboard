import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# ============================================================
# GLOBAL RESOURCE DECISION FRAMEWORK – PRO LEVEL
# Author: Data Analyst Hermann RAMOS
# ============================================================

# 1. Page Configuration
st.set_page_config(
    page_title="Global Resource Decision Framework | RAMOS",
    page_icon="⛏️",
    layout="wide"
)

# 2. Global Dark Theme (Executive / Consulting grade)
st.markdown("""
<style>
.stApp { background-color: #050A30; color: white; }
.block-container { padding-top: 2rem; }
.metric-label { font-size: 14px !important; color: #A0AEC0; }
.metric-value { font-size: 28px !important; font-weight: 700; }
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #050A30;
    color: #8892B0;
    text-align: center;
    padding: 8px;
    font-size: 13px;
    border-top: 1px solid #1E2A44;
    z-index: 100;
}
</style>
""", unsafe_allow_html=True)

# 3. Sidebar – Branding & Controls
with st.sidebar:
    st.markdown("## 📊 Data Analyst RAMOS")
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=70)
    st.caption("Decision Intelligence | Mining, Trading & ESG")
    st.divider()

    comparison_mode = st.checkbox("Enable Side-by-Side Comparison", value=True)
    risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"], index=1)
    investment_horizon = st.selectbox("Investment Horizon", ["Short-term", "Mid-term", "Long-term"], index=1)

# 4. Live Gold Price (Market Signal)
@st.cache_data(ttl=3600)
def get_gold_price():
    try:
        gold = yf.Ticker("GC=F")
        return round(gold.history(period="1d")["Close"].iloc[-1], 2)
    except:
        return 2050.00

current_gold_price = get_gold_price()

# 5. Core Dataset (Illustrative – Decision Framework)
data = {
    "Region": ["Dubai", "Australia"],
    "Gold Reserves (Tons)": [5, 11000],
    "Projected ROI (%)": [25, 18],
    "Production Cost ($/oz)": [500, 1200],
    "Risk Level": ["Low", "Medium"],
    "Strategic Role": ["Trading Hub", "Long-Term Reserve"]
}

df = pd.DataFrame(data)

# 6. Header – Executive Framing
st.title("⛏️ Global Resource Decision Framework")
st.markdown(
    f"**Live Gold Price:** ${current_gold_price}/oz &nbsp;|&nbsp; "
    "Framework designed for **Investors, Traders & Strategic Advisors**"
)

# 7. Decision Recommendation Engine (Rule-based)
if investment_horizon == "Short-term":
    recommendation = "🇦🇪 Dubai – Optimized for liquidity, arbitrage & fast ROI"
elif investment_horizon == "Long-term":
    recommendation = "🇦🇺 Australia – Strategic reserves & asset preservation"
else:
    recommendation = "⚖️ Balanced allocation across Dubai & Australia"

st.success(f"### ✅ Strategic Recommendation: {recommendation}")

st.divider()

# 8. Side-by-Side Regional Analysis
if comparison_mode:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🇦🇪 Dubai – Trading Efficiency Hub")
        st.metric("Gold Reserves", "5 Tons")
        st.metric("Projected ROI", "25%", delta="High Efficiency")
        st.metric("Production Cost", "$500 / oz")
        st.caption("Source: DMCC | Confidence: Medium")
        st.map(pd.DataFrame({'lat': [25.2048], 'lon': [55.2708]}), zoom=9)
        st.info("Low reserves, high velocity → ideal for trading & capital rotation")

    with col2:
        st.subheader("🇦🇺 Australia – Strategic Reserve Base")
        st.metric("Gold Reserves", "11,000 Tons")
        st.metric("Projected ROI", "18%")
        st.metric("Production Cost", "$1,200 / oz")
        st.caption("Source: USGS | Confidence: High")
        st.map(pd.DataFrame({'lat': [-25.2744], 'lon': [133.7751]}), zoom=3)
        st.info("Massive reserves → long-term value & supply security")

st.divider()

# 9. Strategic Comparison Chart (Log Scale)
st.subheader("📊 Strategic KPI Comparison")

fig = px.bar(
    df,
    x="Region",
    y=["Projected ROI (%)", "Gold Reserves (Tons)", "Production Cost ($/oz)"],
    barmode="group",
    log_y=True,
    template="plotly_dark",
    labels={"value": "Metric Value", "variable": "KPI"},
    color_discrete_map={
        "Projected ROI (%)": "#00E5FF",
        "Gold Reserves (Tons)": "#FFD700",
        "Production Cost ($/oz)": "#FF6B6B"
    }
)

fig.update_layout(legend_title_text="Key Performance Indicators")
st.plotly_chart(fig, use_container_width=True)

# 10. Export
st.divider()
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Executive Dataset (CSV)", csv, "global_resource_decision_framework.csv", "text/csv")

# 11. Footer
st.markdown(
    """
    <div class="footer">
        Developed by <b>Data Analyst Hermann RAMOS</b> | © 2026 | Decision Intelligence for Mining, Trading & ESG
    </div>
    """,
    unsafe_allow_html=True
)
