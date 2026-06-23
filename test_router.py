from supervisor.router import route_query

query = "Plan a 4 day Goa trip under 25000 and suggest beaches"

result = route_query(query)

print(result)