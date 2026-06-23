from agents.profile_agent import (
    extract_trip_details
)

query = """
Plan a 5 day honeymoon trip to Kerala
under 50000 rupees
"""

result = extract_trip_details(query)

print(result)