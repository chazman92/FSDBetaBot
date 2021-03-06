import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.watching, name="for the .help command"))
    print("I am online")

# Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@client.event
async def on_member_join(member):
    idchannel = member.server.get_channel(785313315340419205) #Gen Discussion Channel
    await client.get_channel(idchannel).send(f"{member.name} has joined")

@client.event
async def on_member_remove(member):
    idchannel = member.server.get_channel(785313315340419205) #Gen Discussion Channel
    await client.get_channel(idchannel).send(f"{member.name} has left")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")
    print('whoami was run')

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)