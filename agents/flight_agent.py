def recommend_flight(destination, budget):

    if budget < 20000:
        return "Economy Flights Recommended"

    elif budget < 50000:
        return "Premium Economy Flights Recommended"

    else:
        return "Business Class Flights Recommended"