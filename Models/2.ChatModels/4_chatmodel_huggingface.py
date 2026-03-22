from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)
chat = ChatHuggingFace(llm=llm)
result = chat.invoke("Write a 5 line poem about the beauty of nature.")
print(result.content)
