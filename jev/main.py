"""Minimal entry point for the jev learning environment."""

import os


def main() -> None:
    print(os.environ.get("JEV_GREETING", "Hello from jev!"))


if __name__ == "__main__":
    main()
