import os
import sys
import discord

from question import is_question
from client import Viper

from index import extract, print_dict
from collections import defaultdict
from sortedcontainers import SortedDict


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


    # Testing the index
    # table = defaultdict(SortedDict)
    # extract("why is phil so cool?", table)
    # extract("who lives in a pineapple under the sea?", table)
    # print_dict(table)

    return 0


if __name__ == "__main__":
    sys.exit(main())
