import streamlit as st
import plotly.graph_objects as go
from utils.api_client import compare, report_compare

st.set_page_config(
    page_title="Compare Mutual Funds",
    page_icon="⚖",
    layout="wide"
)

st.title("⚖ Mutual Fund Comparison")
st.markdown("Compare two mutual funds and receive AI-powered investment insights.")

st.divider()

# ---------------------------------------------------
# Inputs
# ---------------------------------------------------

fund_1 = st.text_input(
    "Fund 1",
    value="SBI Small Cap Fund"
)

fund_2 = st.text_input(
    "Fund 2",
    value="HDFC Flexi Cap Fund"
)

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    compare_clicked = st.button(
        "🔍 Compare Funds",
        use_container_width=True
    )

with col_btn2:
    report_clicked = st.button(
        "📄 Generate Report",
        use_container_width=True
    )

# ---------------------------------------------------
# Compare Funds
# ---------------------------------------------------

if compare_clicked:

    with st.spinner("Comparing funds..."):
        result = compare(fund_1, fund_2)

    st.success("Comparison completed successfully!")

    # -------------------------
    # Prepare Data
    # -------------------------

    fund1 = result["fund_1"]
    fund2 = result["fund_2"]

    metrics1 = fund1["metrics"]
    metrics2 = fund2["metrics"]

    st.divider()

    # -------------------------
    # Fund Cards
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(fund1["scheme_name"])

        st.metric(
            "Latest NAV",
            f'₹ {metrics1.get("latest_nav")}'
        )

        st.metric(
            "1-Year Return",
            f'{metrics1.get("one_year_return_percent",0)} %'
        )

        st.metric(
            "3-Year CAGR",
            f'{metrics1.get("cagr_3y_percent",0)} %'
        )

    with col2:

        st.subheader(fund2["scheme_name"])

        st.metric(
            "Latest NAV",
            f'₹ {metrics2.get("latest_nav")}'
        )

        st.metric(
            "1-Year Return",
            f'{metrics2.get("one_year_return_percent",0)} %'
        )

        st.metric(
            "3-Year CAGR",
            f'{metrics2.get("cagr_3y_percent",0)} %'
        )

    st.divider()

    # -------------------------
    # Winner Card
    # -------------------------

    winner = result["summary"].split(" performed")[0]

    st.subheader("🏆 Winner")

    st.markdown(
        f"""
<div style="
background:#E8F5E9;
padding:20px;
border-radius:12px;
border-left:8px solid green;
">

<h2>🏆 {winner}</h2>

<p><b>Recommendation</b></p>

<ul>
<li>✔ Better recent performance</li>
<li>✔ Higher one-year return</li>
<li>✔ Recommended based on current comparison</li>
</ul>

</div>
""",
        unsafe_allow_html=True
    )

    st.info(result["summary"])

    st.divider()

    # -------------------------
    # KPI Cards
    # -------------------------

    diff = abs(
        metrics1.get("one_year_return_percent", 0)
        - metrics2.get("one_year_return_percent", 0)
    )

    better_cagr = (
        fund1["scheme_name"]
        if metrics1.get("cagr_3y_percent", 0)
        > metrics2.get("cagr_3y_percent", 0)
        else fund2["scheme_name"]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📈 1-Year Return Difference",
            f"{diff:.2f}%"
        )

    with col2:

        st.metric(
            "🏆 Better 3-Year CAGR",
            better_cagr
        )

    st.divider()

    # -------------------------
    # Plotly Chart
    # -------------------------

    st.subheader("📊 Performance Comparison")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name=fund1["scheme_name"],
            x=["1-Year Return", "3-Year CAGR"],
            y=[
                metrics1.get("one_year_return_percent", 0),
                metrics1.get("cagr_3y_percent", 0)
            ]
        )
    )

    fig.add_trace(
        go.Bar(
            name=fund2["scheme_name"],
            x=["1-Year Return", "3-Year CAGR"],
            y=[
                metrics2.get("one_year_return_percent", 0),
                metrics2.get("cagr_3y_percent", 0)
            ]
        )
    )

    fig.update_layout(
        title="Fund Performance Comparison",
        barmode="group",
        height=500,
        xaxis_title="Metric",
        yaxis_title="Return (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # -------------------------
    # AI Analysis
    # -------------------------

    st.subheader("🤖 AI Investment Recommendation")

    st.success(result["ai_analysis"])

# ---------------------------------------------------
# Generate Report
# ---------------------------------------------------

if report_clicked:

    with st.spinner("Generating report..."):
        report = report_compare(fund_1, fund_2)

    st.success("Report generated successfully!")

    st.json(report)