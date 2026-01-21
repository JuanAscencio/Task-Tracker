from core import task

def list_task(args):
    status_Tasks = task.filter_tasks(args.status)
    for task in status_Tasks:
        print(f"Description: {task.description}. Status: {task.status}")

def register(parser):
    parser.add_argument(
        "status", choices=["todo","in-progress","done"],
        type=str, nargs="?", help="Filter tasks by status"
    )

    parser.set_defaults(func=list_task)