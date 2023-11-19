from discord import app_commands
from discord.ext import commands
import discord.ui as ui
import discord

import db
from index import extract
import question

# Create an instance of the Bot class with '/' as the command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# module globals
unanswered = []
try:
    db_cache = db.restore()
except:
    db_cache = {}


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello world!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    match message.content:
        case "ping":
            await message.channel.send("pong")
        case _:
            pass

    if question.is_question(message.content):
        await on_question(message)
    elif message.reference.message_id is not None:
        await on_answer(message)

    return


async def on_question(message):
    asker = message.author.id
    kw = extract(message.content)

    answers = []
    for k, _ in kw:
        a = db_cache.get(k)
        if a:
            answers.append(a)

    if not answers:
        unanswered.append(message.id)
    else:
        try:
            replies = []
            for a in answers:
                for id in a:
                    reply = await message.channel.fetch_message(id)
                    replies.append(reply.content)

            # await message.reply(full)
            embed = discord.Embed(title="FAQ detected!")
            embed.set_thumbnail(url=bot.user.display_avatar)

            embed.add_field(
                name="Detected topics",
                value=", ".join([k for k, _ in kw]),
                inline=False,
            )

            full = ""
            for i in range(len(replies)):
                full += f"{i+1}: {replies[i]}\n"
            embed.add_field(name="Common answers", value=full, inline=False)
            await message.reply(embed=embed)

        except:
            pass


async def on_answer(message):
    q = await message.channel.fetch_message(message.reference.message_id)
    kw = extract(q.content)
    for k, _ in kw:
        if k in db_cache.keys():
            db_cache[k].append(message.id)
        elif message.reference.message_id in unanswered:
            db_cache[k] = [message.id]
            unanswered.remove(message.reference.message_id)

    db.store(db_cache)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)
