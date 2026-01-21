class Task:
    _next_id = 1

    def __init__(self, description, status  ="todo"):
        self.description = description
        self.status = status
        self.id = Task._next_id
        Task._next_id += 1

list_of_tasks = []

def add_task(task_description):
    new_task = Task(description=task_description)
    list_of_tasks.append(new_task)
    return new_task


def filter_tasks(status):
    status_Tasks = []
    for task in list_of_tasks:
        if status == None:
            status_Tasks.append(task)
            continue

        if status == task.status:
            status_Tasks.append(task)
    return status_Tasks
        
