import discord
import sys
sys.path.append("H:/Misc")

client = discord.Client()
help = """**.help** - Shows this.
**.invite** - Gives you an easy invite link for the bot."""



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
    msg = message.content

    if msg == ".help":
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)

    if msg == ".invite":
        await client.send_message(message.channel, content = "https://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s got an invite link." % message.author)



with open('H:/Misc/token3.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
