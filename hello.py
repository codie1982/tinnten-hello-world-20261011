"""A small greeting module and command line program."""
import sys


def greet(name="World"):
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet(sys.argv[1] if len(sys.argv) > 1 else "World"))
