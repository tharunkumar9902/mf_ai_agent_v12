import streamlit as st
from frontend.utils.api_client import history

st.title("Chat History")

user_id = st.text_input("User ID", value="santhosh")

if st.button("Load History"):
    result = history(user_id)
    st.json(result)
