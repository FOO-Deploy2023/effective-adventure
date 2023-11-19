import os
import sys
import discord

from question import is_question

from index import extract, print_dict
from collections import defaultdict


class TestClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


def get_env(name: str) -> str:
    VALUE: str = os.environ.get(name)

    if VALUE is None:
        raise ValueError(f"Environment variable '{name}' is not set.")

    return VALUE


def main() -> int:
    intents = discord.Intents.default()
    intents.message_content = True
    client = TestClient(intents=intents)
    client.run(get_env("DISCORD_TOKEN"))

    guid_name = client.guild

    # Testing the index
    # table = defaultdict(dict)
    # extract("phil lives in a pineapple", table)
    # extract("phil is SO COOL!", table)
    # extract("phil is actually a pineapple, just like that other phil right there", table)
    # print_dict(table)

    return 0


if __name__ == "__main__":
    sys.exit(main())
