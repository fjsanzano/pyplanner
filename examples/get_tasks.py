import pyplanner

with open('cronograma.planner', 'r') as reader:
    p = pyplanner.PyPlanner(reader.read())
    i=1
    for d in p.get_tasks():
        print(str(i)+str(d['name'])+' > - <'+str(d['parent_id'])+'> - <'+str(d['resource_id']))
        i+=1

    # for r in p.get_resources():
    #     print(r)

    # print(p.get_task_resource('4'))
