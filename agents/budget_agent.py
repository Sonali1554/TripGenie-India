def estimate_budget(days, budget):

    hotel = budget * 0.4
    food = budget * 0.2
    transport = budget * 0.25
    activities = budget * 0.15

    return {
        "hotel": round(hotel),
        "food": round(food),
        "transport": round(transport),
        "activities": round(activities)
    }