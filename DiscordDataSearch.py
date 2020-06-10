import pandas as pd

from discord.ext.commands import Bot

BOT_PREFIX = ("!", "?", "--")
# token_file = open("D:\Auri.txt")
token_file = open("K:\DiscordTest.token")  # Token van Stijn Tas
TOKEN = token_file.read()
client = Bot(command_prefix=BOT_PREFIX)

#   Prepare the data in pandas
df = pd.read_excel("data\\Producenten.xlsx", sheet_name="NED")
df = df.dropna(how='all')


def event_messages():
    #   Discord events
    @client.event
    async def on_message(message):
        my_message = message.content.lower()

        #   We do not want the bot to reply to itself
        if message.author == client.user:
            return

        #   Search product in catalog
        if my_message.startswith('/prod'):
            product = my_message.replace('/prod', '').strip()
            search_df = df[df["Naam producent"].str.contains(product, case=False)]
            search_df = search_df.stack().str.strip().unstack()
            if len(search_df.index) > 10:
                msg = f"--- {len(search_df.index)} Gevonden resultaten, eerste 10 resultaten:\n"
            else:
                msg = f"--- {len(search_df.index)} Gevonden resulaten:\n"
            msg = msg + search_df.head(10).to_string()
            await message.channel.send(msg)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('----')

    client.run(TOKEN)


event_messages()
