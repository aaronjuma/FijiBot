import discord
import mediaManager as mm
import time
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)
intents.members = True
bot = commands.Bot(command_prefix='~', intents = intents)
mutelist = []

def getClient():
    return bot

def getToken():
    f = open('token.txt', 'r')
    token = f.readline()
    f.close()
    return token

def onReady():
    mm.setup()
    print("FIJIBOT ACTIVE")

async def onMessage(message):
    if message.author == bot.user:
        return

    if message.channel.type != discord.ChannelType.private:
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(username + " " + user_message + " " + channel)

        if message.author.id in mutelist:
            await message.author.send("MONKEY <@" + str(message.author.id) + "> YOU ARE STILL MUTED!!!!!!")
            await message.delete()

        await bot.process_commands(message)


@bot.command(name='test')
async def test(ctx):
    print("abcde")
    await ctx.send("PEEPEEPOOPOOO")


@bot.command(name='fiji')
async def fiji(ctx):
    await ctx.reply(mm.getQuote())


@bot.command(name='danny')
async def danny(ctx):
    await ctx.reply(file=discord.File(mm.getImage()))


@bot.command(name='mute')
async def mute(ctx, user):
    if len(user) < 21:
        await ctx.reply("Invalid Input Monkey")
    else:
        guy = int(user[2:-1])
        if ctx.message.guild.get_member(guy) is not None:
            mutelist.append(guy)
            await ctx.channel.send("Monkey <@" + str(ctx.author.id) + "> is silenced in the name of John Xina")
        else:
            await ctx.channel.send("Monkey does not exist")

@bot.command(name='unmute')
async def unmtue(ctx, user):
    if len(user) < 21:
        await ctx.reply("Invalid Input Monkey")
    else:
        guy = int(user[2:-1])
        if ctx.message.guild.get_member(guy) is not None:
            mutelist.remove(guy)
            await ctx.channel.send("Monkey <@" + str(ctx.author.id) + "> is unsilenced!")
        else:
            await ctx.channel.send("Monkey was not muted or did not exist")


