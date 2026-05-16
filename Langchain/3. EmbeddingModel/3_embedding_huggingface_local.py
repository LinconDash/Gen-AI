from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_HOME"] = "D:/huggingface_cache"  
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

result = model.embed_query(text)  # can also be done for docs

print(str(result))
print(len(result))