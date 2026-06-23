from agents.profile_agent import extract_trip_details
from supervisor.travel_supervisor import generate_complete_trip

import time


def run_tripgenie(user_query):

    start = time.time()

    profile = extract_trip_details(user_query)

    print(
        "Profile Agent:",
        round(time.time() - start, 2),
        "sec"
    )

    destination = profile["destination"]
    days = profile["days"]
    budget = profile["budget"]

    start = time.time()

    result = generate_complete_trip(
        destination=destination,
        days=days,
        budget=budget
    )

    print(
        "Trip Planning:",
        round(time.time() - start, 2),
        "sec"
    )

    result["profile"] = profile

    return result