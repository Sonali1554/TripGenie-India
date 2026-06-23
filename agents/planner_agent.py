import ollama
import time


def create_trip_plan(
    destination,
    days,
    budget,
    research=""
):

    prompt = f"""
Destination: {destination}

Create a simple {days}-day itinerary.

Budget: Rs. {budget}

Keep response under 120 words.

Only include:

Day 1
Day 2
Day 3

Top Attractions

Food Recommendations
"""

    start = time.time()

    response = ollama.generate(
        model="qwen2.5:3b",
        prompt=prompt,
        options={
            "num_predict": 150
        }
    )

    print(
        "Planner Time:",
        round(time.time() - start, 2),
        "sec"
    )

    return response["response"]