from utils.pdf_generator import generate_trip_pdf

generate_trip_pdf(
    destination="Goa",
    days=4,
    budget=25000,
    itinerary="""
Day 1: Baga Beach
Day 2: Fort Aguada
Day 3: Water Sports
Day 4: Shopping
""",
    budget_data={
        "hotel":10000,
        "food":5000,
        "transport":6250,
        "activities":3750
    }
)

print("PDF Generated")