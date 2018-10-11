import discord
import sys
sys.path.append("H:/Misc")

client = discord.Client()
help = """**.help** - shows this"""



def msg(msg):
    return msg



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users." % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Toaster 2.0 | .help"))



@client.event
async def on_message(message):
    msg = msg()

    if msg == "-help":
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)



with open('H:/Misc/token3.txt', 'r') as myfile:
    token = myfile.read() #NDk5OTI4OTcxNzExMDg2NjAx.DqDaxg.jvEocVyz37io4QjCtufvxslpQWY
client.run(token)
