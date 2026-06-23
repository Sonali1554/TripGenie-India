def get_travel_tips(destination):

    tips = {

        "Goa": [
            "Visit beaches early morning.",
            "Try local seafood.",
            "Avoid peak traffic hours."
        ],

        "Jaipur": [
            "Visit Amber Fort early.",
            "Carry water during summers.",
            "Explore local markets."
        ],

        "Kashmir": [
            "Carry warm clothes.",
            "Book gondola rides early.",
            "Keep identity proof handy."
        ]
    }

    return tips.get(
        destination,
        ["Enjoy your trip!"]
    )