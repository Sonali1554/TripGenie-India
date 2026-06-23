from rag.document_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import get_embeddings

text = load_pdf("data/goa_travel_guide.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

print("Chunks:", len(chunks))
print("Embedding Dimension:", len(embeddings[0]))