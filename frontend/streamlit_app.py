import streamlit as st

st.set_page_config(
    page_title="AI Mutual Fund Advisor",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Mutual Fund Advisor")
st.markdown("### Intelligent Mutual Fund Analysis using AI + MFAPI + Ollama")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🤖 AI Status",
        value="Online"
    )

with col2:
    st.metric(
        label="📈 MFAPI",
        value="Connected"
    )

with col3:
    st.metric(
        label="🐳 Docker",
        value="Running"
    )

with col4:
    st.metric(
        label="🗄 Database",
        value="Connected"
    )

st.divider()

st.subheader("🚀 Quick Actions")

c1, c2 = st.columns(2)

with c1:
    st.info("🔍 Search Mutual Funds")

    st.write(
        """
Use the **Fund Lookup** page to:

- Search any mutual fund
- View latest NAV
- Check returns
- Analyze fund performance
"""
    )

with c2:
    st.info("⚖ Compare Funds")

    st.write(
        """
Use the **Compare Funds** page to:

- Compare two funds
- View performance metrics
- Get AI recommendations
"""
    )

st.divider()

st.subheader("✨ Features")

st.success("✅ Live Mutual Fund Data (MFAPI)")
st.success("✅ AI Investment Analysis (Ollama)")
st.success("✅ Mutual Fund Comparison")
st.success("✅ Historical NAV Analysis")
st.success("✅ Chat Assistant")
st.success("✅ Docker Deployment")

st.divider()

st.caption("Built with ❤️ using FastAPI • Streamlit • Docker • Ollama")