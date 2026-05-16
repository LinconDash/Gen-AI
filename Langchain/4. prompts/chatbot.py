from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os
from langchain_core.prompts import PromptTemplate, load_prompt

os.environ["HF_HOME"] = "D:/huggingface_cache"  
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",       # 2.2 GB model will be stored locally
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 1000,         # Increase it for better output
    }
    
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI : ", result.content)