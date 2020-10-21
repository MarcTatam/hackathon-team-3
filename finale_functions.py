import json

json_file = open('tasks.json','w')

tasks = {}
id_counter = 0

def add_task(task,description):
    global id_counter
    global json_tasks
    id_counter += 1
    tasks[id_counter] = [task, description]
    print(f'writing {tasks} to file...')
    json_file.write(json.dumps(tasks))

def delete_task(task):
    json_file = open('tasks.json','w')
    for i in range(1,len(tasks)+1):
        if tasks[i][0] == task:
            tasks.pop(i)
    print(f'writing {tasks} to json file...')
    json_file.write(json.dumps(tasks))
        

def read_tasks():
    return tasks

json_file.close()
