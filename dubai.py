import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import numpy as np

# ======================================================
# 1. PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="RAMOS | Enterprise Decision Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# 2. ENTERPRISE THEME (BOARD-LEVEL)
# ======================================================
st.markdown("""
<style>
.stApp { background-color: #050A30; color: white; }
h1, h2, h3 { color: #E5E7EB; }
small { color: #9CA3AF; }
.card {
    background-color: #0B133F;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1E2A44;
}
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #050A30;
    border-top: 1px solid #1E2A44;
    text-align: center;
    padding: 10px;
    font-size: 13px;
    color: #9CA3AF;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# 3. SIDEBAR – EXECUTIVE CONTROLS
# ======================================================
with st.sidebar:
    st.markdown("## 🧠 RAMOS Intelligence")
    st.caption("Enterprise Decision Intelligence")
    st.caption("Mining • Trading • ESG • Strategy")
    st.divider()

    region = st.selectbox("🌍 Region", ["Dubai", "Australia"])
    horizon = st.selectbox("⏳ Investment Horizon", ["Short-term", "Mid-term", "Long-term"])
    risk = st.selectbox("⚠️ Risk Appetite", ["Low", "Medium", "High"])

# ======================================================
# 4. LIVE GOLD PRICE
# ======================================================
@st.cache_data(ttl=3600)
def gold_price():
    try:
        gold = yf.Ticker("GC=F")
        return round(gold.history(period="1d")["Close"].iloc[-1], 2)
    except:
        return 2050.00

price = gold_price()

# ======================================================
# 5. ENTERPRISE DATA MODEL
# ======================================================
df = pd.DataFrame({
    "Region": ["Dubai", "Australia"],
    "Reserves": [5, 11000],
    "ROI": [25, 18],
    "Cost": [500, 1200],
    "Risk_Profile": ["Low–Medium", "Low"],
    "Strategic_Role": ["Trading Hub", "Strategic Reserve"],
    "Lat": [25.2048, -25.2744],
    "Lon": [55.2708, 133.7751]
})

row = df[df["Region"] == region].iloc[0]

# ======================================================
# 6. HEADER
# ======================================================
st.title("⚒️ Enterprise Resource Decision Intelligence")
st.markdown(
    f"""
    **Live Gold Price:** `${price} / oz`  
    _Board-level analytics designed by **Hermann RAMOS**_
    """
)

st.divider()

# ======================================================
# 7. EXECUTIVE KPI CARDS
# ======================================================
k1, k2, k3, k4 = st.columns(4)

k1.markdown(f"""
<div class="card">
<h3>🪙 Reserves</h3>
<b>{row.Reserves:,} Tons</b><br>
<small>Physical Asset Base</small>
</div>
""", unsafe_allow_html=True)

k2.markdown(f"""
<div class="card">
<h3>📈 ROI</h3>
<b>{row.ROI}%</b><br>
<small>Projected Return</small>
</div>
""", unsafe_allow_html=True)

k3.markdown(f"""
<div class="card">
<h3>🏭 Cost</h3>
<b>${row.Cost} / oz</b><br>
<small>Production Economics</small>
</div>
""", unsafe_allow_html=True)

k4.markdown(f"""
<div class="card">
<h3>⚠️ Risk</h3>
<b>{row.Risk_Profile}</b><br>
<small>Operational & Market</small>
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================================================
# 8. DECISION ENGINE (EXPLAINABLE)
# ======================================================
def decision_engine(region, horizon, risk):
    if region == "Dubai" and horizon == "Short-term":
        return "STRONG ALLOCATION", (
            "Dubai offers liquidity, low production cost, "
            "and fast capital rotation. Optimized for trading desks."
        )
    if region == "Australia" and horizon == "Long-term":
        return "STRATEGIC HOLD", (
            "Australia provides supply security, reserve depth, "
            "and long-term asset preservation."
        )
    if risk == "Low":
        return "CONSERVATIVE STRATEGY", (
            "Preference for stable reserves and predictable output."
        )
    return "BALANCED STRATEGY", (
        "Diversified exposure recommended to balance yield and stability."
    )

decision, rationale = decision_engine(region, horizon, risk)

st.success(f"### 🧭 Board Recommendation: **{decision}**")
st.markdown(f"📘 **Rationale:** {rationale}")

st.info(f"🎯 **Strategic Role:** {row.Strategic_Role}")

st.divider()

# ======================================================
# 9. GEOGRAPHIC CONTEXT
# ======================================================
st.subheader("🌍 Geographic Footprint")
st.map(
    pd.DataFrame({"lat": [row.Lat], "lon": [row.Lon]}),
    zoom=9 if region == "Dubai" else 3
)

# ======================================================
# 10. MARKET SIGNAL – GOLD TREND
# ======================================================
st.subheader("📈 Market Signal – Gold Price (30 Days)")

dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
trend = price + np.random.normal(0, 12, len(dates))
trend_df = pd.DataFrame({"Date": dates, "Price": trend})

fig_trend = px.line(
    trend_df,
    x="Date",
    y="Price",
    template="plotly_dark",
    labels={"Price": "USD / oz"}
)

st.plotly_chart(fig_trend, width="stretch")

# ======================================================
# 11. STRATEGIC COMPARISON
# ======================================================
st.subheader("📊 Strategic Comparison Overview")

fig = px.bar(
    df,
    x="Region",
    y=["ROI", "Reserves"],
    barmode="group",
    log_y=True,
    template="plotly_dark",
    color_discrete_map={"ROI": "#00E5FF", "Reserves": "#FFD700"}
)

st.plotly_chart(fig, width="stretch")

# ======================================================
# 12. EXPORT
# ======================================================
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "📥 Download Enterprise Dataset",
    csv,
    "enterprise_decision_dataset.csv",
    "text/csv"
)

# ======================================================
# 13. FOOTER
# ======================================================
st.markdown("""
<div class="footer">
<b>Hermann RAMOS</b> | Enterprise Decision Intelligence Architect  
© 2026 – Mining • Trading • ESG • Strategy
</div>
""", unsafe_allow_html=True)
