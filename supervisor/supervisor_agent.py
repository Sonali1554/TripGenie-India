from supervisor.router import route_query

from agents.planner_agent import create_trip_plan
from agents.budget_agent import estimate_budget
from rag.chatbot import ask_question


def run_supervisor(query):

    routes = route_query(query)

    result = {}

    if routes["planner"]:

        result["trip_plan"] = create_trip_plan(
            "Goa",
            4,
            25000
        )

    if routes["budget"]:

        result["budget"] = estimate_budget(
            4,
            25000
        )

    if routes["rag"]:

        result["travel_info"] = ask_question(query)

    return result