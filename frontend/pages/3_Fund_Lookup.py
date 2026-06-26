import streamlit as st
from utils.api_client import fund_lookup

st.title("Fund Lookup")

query = st.text_input("Search fund", value="HDFC Flexi Cap Fund")

if st.button("Lookup"):
    result = fund_lookup(query)
    st.json(result)
