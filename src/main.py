import os
import sys

import discord
from discord.ext import commands
from discord import app_commands

from question import is_question

from db import insert, search

from index import extract, print_dict
from collections import defaultdict


# Create an instance of the Bot class with '/' as the command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user.name}")
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


@bot.tree.command(name="hello", description="Say hello to the bot!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello world!")

@bot.tree.command(name='questions', description="Find the most common questions in the server and its answers!")
async def embed(ctx):
   
    bot_user = bot.user

    pfp = bot_user.display_avatar

    embed = discord.Embed(title="Most Common Questions", description="This bot will display the most common questions", colour=discord.Colour.blue())
    
    embed.set_thumbnail(url=f"{pfp}")

    embed.add_field(name="Where is phil?", value="Phil is over here!", inline = False)
    embed.add_field(name="Whom is phil?", value="Phil is gdb god!", inline = False)
    embed.add_field(name="What is phil?", value="Also the gdb god", inline = False)

    await ctx.response.send_message(embed=embed)


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
    # table = defaultdict(dict)
    # extract("phil lives in a pineapple", table)
    # extract("phil is SO COOL!", table)
    # extract("phil is actually a pineapple, just like that other phil right there", table)
    # print_dict(table)
    bot.run(get_env("DISCORD_TOKEN"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
