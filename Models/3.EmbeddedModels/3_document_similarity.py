from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is a great cricketer and a role model for many.",
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",
    "M.S. Dhoni is known for his calm demeanor and excellent leadership skills.",
    "Rohit Sharma is a talented batsman and has scored multiple double centuries in ODIs.",
    "Anil Kumble is a legendary spinner and former captain of the Indian cricket team."
]
query = "Tell me about MS Dhoni."
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
print("Similarities:", similarities)
index, sorted_indices = sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1]
print(query)
print(documents[index])
print("Similarity Score:", similarities[index])