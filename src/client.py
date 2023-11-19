import discord

class Viper(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        # if message.content == "ping":
        cont = message.content
        match cont:
            case "ping":
                await message.channel.send("pong")
            case _:
