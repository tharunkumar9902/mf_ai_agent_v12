import streamlit as st
import plotly.express as px
from utils.api_client import search_funds, fund_lookup

st.set_page_config(
    page_title="Portfolio Builder",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Portfolio Builder")

st.markdown(
    "Build your investment portfolio using live Mutual Fund data."
)

st.divider()

# -----------------------------------------------------
# Search Mutual Fund
# -----------------------------------------------------

query = st.text_input(
    "🔍 Search Mutual Fund",
    placeholder="Example: SBI Small Cap"
)

search_clicked = st.button(
    "Search Fund",
    use_container_width=True
)

if search_clicked:

    if not query.strip():

        st.warning("Please enter a mutual fund name.")

    else:

        with st.spinner("Searching mutual funds..."):

            results = search_funds(query)

        if not results:

            st.error("No matching mutual funds found.")

        else:

            st.success(f"{len(results)} matching funds found.")

            fund_names = [
                fund["schemeName"]
                for fund in results
            ]

            selected = st.selectbox(
                "Select Mutual Fund",
                fund_names
            )

            # ---------------------------------------
            # Load selected fund information
            # ---------------------------------------

            with st.spinner("Loading fund details..."):

                details = fund_lookup(selected)

            metrics = details["metrics"]

            st.divider()
            # -------------------------------------
            # Portfolio Session
            # -------------------------------------

            if "portfolio" not in st.session_state:
                st.session_state.portfolio = []
            st.subheader("📊 Fund Information")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Latest NAV",
                    metrics.get("latest_nav", 0)
                )

                st.metric(
                    "1 Month Return",
                    f'{metrics.get("one_month_return_percent",0)} %'
                )

            with col2:

                st.metric(
                    "6 Month Return",
                    f'{metrics.get("six_month_return_percent",0)} %'
                )

                st.metric(
                    "1 Year Return",
                    f'{metrics.get("one_year_return_percent",0)} %'
                )

            with col3:

                st.metric(
                    "3 Year CAGR",
                    f'{metrics.get("cagr_3y_percent",0)} %'
                )

                st.metric(
                    "Fund House",
                    details.get("fund_house", "N/A")
                )

            st.divider()

            st.subheader("💰 Investment")

            amount = st.number_input(
                "Investment Amount (₹)",
                min_value=1000,
                step=1000,
                value=10000
            )
if st.button(
    "➕ Add To Portfolio",
    use_container_width=True
):

    st.session_state.portfolio.append(
        {
            "Scheme Code": details["scheme_code"],
            "Fund": selected,
            "Fund House": details["fund_house"],
            "Amount": amount,
            "Latest NAV": metrics["latest_nav"]
        }
    )

    st.success("Fund added successfully!")
    # ---------------------------------------------------
    # Portfolio
    # ---------------------------------------------------

if st.session_state.portfolio:
    st.divider()

    st.subheader("📂 My Portfolio")

    import pandas as pd

    df = pd.DataFrame(st.session_state.portfolio)

    st.dataframe(
        df,
        use_container_width=True
    )

    total = df["Amount"].sum()

    st.metric(
        "💰 Total Investment",
        f"₹{total:,.0f}"
    )
    st.divider()

    st.subheader("📊 Portfolio Allocation")

    fig = px.pie(
        df,
        names="Fund",
        values="Amount",
        title="Investment Allocation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )