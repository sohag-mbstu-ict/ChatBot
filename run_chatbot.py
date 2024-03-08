import streamlit as st
import google.generativeai as palm


st.set_page_config("ChatBot")
st.header("Chat with Multiple uploaded PDF 💬")
user_question = st.text_input("Ask a Question from the uploaded PDF Files")
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = None

    
    
    
    