import argparse
import sys

def run(args):
    return f"Hello {args.name}!\n"

def main():
    parser = argparse.ArgumentParser(description="Jo CLI greeting tool")
    # Removed required=True so default="User007" actually works
    parser.add_argument(
        "--name", 
        type=str, 
        default="User007", 
        help="This is the name of the user"
    )

    args = parser.parse_args()
    sys.stdout.write(str(run(args)))

if __name__ == "__main__":
    main()