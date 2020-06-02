from discord.ext.commands import Bot
import asyncio
from random import randint


BOT_PREFIX = ("!", "?", "--")
token_file = open("D:\Auri.txt")
TOKEN = token_file.read()
client = Bot(command_prefix=BOT_PREFIX)


def event_messages():
    #   Commands
    async def get_servers():
        await client.wait_until_ready()
        print('List all servers and channels:')
        for server in client.get_all_channels():
            print(server.name)

    #   Discord events
    @client.event
    async def on_message(message):
        my_message = message.content.lower()

        #   We do not want the bot to reply to itself
        if message.author == client.user:
            return

        #   Dice roll command
        if my_message.startswith('/roll'):
            my_message = my_message.replace('/roll ', '')
            my_message = my_message.replace('/roll', '')
            roll = []

            for s in my_message.split('d'):
                if s.isdigit():
                    roll.append(int(s))

            dices = []
            if len(roll) == 2:
                for i in range(0, roll[0]):
                    dices.append(randint(0, roll[1]))
                await message.channel.send(dices)
            else:
                await message.channel.send('Invalid command')

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('----')

    client.loop.create_task(get_servers())
    client.run(TOKEN)


event_messages()


