import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if message.content.startswith('Hallo'):
            await message.channel.send('Hello ' + message.author.name + '!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['BOT_TOKEN'])