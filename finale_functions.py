tasks = {}
id_counter = 0

def add_task(task,description):
    global id_counter
    id_counter += 1
    tasks[id_counter] = [task, description]

def delete_task(task):
    for i in range(1,len(tasks)+1):
        if tasks[i][0] == task:
            tasks.pop(i)

def read_tasks():
    return tasks
