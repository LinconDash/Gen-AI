from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os

os.environ["HF_HOME"] = "D:/huggingface_cache"  
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",       # 2.2 GB model will be stored locally
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
    }
    
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India ?")
print("Answer :", result.content)