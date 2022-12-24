import discordManager as ds
from discord.ext import commands

client = ds.getClient()

@client.event
async def on_ready():
    ds.onReady()

@client.event
async def on_message(message):
    await ds.onMessage(message)

token = ds.getToken()
client.run(token)