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
* define which function is executed
* expose a public logging function
'''

# add_task receives a Namespace
# print will go to /core/ later 
def add_task(args):
    print(f"Added task: {args.description}")

# Doesn't validate logic nor interprets semantic
def register(parser):
    parser.add_argument("description")
    parser.set_defaults(func=add_task)