import streamlit as st
from utils.api_client import chat

st.title("Chat with Mutual Fund AI Agent")

user_id = st.text_input("User ID", value="santhosh")
message = st.text_area("Ask something about mutual funds", height=150)

if st.button("Send"):
    if message.strip():
        with st.spinner("Thinking..."):
            result = chat(user_id, message)
        st.subheader("Answer")
        st.write(result.get("answer", result))
