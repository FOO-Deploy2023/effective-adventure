import os
import sys

from client import bot


def get_env(name: str) -> str:
    VALUE: str = os.environ.get(name)

    if VALUE is None:
        raise ValueError(f"Environment variable '{name}' is not set.")

    return VALUE


def main() -> int:
    bot.run(get_env("DISCORD_TOKEN"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
