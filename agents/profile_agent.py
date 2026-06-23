import ollama
import json
import time


def extract_trip_details(user_query):

    prompt = f"""
Extract travel information from the user query.

Return ONLY valid JSON.

Format:

{{
    "destination":"",
    "days":0,
    "budget":0,
    "travel_type":""
}}

User Query:
{user_query}
"""

    start = time.time()

    response = ollama.generate(
        model="qwen2.5:3b",
        prompt=prompt
    )

    print(
        "Profile Time:",
        round(time.time() - start, 2),
        "sec"
    )

    try:

        result = json.loads(
            response["response"]
        )

        return result

    except:

        return {
            "destination": "",
            "days": 0,
            "budget": 0,
            "travel_type": ""
        }