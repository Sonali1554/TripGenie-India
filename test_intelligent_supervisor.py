from supervisor.intelligent_supervisor import run_tripgenie

query = """
Plan a 6 day family trip to Kashmir
under 60000 rupees
"""

result = run_tripgenie(query)

print(result)