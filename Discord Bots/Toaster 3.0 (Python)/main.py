import discord
import sys
from random import randint as ri
from random import choice as ch
from discord.utils import get
sys.path.append("H:/Misc")

client = discord.Client()



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Toaster 2.0 | .help"))



@client.event
async def on_server_join(server):
    print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message):
    global content

    if message.channel.is_private and not (message.author.bot):
        await client.send_message(message.channel, content = "This bot doesnt work with DMs (sorry!). Invite me to a server and use me there!\nhttps://discordapp.com/oauth2/authorize?client_id=507155028948287490&scope=bot")
        print("%s tried to DM the bot.\n" % message.author)
        return()

    if message.author.bot:
        return()

    activeServers = client.servers
    msg = message.content



    #Help command
    if msg == ".help 1" or msg == ".help":
        embed=discord.Embed(title="Commands anyone can do.", description="", color=0x00ff00)
        embed.set_author(name="General Commands")
        embed.set_footer(text="uwu")

        await client.send_message(message.channel, content = help1)
        print("%s asked for help.\n" % message.author)



    #Invite command (gives invite link)
    if msg == ".invite":
        await client.send_message(message.channel, content = "https://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s got an invite link.\n" % message.author)



    #testing changeable commands
    if msg in {"tcc","test changeable command"}:
        with open("test.txt", "r") as testfile:
            code = testfile.read()
        exec(code)






#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token4.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
