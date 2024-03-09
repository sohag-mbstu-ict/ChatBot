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
import time
import random
import string
 

class chatbot_functionality:
    def __init__(self,api):
        os.environ['GOOGLE_API_KEY'] = api
    
    def get_pdf_text(self,pdf_docs):
        text=""
        for pdf in pdf_docs:
            pdf_reader= PdfReader(pdf)
            for page in pdf_reader.pages:
                text+= page.extract_text()
        if(len(text)==0):
            return "Please upload suitable PDF"
        else:
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

    def generate_session_id(self):
        timestamp = int(time.time() * 1000)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        session_id = f"{timestamp}_{random_string}"
        return session_id

    def user_input(self, user_question):
        session_id = self.generate_session_id()
        start_time = time.time()  # Record start time
        
        if( st.session_state.conversation is not None):
            print("st.session_state.conversation  : ",st.session_state.conversation )
            try:
                response = st.session_state.conversation({'question': user_question})
                st.session_state.chatHistory = response['chat_history']
            
                end_time = time.time()  # Record end time
                response_time = end_time - start_time  # Calculate response time
                
                chat_history_with_session_id = []  # List to store messages with session ID

                for i, message in enumerate(st.session_state.chatHistory):
                    if i % 2 == 0:
                        chat_history_with_session_id.append({'question🚺': message.content})
                    else:
                        chat_history_with_session_id.append({'session_id': session_id, 'speaker': 'ChatBot ', 
                                                            'response_time' : response_time, 'response': message.content})
                
                st.write("Chat history with session ID:", chat_history_with_session_id)
            except:
                st.write("Query is not appropiate. Please Rerun the project and enter valid query (press top right 3 dots to Rerun) ")
        else:
            st.write("Bot: Please upload PDF files and click on the Upload PDF button first.")
    

    