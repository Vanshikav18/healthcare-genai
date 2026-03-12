import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.get_or_create_collection("medical_data")

documents = [

"Fever is commonly caused by infection in the body.",
"Headache can occur due to stress or dehydration.",
"Cough may occur due to cold or throat infection.",
"Diabetes is a condition that causes high blood sugar.",
"Asthma affects breathing and airways.",
"Cold symptoms include sneezing and mild fever."

]

embeddings = model.encode(documents).tolist()

for i, doc in enumerate(documents):

    collection.add(
        documents=[doc],
        embeddings=[embeddings[i]],
        ids=[str(i)]
    )


def search_context(query):

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    return results["documents"][0][0]