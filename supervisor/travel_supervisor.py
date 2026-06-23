from agents.planner_agent import create_trip_plan
from agents.budget_agent import estimate_budget
from agents.weather_agent import get_weather
from agents.hotel_agent import recommend_hotel
from agents.research_agent import research_destination
from agents.packing_agent import get_packing_list
import time


def generate_complete_trip(
    destination,
    days,
    budget
):

    start = time.time()

    # Research Agent
    research = research_destination(
        destination
    )

    # Planner Agent
    itinerary = create_trip_plan(
        destination,
        days,
        budget
    )

    # Budget Agent
    budget_data = estimate_budget(
        days,
        budget
    )

    # Weather Agent
    weather = get_weather(
        destination
    )

    # Hotel Agent
    hotel = recommend_hotel(
        destination,
        budget
    )

    print(
        "Total Supervisor Time:",
        round(time.time() - start, 2),
        "sec"
    )

    packing_list = get_packing_list(
    destination
)

    return {
    "research": research,
    "itinerary": itinerary,
    "budget": budget_data,
    "weather": weather,
    "hotel": hotel,
    "packing": packing_list
}