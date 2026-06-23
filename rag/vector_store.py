from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

client = QdrantClient(path="./qdrant_data")

COLLECTION_NAME = "travel_docs"


def create_collection():

    collections = client.get_collections().collections

    existing = [c.name for c in collections]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        print("Collection Created")

    else:
        print("Collection Already Exists")


def store_chunks(chunks, embeddings):

    points = []

    for idx, (chunk, vector) in enumerate(zip(chunks, embeddings)):

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Stored {len(points)} chunks")