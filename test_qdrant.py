from qdrant_client import QdrantClient

client = QdrantClient(path="./qdrant_data")

print("Qdrant Local Started Successfully")

client.close()