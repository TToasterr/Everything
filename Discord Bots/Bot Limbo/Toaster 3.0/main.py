import discord
import sys
from random import randint as ri
from random import choice as ch
from discord.utils import get
import pygsheets
import pandas as pd
sys.path.append("H:/Misc")
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 3.0 (Python)/server message storage")

client = discord.Client()
prefix = "t."

gc = pygsheets.authorize(service_file='H:/Misc/creds.json')
df = pd.DataFrame()
thing = ""



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
    global thing

    if message.channel.is_private and not (message.author.bot):
        await client.send_message(message.channel, content = "This bot doesnt work with DMs (sorry!). Invite me to a server and use me there!\nhttps://discordapp.com/oauth2/authorize?client_id=507155028948287490&scope=bot")
        print("%s tried to DM the bot.\n" % message.author)
        return()



    if message.author.bot:
        return()



    msg = message.content



    # try:
    sh = gc.open('Testing')
    sheett = False
    sss = 0
    for sheet in sh.worksheets():
        if sheett == False:
            sss += 1
        if sheet.title == message.server.name:
            sheett = True
    if sheett == False:
        sh.add_worksheet(message.server.name, rows=1000, cols=26, src_tuple=None, src_worksheet=None, index=None)
        owo = 0
        for sheet in sh.worksheets():
            owo += 1
        wks = sh[owo-1]
        wks.cell('A1').value = 0
    else:
        wks = sh[sss-1]
    thing = "unbrok"
    # except:
    #     if thing == "unbrok":
    #         thing = "brok"
    #         await client.send_message(message.channel, content = "The sheets API couldn't connect to google (I blame google).\nThis usually fixes itself in about a minute, just w a i t\nThis just means that message storage and stalking wont work.")
    #         print("The API couldn't connect to google. \n")
    #     else:
    #         print("what")
    #     return()



    try:
        if int(wks.cell('A1').value) == 1:
            print("%s | %s | %s: %s\n" % (message.server.name, message.channel, message.author, message.content))
        thing = "unbrok"
    except:
        if thing == "unbrok":
            await client.send_message(message.channel, content = "You used this command too many times in a short period of time (I blame google).\nThis usually fixes itself after about a minute.\nThis just means that message storage and stalking wont work.")
            print("The API reached quota or something. \n")
        else:
            print("what 2")
        return()



    autoresponses = wks.range("B1:B20")
    for x in autoresponses:
        x = str(x[0])
        x = x[6:]
        x = x[:-1]
        x = x.split(" ")

        if x[1] != "''":
            if x[1][1:] in msg:
                await client.send_message(message.channel, content = x[3][:-1])



    try:
        if int(wks.cell("A2").value) == 1 and msg[:2] != "t." and msg[0] not in {".", "!", "?"}:
            with open("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 3.0 (Python)/server message storage/%s.txt" % message.server.name, "a+") as serverFile:
                serverFile.write("**%s**: %s\n" % (message.author, msg))
    except:
        do = "nothing"



    gcmds = []
    mcmds = []
    autorescmds = []
    strgcmds = []
    fcmds = []
    with open("cmdlist.py", "r") as cmdlist:
        temp = cmdlist.read()
        exec(temp, globals())
        for command in cmdArr:
            if command.type == "general":
                gcmds.append(command)
            elif command.type == "mod":
                mcmds.append(command)
            elif command.type == "autores":
                autorescmds.append(command)
            elif command.type == "strg":
                strgcmds.append(command)
            elif command.type == "fun":
                fcmds.append(command)



    if not msg.startswith(prefix):
        return()



    if msg == (prefix + "help") or msg == (prefix + "?"):
        embed=discord.Embed(title="t.help [command] for more info", description="-------------------------", color=0x00ff00)
        embed.set_author(name="All Commands")
        embed.add_field(name="General Commands", value=("\n".join([(command.name) for command in gcmds])), inline=False)
        embed.add_field(name="Fun Commands", value=("\n".join([(command.name) for command in fcmds])), inline=False)
        embed.add_field(name="Autoresponder Commands", value=("\n".join([(command.name) for command in autorescmds])), inline=False)
        embed.add_field(name="Message Storage Commands", value=("\n".join([(command.name) for command in strgcmds])), inline=False)
        await client.send_message(message.channel, embed = embed)
        print("%s got help. \n" % message.author)
        return()



    if msg[:6] == "t.help" or msg[:3] == "t.?":
        cmdname = msg[7:] if msg[:3] != "t.?" else msg[4:]
        for command in cmdArr:
            if cmdname in {command.name, command.alias}:
                embed = discord.Embed(title=(command.name), description=(command.rname), color=0x00ff00)
                embed.add_field(name="-", value="%s\n\nAlias: %s\nWho can use it: %s" % (command.desc, command.alias, command.who))
                embed.set_footer(text=command.type)

        await client.send_message(message.channel, embed = embed)
        print("%s got help for the %s command. \n" % (message.author, cmdname))
        return()



    for command in cmdArr:
        if msg[:(len(command.name) + len(prefix))] == (prefix + command.name) or msg[:(len(command.alias) + len(prefix))] == (prefix + command.alias):

            me = await client.get_user_info("184474965859368960")

            exec(command.code, globals())
            cmd(msg, message, me, wks)
            await client.send_message(message.channel, content = cmdOut)
            if command.name == "suggest":
                await client.send_message(me, content = "**%s** suggests: \n%s\n\n%s" % (message.author, suggestion, invitelink))
            print("")



#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token4.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
