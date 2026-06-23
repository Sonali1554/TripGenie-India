import os

from rag.chunker import chunk_text
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Initialize
client = QdrantClient(path="./qdrant_data")

COLLECTION_NAME = "india_travel"

# Create Collection

try:
    client.delete_collection(COLLECTION_NAME)
except:
    pass

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

print("Collection Created")

# Load embedding model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

all_points = []
point_id = 0

DATA_FOLDER = "data"

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".txt"):

        filepath = os.path.join(
            DATA_FOLDER,
            file
        )

        print(f"Processing: {file}")

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        chunks = chunk_text(text)

        embeddings = model.encode(chunks)

        for chunk, vector in zip(
            chunks,
            embeddings
        ):

            all_points.append(

                PointStruct(
                    id=point_id,
                    vector=vector.tolist(),
                    payload={
                        "source": file,
                        "text": chunk
                    }
                )
            )

            point_id += 1

client.upsert(
    collection_name=COLLECTION_NAME,
    points=all_points
)

print(f"Stored {len(all_points)} chunks")