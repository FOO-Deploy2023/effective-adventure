import os
import sys

import discord
from discord.ext import commands
from discord import app_commands

from question import is_question

from db import insert, search

from index import build, print_dict
from collections import defaultdict


# Create an instance of the Bot class with '/' as the command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)


@bot.event
async def on_ready():
    print("Logged on as {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message):
        if message.author == bot.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello world!")


def get_env(name: str) -> str:
    VALUE: str = os.environ.get(name)

    if VALUE is None:
        raise ValueError(f"Environment variable '{name}' is not set.")

    return VALUE


def main() -> int:
    #intents = discord.Intents.default()
    #intents.message_content = True
    #client = TestClient(intents=intents)
    #client.run(get_env("DISCORD_TOKEN"))

   # guid_name = client.guild

    # Testing the index
    table = defaultdict(dict)
    table = build("phil lives in a pineapple", table)
    table = build("phil is SO COOL!", table)
    table = build("phil is actually a pineapple, just like that other phil right there", table)
    print_dict(table)
    # bot.run(get_env("DISCORD_TOKEN"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
