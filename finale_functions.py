import json

json_file = open('tasks.json','w')

tasks = {}
id_counter = 0

def add_task(task,description):
    global id_counter
    global json_tasks
    id_counter += 1
    tasks[id_counter] = [task, description]
    json_file.write(json.dumps(tasks))

def delete_task(task_id):
    json_file = open('tasks.json','w')
    tasks.pop(task_id)
    json_file.write(json.dumps(tasks))


def read_tasks():
    return tasks

json_file.close()
