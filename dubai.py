import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# 1. Page Configuration & Theme
st.set_page_config(page_title="Data Analyst RAMOS | Portfolio", layout="wide")

# Dark Mode CSS mifanaraka amin'ny Climate Shield
st.markdown("""
    <style>
    .stApp { background-color: #050A30; color: white; }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #050A30;
        color: #888888;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #1E2A44;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: Logo sy Branding
with st.sidebar:
    st.markdown("### 📊 Data Analyst RAMOS")
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=80) # Logo kely kisary (Icon)
    st.write("Specialist in Investment Frameworks & ESG Data.")
    st.divider()
    comparison_mode = st.checkbox("Show Side-by-Side Comparison", value=True)

# 3. Live Gold Price Data
@st.cache_data(ttl=3600)
def get_gold_price():
    try:
        gold = yf.Ticker("GC=F")
        return round(gold.history(period="1d")['Close'].iloc[-1], 2)
    except:
        return 2050.00

current_gold_price = get_gold_price()

# 4. Data Definition (Australia vs Dubai)
data_comparison = {
    "Region": ["Dubai", "Australia"],
    "Gold Reserves (Tons)": [5, 11000],
    "Projected ROI (%)": [25, 18],
    "Production Cost ($/oz)": [500, 1200]
}
df_comp = pd.DataFrame(data_comparison)

# 5. Header Section
st.title("⚒️ Global Resource Decision Framework")
st.write(f"**Live Market Gold Price:** ${current_gold_price}/oz | Analyzed by **RAMOSTAFY**")

# 6. Comparison Layout
if comparison_mode:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🇦🇪 Dubai Analysis")
        st.metric("Reserves", "5 Tons")
        st.metric("ROI", "25%", delta="High Efficiency")
        st.map(pd.DataFrame({'lat': [25.2048], 'lon': [55.2708]}), zoom=9)
    with col2:
        st.subheader("🇦🇺 Australia Analysis")
        st.metric("Reserves", "11,000 Tons")
        st.metric("ROI", "18%")
        st.map(pd.DataFrame({'lat': [-25.2744], 'lon': [133.7751]}), zoom=3)

st.divider()

# 7. Chart miaraka amin'ny Log Scale mba ho hita i Dubai
st.subheader("📊 Strategic Metric Comparison (Log Scale)")
fig_comp = px.bar(
    df_comp, x="Region", y=["Projected ROI (%)", "Gold Reserves (Tons)"],
    barmode="group", log_y=True, template="plotly_dark",
    color_discrete_map={"Projected ROI (%)": "#00CCFF", "Gold Reserves (Tons)": "#FFD700"}
)
fig_comp.update_traces(texttemplate='%{y}', textposition='outside')
st.plotly_chart(fig_comp, width='stretch')

# 8. Export & Footer
csv = df_comp.to_csv(index=False).encode('utf-8')
st.download_button("Download Comparison Report (CSV)", csv, "report_ramos.csv", "text/csv")

st.markdown(
    """
    <div class="footer">
        <p>Developed by <b>Data Analyst Hermann RAMOS</b> | © 2026 | Decision Intelligence for Mining & ESG</p>
    </div>
    """,
    unsafe_allow_html=True
)