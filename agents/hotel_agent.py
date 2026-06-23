def recommend_hotel(destination, budget):

    if budget < 20000:

        return {
            "category": "Budget",
            "recommendation":
                f"Budget hotels in {destination}"
        }

    elif budget < 50000:

        return {
            "category": "Mid Range",
            "recommendation":
                f"3-4 star hotels in {destination}"
        }

    else:

        return {
            "category": "Luxury",
            "recommendation":
                f"5 star luxury resorts in {destination}"
        }