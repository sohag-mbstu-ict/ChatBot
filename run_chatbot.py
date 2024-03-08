import streamlit as st
import time
from chatbot import chatbot_functionality

st.set_page_config("ChatBot")
st.header("Chat with Multiple uploaded PDF 💬")
user_question = st.text_input("Ask a Question from the uploaded PDF Files")
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = None
    
    
api='AIzaSyCpeOogkzyWebU0JxyrPu2mC4zK6UKb4j8'
chatbot_obj = chatbot_functionality(api)  # create class instance



print("1111111111111111111111111111111111111111")
with st.sidebar:
    st.title("Settings")
    st.subheader("Upload your Documents")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Process Button", accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("Processing"):
            raw_text     = chatbot_obj.get_pdf_text(pdf_docs)        # get text from pdf files
            text_chunks  = chatbot_obj.get_text_chunks(raw_text)     # used chunk_size=1000, chunk_overlap=20
            vector_store = chatbot_obj.get_vector_store(text_chunks) #
            st.session_state.conversation = chatbot_obj.get_conversational_chain(vector_store)
            st.success("Done")
    
    
if user_question:
    chatbot_obj.user_input(user_question)
    
    