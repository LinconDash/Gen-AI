import os
import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


os.environ["HF_HOME"] = "D:/huggingface_cache"  
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

available_documents = [
    "Cat is a domestic animal",
    "Tiger is a wild animal",
    "Dogs are domestic animals",
    "Elephants are wild animals"
]

doc_embeddings = model.embed_documents(available_documents)

user_query = str(input("Ask question : "))

query_embeddings = model.embed_query(user_query)

similarity_scores = np.squeeze(cosine_similarity([query_embeddings], doc_embeddings))
print("Similarity scores : ", similarity_scores)
print("Most similar document found: ", available_documents[np.argmax(similarity_scores)])