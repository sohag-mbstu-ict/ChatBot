import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as palm
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os

 

class chatbot_functionality:
    def __init__(self,api):
        os.environ['GOOGLE_API_KEY'] = api
    
    def get_pdf_text(self,pdf_docs):
        text=""
        for pdf in pdf_docs:
            pdf_reader= PdfReader(pdf)
            for page in pdf_reader.pages:
                text+= page.extract_text()
        return  text

    def get_text_chunks(self,text):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        chunks = text_splitter.split_text(text)
        return chunks

    def get_vector_store(self,text_chunks):
        embeddings = GooglePalmEmbeddings()
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        return vector_store

    def get_conversational_chain(self,vector_store):
        llm=GooglePalm()
        memory = ConversationBufferMemory(memory_key = "chat_history", return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
        return conversation_chain

    def user_input(self,user_question):
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chatHistory = response['chat_history']
        for i, message in enumerate(st.session_state.chatHistory):
            if i%2 == 0:
                st.write("Human:🚺 ", i,message.content)
            else:
                st.write("response: ✔️", i,message.content)
    

    