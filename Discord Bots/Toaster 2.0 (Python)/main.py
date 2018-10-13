import discord
import sys
sys.path.append("H:/Misc")

client = discord.Client()
help = """**.help** - Shows this.
**.invite** - Gives you an easy invite link for the bot.
**.addrole [id]** - Adds a moderator role by ID. To get a role id, ping it and add a backslash before the @ sign.
**.stalk** - Turns on stalking for this server.
**.vw [message], [spaces amount]** - Vaporwaves your message with the specified amount of spaces.

__**AutoResponder**__
**.addresponse [trigger], [response]** - Adds an autoresponder response.
**.delresponse [name]** - Removes the responses with said name.
**.listresponses** - Lists all autoresponder responses for this server.""" #The commands (what shows up when you do .help)



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
    mod = False

    #Try to open the servers file (stores data about whether its stalking or not and such)
    try:
        with open(("%s-stalking.txt" % message.server.name), "r") as sFile:
            if message.author.bot: #stop doin this gay shit if its a bot
                return()
            a = sFile.read()
            if a == "1":
                print("%s | #%s | %s: %s" % (message.server.name, message.channel, message.author, message.content))
    #If it cant find the file, create one
    except:
        with open(("%s-stalking.txt" % message.server.name), "w+") as stalkingFile:
            stalkingFile.write("0" % message.server.name)



    try:
        with open(("%s-modRoles.txt" % message.server.name), "r") as modFile:
            modRoles = modFile.read().split("\n")

    except:
        with open(("%s-modRoles.txt" % message.server.name), "w+") as stalkingFile:
            stalkingFile.write("")



    try:
        with open(("%s-autoresponder.txt" % message.server.name), "r") as arFile:
            ar = arFile.read().split("---")
            for num in range(len(ar) - 1):
                i = ar[num].split(" -> ")
                if str(i[0])[1:] in message.content:
                    await client.send_message(message.channel, content = i[1])

    except:
        with open(("%s-autoresponder.txt" % message.server.name), "w+") as arFile:
            asdf = "asdf"



    #Help command
    if msg == ".help":
        await client.send_message(message.channel, content = help)
        print("%s asked for help.\n" % message.author)



    #Invite command (gives invite link)
    if msg == ".invite":
        await client.send_message(message.channel, content = "https://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s got an invite link.\n" % message.author)



    #Stalk command (prints every message sent into a server into console if on)
    if msg == ".stalk":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author == "Toaster#2600":
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        print("%s toggled stalking for %s.\n" % (message.author, message.server.name))

        with open(("%s-stalking.txt" % message.server.name), "r") as sFile:
            content = sFile.read()

        with open(("%s-stalking.txt" % message.server.name), "w+") as stalkingFile:
            if content == "":
                stalkingFile.write("0" % message.server.name)
            else:

                if content == "1":
                    content = "0"
                    await client.send_message(message.channel, content = "Stalking turned off for **%s**." % message.server.name)
                else:
                    content = "1"
                    await client.send_message(message.channel, content = "Stalking turned on for **%s**." % message.server.name)
                stalkingFile.write(content)



    #vaporwave command
    if msg[:3] == ".vw":
        if not message.channel.is_private:
            await client.delete_message(message)
        args = msg[4:].split(", ")
        mesg = args[0]
        spaceamount = args[1]
        final = []
        print("%s vaporwaved \"%s\" with %s space(s).\n" % (message.author, mesg, spaceamount))

        for char in mesg:
            final.append(char)

        spaces = " " * int(spaceamount)
        final = spaces.join(final)
        await client.send_message(message.channel, content = final)



    #server specific autoresponder
    if msg[:12] == ".addresponse":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author == "Toaster#2600":
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        msg = msg[13:].split(", ")
        trigger = msg[0]
        response = msg[1]

        with open(("%s-autoresponder.txt" % message.server.name), "r") as arFile:
            ar = arFile.read().split("---")

        for num in range(len(ar) - 1):
            i = ar[num].split(" -> ")
            if str(i[0])[1:] == trigger:
                await client.send_message(message.channel, content = "You cant have two responses to the same word!")
                return()

        with open(("%s-autoresponder.txt" % message.server.name), "a+") as arFile:
            arFile.write("\n%s -> %s\n---" % (trigger, response))

        await client.send_message(message.channel, content = "Your autoresponder has been added!")
        print("%s just added an autoresponder to %s.\nTrigger: '%s'\nResponse: '%s'\n" % (message.author, message.server.name, trigger, response))



    #more autoresponder
    if msg[:12] == ".delresponse":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author == "Toaster#2600":
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        trigger = msg[13:]
        removed = 0
        popnum = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
        numb = 0

        with open(("%s-autoresponder.txt" % message.server.name), "r") as arFile:
            ar = arFile.read().split("---")

        for num in range(len(ar) - 1):
            i = ar[num].split(" -> ")
            if str(i[0])[1:] == trigger:
                popnum[numb] = num
                numb += 1
                removed += 1

        for num in popnum:
            try:
                ar.pop(num)
            except:
                urmom = "gay"

        with open(("%s-autoresponder.txt" % message.server.name), "w+") as arFile:
            arFile.write("---".join(ar))

        if removed > 0:
            await client.send_message(message.channel, content = "%s trigger(s) have been removed." % removed)
            print("%s removed %s triggers from %s.\n" % (message.author, removed, message.server.name))
        else:
            await client.send_message(message.channel, content = "There werent any triggers with that name.")



    #List autoresponder responses
    if msg == ".listresponses":
        try:
            with open(("%s-autoresponder.txt" % message.server.name), "r") as arFile:
                ar = arFile.read().split("---")

            if ar == [""]:
                await client.send_message(message.channel, content = "This server doesnt have any autoresponses.")
                return()

            ar = "".join(ar)
            await client.send_message(message.channel, content = ar)

        except:
            await client.send_message(message.channel, content = "This server doesnt have any autoresponses.")



    #Add a moderator role
    if msg[:8] == ".addrole":
        role = msg[9:]

        with open(("%s-modRoles.txt" % message.server.name), "a+") as modFile:
            modFile.write("%s\n" % role)

        await client.send_message(message.channel, content = "Successfully added %s to the mod roles." % role)
        print("%s just added %s to the mod roles for %s.\n" % (message.author, role, message.server.name))






#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token3.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
