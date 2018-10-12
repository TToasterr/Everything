import discord
import sys
sys.path.append("H:/Misc")

client = discord.Client()
help = """**.help** - Shows this.
**.invite** - Gives you an easy invite link for the bot.
**.stalk** - Turns on stalking for this server.
**.vw [message], [spaces amount]** - Vaporwaves your message with the specified amount of spaces.""" #The commands (what shows up when you do .help)



@client.event
async def on_ready(): #when the bot starts up
    activeServers = client.servers #activeServers is the servers the bot is in
    sum = 0 #sum = 0
    for s in activeServers: #for each server in active Servers
        sum += len(s.members) #get the member count and add it to the sum.
    print("Bot started in %s server(s), with %s users." % (len(client.servers), sum)) #print the server count and member count
    await client.change_presence(game=discord.Game(name="Toaster 2.0 | .help")) #change presence to show the help command



@client.event
async def on_message(message): #when a message is sent
    global content

    activeServers = client.servers
    msg = message.content #msg is the message the user sent

    #Try to open the servers file (stores data about whether its stalking or not and such)
    try:
        with open(("%s\stalking.txt" % message.server.name), "r") as sFile:
            if message.author.bot: #stop doin this gay shit if its a bot
                return()
            a = sFile.read()
            if a == "1":
                print("%s | #%s | %s: %s" % (message.server.name, message.channel, message.author, message.content))
    #If it cant find the file, create one
    except:
        with open(("%s\stalking.txt" % message.server.name), "w+") as serverFile:
            asdfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa = "i want to die please kthx" #dont I just have the best code

    #If the message is the help command, send help
    if msg == ".help":
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)

    #Invite command (gives invite link)
    if msg == ".invite":
        await client.send_message(message.channel, content = "https://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s got an invite link." % message.author)

    #Stalk command (prints every message sent into a server into console if on)
    if msg == ".stalk":
        print("%s toggled stalking for %s." % (message.author, message.server.name))

        with open(("%s\stalking.txt" % message.server.name), "r") as sFile:
            content = sFile.read()

        with open(("%s\stalking.txt" % message.server.name), "w+") as serverFile:
            if content == "":
                serverFile.write("0" % message.server.name)
            else:

                if content == "1":
                    content = "0"
                    await client.send_message(message.channel, content = "Stalking turned off for **%s**." % message.server.name)
                else:
                    content = "1"
                    await client.send_message(message.channel, content = "Stalking turned on for **%s**." % message.server.name)
                serverFile.write(content)

    #vaporwave command
    if msg[:3] == ".vw":
        if not message.channel.is_private:
            await client.delete_message(message)
        args = msg[4:].split(", ")
        mesg = args[0]
        spaceamount = args[1]
        final = []
        print("%s vaporwaved \"%s\" with %s space(s)." % (message.author, mesg, spaceamount))

        for char in mesg:
            final.append(char)

        spaces = " " * int(spaceamount)
        final = spaces.join(final)
        await client.send_message(message.channel, content = final)



#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token3.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
