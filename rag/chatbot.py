from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import ollama


def get_client():
    return QdrantClient(path="./qdrant_data")


embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(query):

    query_vector = embed_model.encode(query).tolist()

    client = get_client()

    results = client.query_points(
        collection_name="india_travel",
        query=query_vector,
        limit=3
    ).points

    client.close()

    context = "\n\n".join(
        [r.payload["text"] for r in results]
    )

    return context


def ask_question(question):

    print("Step 1: Retrieving Context...")

    context = retrieve_context(question)

    print("Step 2: Context Retrieved")
    print(context[:300])

    prompt = f"""
You are a travel assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}
"""

    print("Step 3: Sending to Qwen")

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Step 4: Response Received")

    return response["message"]["content"]