# It creates or deletes a directory
# With the following commands:
# python subparser.py create -d "Directory_name"
# python subparser.py delete -d "Directory_name"
import argparse
import os

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")

create_parser = subparser.add_parser(
    "create", help="create directory"
)

create_parser.add_argument(
    "-d", nargs=1
)

delete_parser = subparser.add_parser(
    "delete", help="create directory"
)

delete_parser.add_argument(
    "-d", nargs=1
)


args: argparse.Namespace = parser.parse_args()

print(args)

if args.command == "create":
    if args.d:
        os.mkdir(args.d[0])
        print("The directory has been created")

if args.command == "delete":
    os.rmdir(args.d[0])
    print("The directory has been removed succesfully!")

