import streamlit as st
from frontend.utils.api_client import compare, report_compare

st.title("Compare Mutual Funds")

fund_1 = st.text_input("Fund 1", value="SBI Small Cap Fund")
fund_2 = st.text_input("Fund 2", value="Parag Parikh Flexi Cap Fund")

col1, col2 = st.columns(2)

with col1:
    if st.button("Compare"):
        result = compare(fund_1, fund_2)
        st.json(result)

with col2:
    if st.button("Generate Report"):
        result = report_compare(fund_1, fund_2)
        st.json(result)
        st.info("Report files are generated inside the reports/ folder on the backend container/project.")
