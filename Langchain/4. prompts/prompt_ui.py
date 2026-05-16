from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

os.environ["HF_HOME"] = "D:/huggingface_cache"  
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",       # 2.2 GB model will be stored locally
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,         # Increase it for better output
    }
    
)

model = ChatHuggingFace(llm=llm)


st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    # This piece of code is LCEL (langchain expression language) and | is a chain in langchain
    chain = template | model                
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })

    # It has the same meaning as 
    # formatted_prompt = template.invoke({
    #     'paper_input':paper_input,
    #     'style_input':style_input,
    #     'length_input':length_input
    # }
    # )
    # result = model.invoke(formatted_prompt)

    st.write(result.content)