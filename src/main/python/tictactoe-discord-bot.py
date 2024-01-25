import discord
import os


class TicTacToeBotClient(discord.Client):
    message_count: int = 0

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        self.message_count = self.message_count + 1
        print(f'Message #{self.message_count} from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if message.content.startswith('Hallo'):
            await message.channel.send('Hello ' + message.author.name + '!')


intents = discord.Intents.default()
intents.message_content = True

client = TicTacToeBotClient(intents=intents)
client.run(os.environ['BOT_TOKEN'])
