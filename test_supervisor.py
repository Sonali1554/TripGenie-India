from supervisor.supervisor_agent import run_supervisor

query = "Plan a Goa trip under 25000 and suggest beaches"

result = run_supervisor(query)

print(result)