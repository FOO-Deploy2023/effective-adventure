import discord

# import db
from index import extract
import question

class Viper(discord.Client):
    asked = []
    db = {}
    
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        match message.content:
            case "ping":
                await message.channel.send("pong")
            case _:
                pass

        
        if question.is_question(message.content):
            asker = message.author.id

            # get keywords
            kw = extract(message.content)
            print("keywords: ", kw)

            answers = []
            for k, _ in kw:
                a = self.db.get(k)
                if a:
                    answers.append(a)

            if not answers:
                self.asked.append(message.id)
                print("could not find answer, waiting for reply...", message.id)
            else:
                try:
                    for a in answers:
                        reply = await message.channel.fetch_message(a)
                        await message.reply(reply.content)
                except:
                    pass
        else:
            try:
                message.reference.message_id
            except:
                print("not a reply")
            else:
                if message.reference.message_id in self.asked:
                    print("got a reply", message.reference.message_id)
                    q = await message.channel.fetch_messasge(message.reference.message_id)
                    kw = extract(q.content)
                    print("keywords: ", kw)
                    for k, _ in kw:
                        self.db[k] = message.id

                    self.asked.remove(message.reference.message_id)

        print("DB: ", self.db)
            
        return
