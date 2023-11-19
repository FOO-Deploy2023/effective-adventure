import discord

import question

class Viper(discord.Client):
    asked = {}
    
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        # if message.content == "ping":
        # msg = message.content
        match message.content:
            case "ping":
                await message.channel.send("pong")
            case _:
                pass

        
        if question.is_question(message.content):
            asker = message.author.id

            # get keywords
            kw = "nothing"

            # db lookup
            answer = "answer"
            try:
                await message.reply(answer)
            finally:
                return

            # if not in db:
            who_asked[kw] = message.id
            self.asked[message.id] = kw

            return          


        try:
            message.reference
        except NameError:
            print("not a reply")
        else:
            if message.reference.message_id in self.asked:
                #store into db as an answer
                print("store into db")
                self.asked.pop(message.reference.message_id)
            
