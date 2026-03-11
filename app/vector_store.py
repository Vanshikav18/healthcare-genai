import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.get_or_create_collection("medical_data")

documents = [

"Diabetes is a chronic condition that causes high blood sugar levels.",

"Hypertension means high blood pressure and may increase heart disease risk.",

"Fever is commonly caused by infection in the body.",

"Asthma affects breathing due to airway inflammation.",

"Headache may occur due to stress, dehydration or lack of sleep.",

"Common cold symptoms include sneezing, cough and mild fever.",

"Stomach pain can occur due to indigestion or infection."

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
        n_results=2
    )

    return results["documents"][0]