from pyplanner import pyplanner

with open('cronograma.planner', 'r') as reader:
    project = pyplanner.PyPlanner(reader.read())

    # Print dictionary list of tasks
    for task in project.get_tasks():
        print(task)

    for res in project.get_resources():
        print(res)


