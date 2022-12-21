import discordManager as ds
from discord.ext import commands

client = ds.getClient()

@client.event
async def on_ready():
    ds.onReady()

@client.event
async def on_message(message):
    await ds.onMessage(message)

client.run('ODgyNTA3ODE0NTQxNjA2OTIz.GWasbg.MSEBd7Siin92icqCcD4ZnjjIS4aG2hbjpZuSC0')