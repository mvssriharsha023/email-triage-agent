from graphs.workflow import graph

initial_state = {
    "email": """
    Hi Team,
    The production servers are experiencing high latency and some requests are timing out.
    This issue is impacting our customers and needs urgent attention.
    Please investigate and resolve this as soon as possible.

    Thank you,
    John Doe
    """
}

result = graph.invoke(initial_state)

print("Final State: \n")
print(result)