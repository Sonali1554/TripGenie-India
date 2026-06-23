from rag.document_loader import load_pdf
from rag.chunker import chunk_text

text = load_pdf("data/goa_travel_guide.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])