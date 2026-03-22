from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=1.8)#, max_completion_tokens=10)

result = chat.invoke("Write a 5 line poem about the beauty of nature.")
print(result.content)