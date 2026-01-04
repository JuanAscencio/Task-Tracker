import argparse
import commands

def main():
    # Creation of Parser
    parser = argparse.ArgumentParser(prog="task-cli")

    # Creation of the subcommand manager
    subparser = parser.add_subparsers(dest="command")
    subparser.required = True

    # Request /commands/ to register commands
    commands.load_commands(subparser)

    # Parse arguments
    args: argparse.Namespace = parser.parse_args()

    # Dispatch
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()