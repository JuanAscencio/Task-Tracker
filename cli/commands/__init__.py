'''
Role of commands/__init__.py
* It knows which commands exist
* It creates the parser for each command
* It delegates its configuration to the corresponding module

Important!
- It does NOT execute commands
- It does NOT parse arguments
- It does NOT print anything

'''
from . import add

def load_commands(subparsers):
    add_parser = subparsers.add_parser("add")
    add.register(add_parser)