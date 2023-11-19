import discord

from client import Viper
from db import insert, search

import os
import sys


def get_env(name: str) -> str:
    VALUE: str = os.environ.get(name)

    if VALUE is None:
        raise ValueError(f"Environment variable '{name}' is not set.")

    return VALUE


def main() -> int:
    intents = discord.Intents.default()
    intents.message_content = True
    client = Viper(intents=intents)
    client.run(get_env("DISCORD_TOKEN"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
