def list_task(args):
    if args.status:
        print(f"Listing all task with status: {args.status}")
    else:
        print("Listing all tasks")

def register(parser):
    parser.add_argument(
        "status", choices=["todo","in-progress","done"],
        type=str, nargs="?", help="Filter tasks by status"
    )

    parser.set_defaults(func=list_task)