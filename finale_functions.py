import json

tasks = {}
id_counter = 0

def add_task(task,description):
    global id_counter
    global json_tasks
    id_counter += 1
    tasks[id_counter] = [task, description]
    json_tasks = json.dumps(tasks)

def delete_task(task):
    global json_tasks
    for i in range(1,len(tasks)+1):
        if tasks[i][0] == task:
            tasks.pop(i)
    json_tasks = json.dumps(tasks)

def read_tasks():
    return tasks

add_task('hello','goodbye')
print(json_tasks)
