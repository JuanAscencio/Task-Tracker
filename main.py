# You run it like this: python main.py 
# depending on the commands you write is the output you get XD
import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument(
    "filename", help="A name of a file to process",
    nargs="?", default="default_file.txt"
)

parser.add_argument(
    "-c", "--copy", type=int,
    metavar="N", help="Make N number of copies",
    nargs="?", const=2
)

parser.add_argument(
    "-s","--something",
    action="store_true" 
)

parser.add_argument(
    "-d", "--date", 
    type=datetime.date.fromisoformat, help="datetime"
)

parser.add_argument(
    "-v","--version",
    action="version", version="main.py v1.0"
)

parser.add_argument(
    "-n", "--name", default="file_copy",
    choices=["name1","name2","name3"]
)

parser.add_argument(
    "-a","--append", action="append"
)

parser.add_argument(
    "-o","--other",
    const=1,
    action="append_const", dest="some_list"
)

parser.add_argument(
    "-e","--etcethera", 
    const=2,
    action="append_const", dest="some_list"
)

parser.add_argument(
    "-q", "--quantity",
    help="Counts the times you input the command",
    action="count"
)

args: argparse.Namespace = parser.parse_args()
print(args)

if args.something and args.copy:
    print("You use -s and -c command") 
elif args.something:
    print("You used -s command")
elif args.copy:
    print("You used -c command")
else:
    print("You didn\'t used any command")
