from supervisor.travel_supervisor import (
    generate_complete_trip
)

result = generate_complete_trip(
    destination="Kerala",
    days=5,
    budget=40000
)

print(result)