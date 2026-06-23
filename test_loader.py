from rag.document_loader import load_pdf

text = load_pdf("data/goa_travel_guide.pdf")

print(text[:3000])