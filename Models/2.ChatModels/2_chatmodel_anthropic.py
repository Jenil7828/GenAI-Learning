from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

chat = ChatAnthropic(model='claude-sonnet-4-6', temperature=1.8)
result = chat.invoke("Write a 5 line poem about the beauty of nature.")
print(result.content)
