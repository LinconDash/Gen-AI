from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)    # model name and output vector dimension 

result = model.embed_query("Delhi is the capital of India")

print(result)  # It is a vector