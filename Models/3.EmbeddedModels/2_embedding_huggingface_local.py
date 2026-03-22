from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome."
]
result = embeddings.embed_documents(documents)
print(str(result))