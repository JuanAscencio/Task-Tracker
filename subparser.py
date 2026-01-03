# It creates a directory
# With the following command:
# python subparser.py create -d "Directory_name"
import argparse
import os

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

create_parser = subparser.add_parser(
    "create", help="create directory"
)

create_parser.add_argument(
    "-d", nargs=1
)


args = parser.parse_args()

print(args)

if args.d:
    os.mkdir(args.d[0])
    print("Done")