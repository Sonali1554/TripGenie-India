import fitz

pdfs = [
    "data/india_tourism.pdf",
    "data/budget_travel.pdf",
    "data/goa_travel_guide.pdf"
]

for pdf_path in pdfs:

    print("\n" + "=" * 80)
    print(pdf_path)
    print("=" * 80)

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc[:3]:
        text += page.get_text()

    print(text[:1500])