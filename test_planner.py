from agents.planner_agent import create_trip_plan

plan = create_trip_plan(
    destination="Goa",
    days=4,
    budget=25000
)

print(plan)