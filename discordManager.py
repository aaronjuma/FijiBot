import discord
import mediaManager as mm
import time
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)
intents.members = True
bot = commands.Bot(command_prefix='~', intents = intents)
admins = [293850557821747201, 387022004710146079, 802783334181634058, 658834349667385360]
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

def isAdmin(ctx):
    user_id = ctx.author.id
    if user_id in admins:
        return True
    else:
        return False
    

async def onMessage(message):
    if message.author == bot.user:
        return

    if message.channel.type != discord.ChannelType.private:
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(username + " " + user_message + " " + channel)

        if message.author.id in mutelist:
            await message.channel.send("MONKEY <@" + str(message.author.id) + "> YOU ARE STILL MUTED!!!!!!", delete_after = 2)
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
    if isAdmin(ctx) == False:
        await ctx.channel.send("YOU DONT HAVE PERMS MONKEY")
        return
    if len(user) < 21:
        await ctx.channel.send("Invalid Input Monkey")
    else:
        print(user)
        guy = int(user[2:-1])
        if guy in mutelist:
            await ctx.channel.send("Monkey is already muted")
        elif ctx.message.guild.get_member(guy) is not None:
            mutelist.append(guy)
            await ctx.channel.send("Monkey <@" + str(guy) + "> is silenced in the name of John Xina")
        else:
            await ctx.channel.send("Monkey does not exist")

@bot.command(name='unmute')
async def unmtue(ctx, user):
    if isAdmin(ctx) == False:
        await ctx.channel.send("YOU DONT HAVE PERMS MONKEY")
        return
    if len(user) < 21:
        await ctx.channel.send("Invalid Input Monkey")
    else:
        guy = int(user[2:-1])
        if guy in mutelist:
            mutelist.remove(guy)
            await ctx.channel.send("Monkey <@" + str(guy) + "> is unsilenced!")
        elif ctx.message.guild.get_member(guy) is None:
            await ctx.channel.send("Monkey does not exist")
        else:
            await ctx.channel.send("Monkey was never muted")


