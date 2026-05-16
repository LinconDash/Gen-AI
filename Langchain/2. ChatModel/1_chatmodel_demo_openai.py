from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temp : randomness, max_completion_tokens: limit the output length to reduce cost
model = ChatOpenAI(model="gpt-4", temperature=0, max_completion_tokens=1000)        
    
result = model.invoke(input="What is the capital of India ?")

print(result.content)