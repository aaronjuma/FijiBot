import discord
from discord.ext import commands
import random

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
        num = str(random.randrange(5))
        await message.reply(file=discord.File('img/fiji' + num + '.png'))

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Help")
    em.add_field(name = "~danny", value = "Displays image of fiji", inline=False)
    em.add_field(name = "~fiji", value = "Displays a Fiji quote", inline=False)
    await ctx.send(embed = em)

client.run('ODgyNTA3ODE0NTQxNjA2OTIz.YS8Zcw.AHznuk2FfMbSsUEQBJAjk3CbUvI')