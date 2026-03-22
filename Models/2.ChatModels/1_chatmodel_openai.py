from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(model='gpt-5.4', temperature=1.8, max_completion_tokens=10)

result = chat.invoke("Write a 5 line poem about the beauty of nature.")
print(result.content)
