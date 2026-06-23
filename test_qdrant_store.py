from rag.document_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import get_embeddings
from rag.vector_store import create_collection
from rag.vector_store import store_chunks

text = load_pdf("data/goa_travel_guide.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

create_collection()

store_chunks(chunks, embeddings)