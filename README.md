
## Deployment to streamlit.io
I have deployed this app to https://streamlit.io/ free server.  The link is : https://chatbot-r7xbxre856fudvodqt8bul.streamlit.app/


## Dependencies:
```bash
google-generativeai==0.4.0
PyPDF2==3.0.1
langchain==0.0.339
streamlit==1.32.0
faiss-cpu==1.8.0
django==4.2.11 
```

## Installation and run this project

```bash
git clone git@github.com:sohag-mbstu-ict/ChatBot.git
cd ChatBot
pip install -r requirements.txt
python manage.py runserver
```


# Architecture of LangChain
![](https://github.com/sohag-mbstu-ict/ChatBot/blob/main/Screenshots/LangChain_architecture.png)


## LangChain's key components and functionalities

LangChain is a framework for building conversational AI systems developed by Google. It provides tools and libraries for various natural language processing tasks, such as text embedding, language modeling, and conversational retrieval. 

### Text Embeddings:
LangChain offers tools for generating embeddings (vector representations) of text data. These embeddings capture semantic similarities between words and sentences, enabling advanced natural language understanding tasks.

### Language Models (LLMs):
LangChain includes pre-trained language models (LLMs) that can generate high-quality responses to user queries. These models are trained on large corpora of text data and are fine-tuned for specific conversational tasks.

### Vector Stores:
Vector stores are data structures optimized for efficient retrieval of text embeddings. LangChain provides vector store implementations that enable fast lookup of similar text passages based on their embeddings.

### Conversational Retrieval Chains:
A conversational retrieval chain is a pipeline that combines a language model with a vector store to retrieve relevant responses to user queries. LangChain provides tools for building and customizing retrieval chains tailored to specific conversational use cases.

### Memory Mechanisms:
LangChain includes memory mechanisms for storing and recalling previous interactions in a conversation. These mechanisms enable context-aware responses and help maintain coherence in long conversations.

### Integration with External Systems:
LangChain is designed to integrate seamlessly with other AI systems and applications. It provides APIs and interfaces for interacting with external data sources, allowing developers to incorporate LangChain-powered chatbots into their existing workflows


## Chat with Multiple PDF
Django and Streamlit user interface is used to upload multiple PDF files and ask questions.


## Procedure to upload PDF
![](https://github.com/sohag-mbstu-ict/ChatBot/blob/main/Screenshots/upload_pdf.png)

Used Streamlit to create a user interface where users can upload multiple PDF files and ask questions. Users can provide text input boxes for users to enter questions. Used Python libraries such as PyPDF2 to extract text from the uploaded PDF files. Process each PDF file individually to extract its text content.

## Chat with the pdf file
![](https://github.com/sohag-mbstu-ict/ChatBot/blob/main/Screenshots/query1.png)

This figure shows a simple interaction between the user and the chatbot, where the chatbot provides information in response to the user's query about SQL. The session ID helps keep track of the conversation context and history for future reference or analysis.

## Chat with the pdf file
![](https://github.com/sohag-mbstu-ict/ChatBot/blob/main/Screenshots/chat_with_multiple_pdf.png)

Overall, chatting with multiple PDFs using PaLM 2 and LangChain enables users to access comprehensive information in a conversational manner, leveraging advanced language understanding capabilities to provide accurate and personalized responses.


