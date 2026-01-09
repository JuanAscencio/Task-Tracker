from core import task

def list_task(args):
    print(task.tasks(args.status))

def register(parser):
    parser.add_argument(
        "status", choices=["todo","in-progress","done"],
        type=str, nargs="?", help="Filter tasks by status"
    )

    parser.set_defaults(func=list_task)