example_tasks = {
    "todo": "First example"
}

def add_task(description: str) -> str:
    return f"Added task: {description}."

def tasks(status: str) -> str:
    if status == "todo":
        for todo_task in example_tasks:
            return example_tasks[todo_task]
        
