import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Portfolio Analyzer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Portfolio Analyzer")

st.markdown(
    "Upload your mutual fund portfolio in CSV format."
)

uploaded_file = st.file_uploader(
    "Choose Portfolio CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Portfolio")

    st.dataframe(df, use_container_width=True)

    total = df["Amount"].sum()

    st.metric(
        "💰 Total Portfolio Value",
        f"₹ {total:,.0f}"
    )

    fig = px.pie(
        df,
        names="Fund",
        values="Amount",
        title="Portfolio Allocation"
    )

    st.plotly_chart(fig, use_container_width=True)

    largest = df.loc[df["Amount"].idxmax()]

    st.success(
        f"""
Largest Investment

Fund: **{largest['Fund']}**

Investment: **₹{largest['Amount']:,.0f}**
"""
    )