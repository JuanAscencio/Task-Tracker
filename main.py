# You run it like this: python main.py 2 5 -vvv
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument(
    "a", type=int, help="The base value"
)

parser.add_argument(
    "b", type=int, help="The exponent"
)

group.add_argument(
    "-v", "--verbose", action="count",
    help="Provides a verbose description. Use -vv for extra verbose."
)

group.add_argument(
    "-s", "--silence", action="store_true",
    help="Generate a silent version of the output"
)

args: argparse.Namespace = parser.parse_args()
result: int = args.a ** args.b

if args.silence:
    print("Silenced!")
else:
    match args.verbose:
        case 1:
            print(f"The result is {result}")
        case 2:
            print(f"{args.a} ** {args.b} = {result}")
        case _:
            print(result)