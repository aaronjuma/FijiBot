import discord
from discord.ext import commands
import random
import pathlib
import os

client = commands.Bot(command_prefix = "~")
client.remove_command('help')

fijiquotes = ["JOHN MERTON FROM OAK LAWN ILLINOIS", "CHISA IS BEST GIRL", "@Raycheck#8150 IS MY DAD", "I SUCK OFF MICHAEL", "You're fat!", "I HAVE AUTISM"]

@client.event
async def on_ready():
    print("Fiji Bot active")

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.content.startswith('~fiji'):
        await message.reply(fijiquotes[random.randrange(len(fijiquotes))], mention_author=True)

    if message.content.startswith('~danny'):
        await message.reply(file=discord.File("img/" + random.choice(os.listdir("img/"))))

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Help")
    em.add_field(name = "~danny", value = "Displays image of fiji", inline=False)
    em.add_field(name = "~fiji", value = "Displays a Fiji quote", inline=False)
    await ctx.send(embed = em)



#DONT FORGET TO REMOVE TOKEN BEFORE PUSHING >:(
client.run('token')