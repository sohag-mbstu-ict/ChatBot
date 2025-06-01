from langchain.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List

# Custom embedding wrapper using Hugging Face Sentence Transformers
class HuggingFaceEmbeddingWrapper(Embeddings):
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(texts)

    def embed_query(self, text: str) -> List[float]:
        return self.embeddings.embed_query(text)

# Method to create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddingWrapper()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

# Sample texts
x = 'What do squirrels eat?'
close_to_x = 'nuts and acorns'
different_from_x = 'This morning I woke up in San Francisco, and took a walk to the Bay Bridge. It was a good, sunny morning with no fog.'

# Create FAISS vector store
chunks = [x, close_to_x, different_from_x]
vector_store = get_vector_store(chunks)

# Search example
docs = vector_store.similarity_search(query="What do squirrels eat?", k=2)
for doc in docs:
    print("Match:", doc.page_content)