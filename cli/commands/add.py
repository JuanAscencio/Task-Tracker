'''
Role of add.py

add.py must:
- NOT create ArgumentParser
- NOT call parse_args
- NOT know main.py
- NOT execute domain logic (save tasks)

It must:
* receive the parser from the add command
* define which function is executed
* expose a public command register function
'''
from core import task

def handle(args):
    print(task.add_task(args.description))

# Doesn't validate logic nor interprets semantic
def register(parser):
    parser.add_argument("description")
    parser.set_defaults(func=handle)