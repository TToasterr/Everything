import discord
import sys
from random import randint as ri
from random import choice as ch
from discord.utils import get
import subprocess
sys.path.append("H:/Misc")
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 3.0 (Python)/commands")

client = discord.Client()
prefix = "t."



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Toaster 3.0 | t.help"))



@client.event
async def on_server_join(server):
    print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message):
    if message.channel.is_private and not (message.author.bot):
        await client.send_message(message.channel, content = "This bot doesnt work with DMs (sorry!). Invite me to a server and use me there!\nhttps://discordapp.com/oauth2/authorize?client_id=507155028948287490&scope=bot")
        print("%s tried to DM the bot.\n" % message.author)
        return()

    if message.author.bot:
        return()

    msg = message.content
    with open("cmdlist.txt", "r") as cmdlist:
        commands = cmdlist.read().split("\n")
        del commands[-1]



    if not msg.startswith(prefix):
        return()

    if msg == (prefix + "help"):
        await client.send_message(message.channel, content = ("Commands: \n\n" + "\n".join(commands)))
        print("%s got help. \n" % message.author)
        return()

    for command in commands:
        if msg[:(len(command) + len(prefix))] == (prefix + command):
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 3.0 (Python)/commands/%s.txt" % command), "r") as cmdfile:
                comd = cmdfile.read()

            invitelink = await client.create_invite(destination = message.channel, xkcd = True, max_uses = 100)
            me = await client.get_user_info("184474965859368960")

            exec(comd, globals())
            cmd(message, msg, invitelink, me)
            if doMsgOut:
                for i in range(msgAmm):
                    await client.send_message(channel[i], content = msgOut[i])
            print(consoleOut + "\n")






#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token4.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
