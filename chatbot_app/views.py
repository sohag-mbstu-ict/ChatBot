from django.shortcuts import render
from django.http import HttpResponse
import streamlit as st
import time
import subprocess
from chatbot_app.chatbot import chatbot_functionality

def index(request):
    # Command to run the Streamlit app
    command = ['streamlit', 'run', 'run_chatbot.py']
    
    # Run the Streamlit app as a subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Read the output of the Streamlit app
    output, _ = process.communicate()
    

