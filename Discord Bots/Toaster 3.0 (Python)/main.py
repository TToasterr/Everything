import discord
import sys
from random import randint as ri
from random import choice as ch
sys.path.append("H:/Misc")



client = discord.Client()



help = """
,help - this
,suggest [suggestion] - submits your suggestions to the REAL Toaster.
"""



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Toaster 3.0 | ,help"))



@client.event
async def on_message(message):

    if message.channel.is_private and not (message.author.bot):
        await client.send_message(message.channel, content = "This bot doesnt work with DMs (sorry!). Invite me to a server and use me there!\nhttps://discordapp.com/oauth2/authorize?client_id=507155028948287490&scope=bot")
        print("%s tried to DM the bot. \n" % message.author)
        return()



    if message.author.bot:
        return()



    msg = message.content



    if msg == ",help":
        embed = discord.Embed(title="Toaster 3.0 Commands", description="", color=0x3aff3a)
        embed.add_field(name="General Commands", value=help, inline=False)
        await client.send_message(message.channel, embed=embed)
        print("%s got help.\n" % message.author)



    if msg[:8] == ",suggest":
        suggestion = msg[9:]

        if suggestion == "":
            await client.send_message(message.channel, content = "You didnt supply a suggestion!")
            return()

        me = await client.get_user_info("184474965859368960")
        await client.send_message(me, content = "**%s** suggests: \n%s" % (message.author, suggestion))
        await client.send_message(message.channel, content = "Your suggestion has been sent.")
        print("%s suggested '%s'\n" % (message.author, suggestion))



with open('H:/Misc/toaster3.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
