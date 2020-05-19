from discord.ext.commands import Bot
import asyncio


BOT_PREFIX = ("!", "?", "--")
TOKEN = 'TOKEN'
client = Bot(command_prefix=BOT_PREFIX)


def event_messages():
    # Trader
    async def DO_SOMETHING():
        await client.wait_until_ready()
        while not client.is_closed:
            if not client.wait_until_ready():
                print('Client not ready yet')
                await asyncio.sleep(5)
            await client.wait_until_ready()


    # Commands
    async def get_servers():
        await client.wait_until_ready()
        print('List all servers and channels:')
        for server in client.get_all_channels():
            print(server.name)

    #   Discord events
    @client.event
    async def on_message(message):
        my_message = message.content.lower()

        #   we do not want the bot to reply to itself
        if message.author == client.user:
            return

        # Auri only reacts in the auri channel
        if message.channel.name != 'auri':
            print('Auri only responds to the Auri channel!')
            return
        msg = []
        #   React




    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('----')

    client.loop.create_task(get_servers())
    client.loop.create_task(DO_SOMETHING())
    client.run(TOKEN)


event_messages()


