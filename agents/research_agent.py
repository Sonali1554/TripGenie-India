def research_destination(destination):

    research_data = {

        "Goa": """
Best Time: November to February

Top Attractions:
Baga Beach, Calangute Beach, Fort Aguada

Popular Foods:
Fish Curry, Prawn Balchao, Bebinca

Adventure Activities:
Water Sports, Parasailing, Scuba Diving

Ideal For:
Families, Couples, Friends

Average Budget:
Rs. 20,000 - Rs. 50,000
""",

        "Kerala": """
Best Time: September to March

Top Attractions:
Munnar, Alleppey, Thekkady

Popular Foods:
Appam, Kerala Sadya, Fish Curry

Adventure Activities:
Houseboat Cruises, Trekking

Ideal For:
Families, Honeymooners

Average Budget:
Rs. 25,000 - Rs. 60,000
""",

        "Jaipur": """
Best Time: October to March

Top Attractions:
Amber Fort, Hawa Mahal, City Palace

Popular Foods:
Dal Baati Churma, Ghewar

Adventure Activities:
Fort Exploration, Local Shopping

Ideal For:
Families, History Lovers

Average Budget:
Rs. 15,000 - Rs. 40,000
""",

        "Kashmir": """
Best Time: March to October

Top Attractions:
Dal Lake, Gulmarg, Pahalgam

Popular Foods:
Rogan Josh, Kahwa

Adventure Activities:
Skiing, Gondola Ride

Ideal For:
Couples, Families

Average Budget:
Rs. 30,000 - Rs. 80,000
""",

        "Manali": """
Best Time: October to June

Top Attractions:
Solang Valley, Rohtang Pass

Popular Foods:
Siddu, Trout Fish

Adventure Activities:
Paragliding, River Rafting

Ideal For:
Adventure Lovers

Average Budget:
Rs. 20,000 - Rs. 50,000
""",

        "Shimla": """
Best Time: March to June

Top Attractions:
Mall Road, Kufri, Jakhoo Temple

Popular Foods:
Madra, Chha Gosht

Adventure Activities:
Horse Riding, Trekking

Ideal For:
Families and Couples

Average Budget:
Rs. 15,000 - Rs. 40,000
"""
    }

    return research_data.get(
        destination,
        f"""
Best Time: October to March

Top Attractions:
Popular attractions in {destination}

Popular Foods:
Local Cuisine

Adventure Activities:
Sightseeing

Ideal For:
Families, Couples, Solo Travelers

Average Budget:
Rs. 20,000 - Rs. 50,000
"""
    )