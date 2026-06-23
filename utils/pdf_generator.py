from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_trip_pdf(result):

    pdf_path = "reports/trip_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    profile = result.get("profile", {})

    # Title
    content.append(
        Paragraph(
            "TripGenie India Travel Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Profile
    content.append(
        Paragraph(
            "Travel Profile",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Destination: {profile.get('destination', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Days: {profile.get('days', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Budget: Rs. {profile.get('budget', 0):,}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Travel Type: {profile.get('travel_type', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # Weather
    content.append(
        Paragraph(
            "Weather",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            result.get("weather", "N/A"),
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # Hotel
    hotel = result.get("hotel", {})

    content.append(
        Paragraph(
            "Hotel Recommendation",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Category: {hotel.get('category', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Recommendation: {hotel.get('recommendation', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # Budget
    budget = result.get("budget", {})

    content.append(
        Paragraph(
            "Budget Breakdown",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Hotel: Rs. {budget.get('hotel', 0):,}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Food: Rs. {budget.get('food', 0):,}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Transport: Rs. {budget.get('transport', 0):,}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Activities: Rs. {budget.get('activities', 0):,}",
            styles["Normal"]
        )
    )

    content.append(PageBreak())

    # Itinerary
    content.append(
        Paragraph(
            "Complete Travel Itinerary",
            styles["Heading1"]
        )
    )

    itinerary = result.get(
        "itinerary",
        "No itinerary generated."
    )

    itinerary = (
        itinerary
        .replace("**", "")
        .replace("\n", "<br/>")
    )

    content.append(
        Paragraph(
            itinerary,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_path