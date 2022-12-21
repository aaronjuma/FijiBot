import discord
import time
import mediaManager as mm
from discord.ext import commands

client = discord.Client()

def onReady():
    mm.setup()
    print("FIJIBOT ACTIVE")

async def onMessage(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    if user_message[1:] == 'fiji':
        await message.reply(mm.getQuote())

    if user_message[1:] == 'danny':
        await message.reply(file=discord.File(mm.getImage()))

    if username == 'uenoo#4717':
        time.sleep(1)
        await message.delete()

    # #Section for commands
    # if user_message[0] == '~':
    #     await cm.command(message)

def getClient():
    return client