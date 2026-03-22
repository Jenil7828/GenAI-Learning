from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
os.environ['HF_HOME'] = 'D:/LangChain/GenAI-Learning/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 1.8
    }
)    

chat = ChatHuggingFace(llm=llm)
result = chat.invoke("Write a 5 line poem about the beauty of nature.")
print(result.content)
