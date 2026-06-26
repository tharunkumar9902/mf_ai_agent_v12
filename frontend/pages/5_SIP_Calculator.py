import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="SIP Calculator",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SIP Investment Calculator")
st.markdown("Calculate the future value of your SIP investment.")

st.divider()

monthly = st.number_input(
    "Monthly Investment (₹)",
    min_value=500,
    value=5000,
    step=500
)

years = st.slider(
    "Investment Period (Years)",
    1,
    40,
    10
)

rate = st.slider(
    "Expected Annual Return (%)",
    1.0,
    20.0,
    12.0
)

if st.button("📈 Calculate SIP", use_container_width=True):

    monthly_rate = rate / 12 / 100
    months = years * 12

    future_value = monthly * (
        ((1 + monthly_rate) ** months - 1)
        / monthly_rate
    ) * (1 + monthly_rate)

    invested = monthly * months
    profit = future_value - invested

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💰 Future Value",
            f"₹ {future_value:,.0f}"
        )

    with col2:
        st.metric(
            "📥 Total Invested",
            f"₹ {invested:,.0f}"
        )

    with col3:
        st.metric(
            "📈 Estimated Profit",
            f"₹ {profit:,.0f}"
        )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["Invested", "Future Value"],
            y=[invested, future_value]
        )
    )

    fig.update_layout(
        title="Investment Growth",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        f"""
If you invest **₹{monthly:,} every month** for **{years} years**
at an expected return of **{rate}%**, your investment could
grow to approximately **₹{future_value:,.0f}**.
"""
    )