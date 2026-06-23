def route_query(query):

    query = query.lower()

    planner = any(
        word in query
        for word in [
            "trip",
            "itinerary",
            "plan",
            "travel"
        ]
    )

    budget = any(
        word in query
        for word in [
            "budget",
            "cost",
            "expense",
            "price",
            "under",
            "within",
            "₹",
            "rs"
        ]
    )

    rag = any(
        word in query
        for word in [
            "beach",
            "hotel",
            "restaurant",
            "attraction",
            "place",
            "goa"
        ]
    )

    return {
        "planner": planner,
        "budget": budget,
        "rag": rag
    }