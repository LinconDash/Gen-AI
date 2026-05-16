from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)    # model name and output vector dimension 

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "I am a good boy"
]


result = model.embed_documents(documents)

print(result)  # It is a 2-D vector with dimension (3, 32)