from graphs.workflow import graph

initial_state = {
    "email": "You won a free lottery!"
}

result = graph.invoke(initial_state)

print(result)