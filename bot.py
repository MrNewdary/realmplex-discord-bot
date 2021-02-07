import discord
from discord.ext import commands
from mcstatus import MinecraftServer

token = ''
client = commands.Bot(command_prefix='?', case_insensitive=True)

@client.command()
async def status(ctx):
    server = MinecraftServer.lookup("realmplex.mc.gg")
    status = server.status()
    usersConnected = sorted([status.players.sample[i].name for i in range(status.players.online)])
    if len(usersConnected) > 0:
        usersConnected = ', '.join(usersConnected[i] for i in range(len(usersConnected)))
    else:
        usersConnected = 'No one online'
    online = status.players.online
    maximum = status.players.max
    version = status.version.name
    embedVar = discord.Embed(title=f'Realmplex Status',color=15105570)
    embedVar.add_field(name="Player Count", value=f"{online}/{maximum}", inline=True)
    embedVar.add_field(name="Version", value=f"{version}", inline=True)
    embedVar.add_field(name="Players", value=f"{usersConnected}", inline=False)
    await ctx.channel.send(embed=embedVar)

@client.command()
async def ip(ctx):
    embedVar = discord.Embed(title=f'realmplex.mc.gg', color=15105570)
    await ctx.channel.send(embed=embedVar)

client.run(token)
