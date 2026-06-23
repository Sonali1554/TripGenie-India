from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(path="./qdrant_data")

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "best beaches in goa"

query_vector = model.encode(query).tolist()

results = client.query_points(
    collection_name="travel_docs",
    query=query_vector,
    limit=3
).points

print(f"Found {len(results)} results")

for i, result in enumerate(results, start=1):
    print("\n" + "="*80)
    print(f"RESULT {i}")
    print("="*80)
    print(result.payload["text"][:500])

client.close()