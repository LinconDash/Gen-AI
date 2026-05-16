from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


llm = HuggingFaceEndpoint(
    model="katanemo/Arch-Router-1.5B",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    temperature=0.5,
    max_new_tokens=100
)


model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India ?")
print(result.content)