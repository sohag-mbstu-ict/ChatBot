import streamlit as st
from chatbot import chatbot_functionality  # Updated import

st.set_page_config(page_title="ChatBot")
st.header("Chat with Multiple Uploaded PDFs 💬")

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:  # Fixed to match chatbot.py
    st.session_state.chat_history = None

# Input for API key
api_key = st.text_input("Enter Google API Key", type="password", value="AIzaSyBExPddjZrh9VwycHjFtwEGgOaVnjJu3Yo")

# Initialize chatbot
if api_key:
    try:
        chatbot_obj = chatbot_functionality(api_key)
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {e}")
        st.stop()
else:
    st.error("Please enter a valid Google API Key.")
    st.stop()

with st.sidebar:
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Upload PDF Button", accept_multiple_files=True, type="pdf")
    if st.button("Upload PDF"):
        if pdf_docs:
            with st.spinner("Processing..."):
                raw_text = chatbot_obj.get_pdf_text(pdf_docs)
                if "Error" in raw_text or "Please upload" in raw_text:
                    st.error(raw_text)
                else:
                    text_chunks = chatbot_obj.get_text_chunks(raw_text)
                    vector_store = chatbot_obj.get_vector_store(text_chunks)
                    if vector_store:
                        st.session_state.conversation = chatbot_obj.get_conversational_chain(vector_store)
                        if st.session_state.conversation:
                            st.success("Done")
                        else:
                            st.error("Failed to create conversational chain.")
                    else:
                        st.error("Failed to create vector store.")
        else:
            st.error("Please upload at least one PDF file.")

user_question = st.text_input("Ask a Question from the Uploaded PDF Files")
if user_question and st.button("Submit Question"):
    with st.spinner("Generating response..."):
        chatbot_obj.user_input(user_question)