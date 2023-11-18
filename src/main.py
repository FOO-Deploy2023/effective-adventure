import os
import sys
import discord


class TestClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = TestClient(intents=intents)
    client.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    sys.exit(main())
