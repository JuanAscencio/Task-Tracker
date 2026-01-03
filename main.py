import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "square", help="Squares a given number", 
    type=int, default=0, nargs="?"
)

parser.add_argument(
    "-v", "--verbose", 
    help="Verbose description. Use -vv for extra verbose",
    action="count"
)

args: argparse.Namespace = parser.parse_args()
result: int = args.square ** 2

if args.verbose == 1:
    print(f"The result is: {result}")
elif args.verbose == 2:
    print(f"{args.square} ** {args.square} = {result}")
else:
    print(result)