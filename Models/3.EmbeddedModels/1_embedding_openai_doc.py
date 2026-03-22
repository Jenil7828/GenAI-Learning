from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)
documents = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
]
result = embeddings.embed_documents(documents)
print(str(result))