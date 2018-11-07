import discord
import sys
from random import randint as ri
from random import choice as ch
from discord.utils import get
sys.path.append("H:/Misc")
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files")

client = discord.Client()
help1 = """
----------------------------__**General Commands**__----------------------------
These commands can be done by anyone.

**.help 1** - Shows this.
**.help 2** - Showed Mod help.
**.planning** - Lists the commands or ideas that I'm currently planning or thinking about. Suggest something and it might appear here!
**.invite** - Gives you an easy invite link for the bot.

**.suggest [suggestion]** - Will suggest the suggestion to the bot owner. Please keep it (roughly) to commands or fixes.
**.botstats** - Returns the bots stats.
**.github** - Gives you the link to the bot's github.

**.vw [message], [spaces amount]** - Vaporwaves your message with the specified amount of spaces.
**.weeb [message]** - Weebifies the message. (turns every 'r' into a 'w', turns every 'o' into 'owo')
**.genrandominvite [number]** - Generates the number of random discord invite links. The number cant go above 20. Will it be a real server? Almost definetely not.
"""
help2 = """
----------------------------__**Moderator Commands**__----------------------------
These can only be done with people who have the moderator roles (added with .addrole) or who have the 'admin' permission.

**.stalk** - Turns on stalking for this server. Sends every message sent in the server into the bot's console. Dont know why you'd want this, it was just me testing server-specific settings.

__**Moderator Roles**__
**.addrole [id]** - Adds a moderator role by ID. To get a role id, ping it and add a backslash before the @ sign. You should get <@ID>. Copy the id.
**.delrole [id]** - Removes a moderator role by ID.
**.listroles** - Lists all moderator roles.

__**AutoResponder**__
**.addresponse [trigger], [response]** - Adds an autoresponder response.
**.delresponse [trigger]** - Removes the responses with said trigger.
**.listresponses** - Lists all autoresponder responses for this server.

__**Channel Reactions**__
**.addchannelreaction [channel], [reaction]** - Adds a reaction to every message sent in the channel you say.
**.delchannelreaction [channel], [reaction]** - Deletes the reaction from the channel.
**.listchannelreactions** - Lists all server channel reactions.
"""
planning = """
----------------------------__**Planning**__----------------------------
These are the commands and such that I'm planning on adding!

**.addreaction [trigger], [reaction]** - Essentially an Autoresponder except with reactions.
**.delreaction [trigger]** - Deletes an autoreaction
**.listreactions** - Lists reactions for this server.

**Some Hangman Game** - Havent put too much thought into this, but .suggest it if you like it!
Tally for hangman - ||

**search, word, msg, split** - Options for autoresponder, do .ex respondertags
"""



@client.event
async def on_ready(): #when the bot starts up
    activeServers = client.servers #activeServers is the servers the bot is in
    sum = 0 #sum = 0
    for s in activeServers: #for each server in active Servers
        sum += len(s.members) #get the member count and add it to the sum.
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum)) #print the server count and member count
    await client.change_presence(game=discord.Game(name="Toaster 2.0 | .help")) #change presence to show the help command



@client.event
async def on_server_join(server):
    print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message): #when a message is sent
    global content

    if message.channel.is_private and not (message.author.bot):
        await client.send_message(message.channel, content = "This bot doesnt work with DMs (sorry!). Invite me to a server and use me there!\nhttps://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s tried to DM the bot.\n" % message.author)
        return()

    if message.author.bot:
        return()

    activeServers = client.servers
    msg = message.content #msg is the message the user sent
    mod = False

    #Try to open the servers file (stores data about whether its stalking or not and such)
    try:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-stalking.txt" % message.server.name), "r") as sFile:
            if message.author.bot: #stop doin this gay shit if its a bot
                return()
            a = sFile.read()
            if a == "1":
                print("%s | #%s | %s: %s\n" % (message.server.name, message.channel, message.author, message.content))
    #If it cant find the file, create one
    except:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-stalking.txt" % message.server.name), "w+") as stalkingFile:
            stalkingFile.write("0")



    try:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "r") as modFile:
            modRoles = modFile.read().split("\n")

    except:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "w+") as stalkingFile:
            stalkingFile.write("")



    try:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "r") as arFile:
            ar = arFile.read().split("---")
            for num in range(len(ar) - 1):
                i = ar[num].split(" -> ")
                if str(i[0])[1:].lower() in message.content.lower():
                    await client.send_message(message.channel, content = i[1])

    except:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "w+") as arFile:
            asdf = "asdf"



    try:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "r", encoding="UTF-8") as reactfile:
            reactions = reactfile.read().split("\n")
            for i in range(len(reactions) - 1):
                a = reactions[i].split(", ")
                if a[0] == message.channel.id:
                    if a[1][0] == "<":
                        a[1] = a[1].split(":")
                        a[1].pop(0)
                        a[1].pop(1)
                        a[1] = str(a[1])[2:-2]
                        emoji = get(client.get_all_emojis(), name=a[1])
                        a[1] = emoji
                    await client.add_reaction(message, a[1])

    except FileNotFoundError:
        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "w+") as reactfile:
            reactfile.write("")



    #Help command
    if msg == ".help 1" or msg == ".help":
        await client.send_message(message.channel, content = help1)
        print("%s asked for help.\n" % message.author)
    if msg == ".help 2":
        await client.send_message(message.channel, content = help2)
        print("%s asked for the Mod help.\n" % message.author)
    if msg == ".planning":
        await client.send_message(message.channel, content = planning)
        print("%s got the planned commands.\n" % message.author)



    #Invite command (gives invite link)
    if msg == ".invite":
        await client.send_message(message.channel, content = "https://discordapp.com/oauth2/authorize?client_id=499928971711086601&scope=bot")
        print("%s got an invite link.\n" % message.author)



    if msg == ".ex respondertags":
        await client.send_message(message.channel, content = """For all examples, the trigger is 'xd'.
y means it would respond, n means it wouldnt.

**search:**
xd--------------------------y
i want to xd----------------y
i wantxd--------------------y
i want to x then d----------n

**word:**
xd--------------------------y
i want to xd----------------y
i wantxd--------------------n
i want to x then d----------n

**msg:**
xd--------------------------y
i want to xd----------------n
i wantxd--------------------n
i want to x then d----------n

**split:**
xd--------------------------y
i want to xd----------------y
i wantxd--------------------y
i want to x then d----------y""")



    #Stalk command (prints every message sent into a server into console if on)
    if msg == ".stalk":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        print("%s toggled stalking for %s.\n" % (message.author, message.server.name))

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-stalking.txt" % message.server.name), "r") as sFile:
            content = sFile.read()

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-stalking.txt" % message.server.name), "w+") as stalkingFile:
            if content == "":
                stalkingFile.write("0")
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
        try:
            args = msg[4:].split(", ")
            mesg = args[0]
            spaceamount = args[1]
        except:
            await client.send_message(message.channel, content = "You didn't supply enough arguments.")
            return()
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

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        try:
            msg = msg[13:].split(", ")
            trigger = msg[0]
            response = msg[1]
        except:
            await client.send_message(message.channel, content = "You didn't supply enough arguments.")
            return()

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "r") as arFile:
            ar = arFile.read().split("---")

        for num in range(len(ar) - 1):
            i = ar[num].split(" -> ")
            if str(i[0])[1:] == trigger:
                await client.send_message(message.channel, content = "You cant have two responses to the same word!")
                return()

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "a+") as arFile:
            arFile.write("\n%s -> %s\n---" % (trigger, response))

        await client.send_message(message.channel, content = "Your autoresponder has been added!")
        print("%s just added an autoresponder to %s.\nTrigger: '%s'\nResponse: '%s'\n" % (message.author, message.server.name, trigger, response))



    #more autoresponder
    if msg[:12] == ".delresponse":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        try:
            trigger = msg[13:]
        except:
            await client.send_message(message.channel, content = "You didn't supply enough arguments.")
            return()
        removed = 0
        popnum = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
        numb = 0

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "r") as arFile:
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

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "w+") as arFile:
            arFile.write("---".join(ar))

        if removed > 0:
            await client.send_message(message.channel, content = "%s trigger(s) have been removed." % removed)
            print("%s removed %s triggers from %s.\n" % (message.author, removed, message.server.name))
        else:
            await client.send_message(message.channel, content = "There werent any triggers with that name.")



    #List autoresponder responses
    if msg == ".listresponses":
        try:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-autoresponder.txt" % message.server.name), "r") as arFile:
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
        try:
            role = msg[9:]
        except:
            await client.send_message(message.channel, content = "You didn't supply enough arguments.")
            return()

        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "a+") as modFile:
            modFile.write("%s\n" % role)

        await client.send_message(message.channel, content = "Successfully added %s to the mod roles." % role)
        print("%s just added %s to the mod roles for %s.\n" % (message.author, role, message.server.name))



    #Delete a moderator role
    if msg[:8] == ".delrole":
        try:
            role = msg[9:]
            delCount = 0
        except:
            await client.send_message(message.channel, content = "You didn't supply enough arguments.")
            return()

        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        try:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "r") as modFile:
                modRoles = modFile.read().split("\n")

            for i in range(len(modRoles)-1):
                if modRoles[i] == role:
                    modRoles.pop(i)
                    delCount += 1

            if delCount == 0:
                await client.send_message(message.channel, content = "That role isnt a moderator role!")
            else:
                modRoles = "\n".join(modRoles)

                with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "w") as modFile:
                    modFile.write(modRoles)

                await client.send_message(message.channel, content = "Successfully deleted %s moderator role(s)" % delCount)
                print("%s deleted the moderator role %s from %s" % (message.author, role, message.server.name))

        except:
            await client.send_message(message.channel, content = "This server either has no moderator roles, or you formatted it wrong.")



    #List moderator roles
    if msg[:10] == ".listroles":
        try:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-modRoles.txt" % message.server.name), "r") as modFile:
                modRoles = modFile.read()

            await client.send_message(message.channel, content = modRoles)

        except:
            await client.send_message(message.channel, content = "This server either has no moderator roles, or you formatted it wrong.")



    #suggestions
    if msg[:8] == ".suggest":
        suggestion = msg[9:]

        if suggestion == "" or msg[8] != " ":
            await client.send_message(message.channel, content = "You didnt supply a suggestion!")
            return()

        me = await client.get_user_info("184474965859368960")
        await client.send_message(me, content = "%s suggests: \n%s" % (message.author, suggestion))
        await client.send_message(message.channel, content = "Your suggestion has been sent.")
        print("%s suggested '%s'\n" % (message.author, suggestion))



    #botstats
    if msg[:9] == ".botstats":
        activeServers = client.servers #activeServers is the servers the bot is in
        sum = 0 #sum = 0
        for s in activeServers: #for each server in active Servers
            sum += len(s.members) #get the member count and add it to the sum.
        await client.send_message(message.channel, content = "This bot is in %s server(s), with %s users." % (len(client.servers), sum))
        print("%s just got the bot stats.\n" % message.author)



    #github
    if msg[:7] == ".github":
        await client.send_message(message.channel, content = "https://github.com/TToasterr/Everything/tree/master/Discord%20Bots/Toaster%202.0%20(Python)")
        print("%s got the github link to the bot.\n" % message.author)



    #add channel reaction
    if msg[:19] == ".addchannelreaction" or msg == ".acr":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        args = msg[20:].split(", ")
        try:
            channel = args[0]
            channel = channel[2:20]
            reaction = args[1]
        except:
            await client.send_message(message.channel, content = "You didnt supply enough arguments!")
            return()

        with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "a+", encoding="UTF-8") as reactfile:
            reactfile.write("%s, %s\n" % (channel, reaction))

        await client.send_message(message.channel, content = "Your channel reaction has been added!")
        print("%s just added the channel reaction %s to channel %s.\n" % (message.author, reaction, channel))



    #delete channel reaction
    if msg[:19] == ".delchannelreaction" or msg == ".dcr":
        for i in modRoles:
            if i in [y.id for y in message.author.roles]:
                mod = True

        if message.author.server_permissions.administrator:
            mod = True

        if not mod:
            await client.send_message(message.channel, content = "You dont have the right role to do this.")
            return()

        args = msg[20:].split(", ")
        delcount = 0
        try:
            channel = args[0]
            channel = channel[2:20]
            reaction = args[1]
        except:
            await client.send_message(message.channel, content = "You didnt supply enough arguments!")
            return()

        try:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "r") as reactfile:
                reactions = reactfile.read().split("\n")
        except:
            await client.send_message(message.channel, content = "This server doesnt have any reactions yet!")
            return()

        for i in range(len(reactions)-1):
            reactions[i] = reactions[i].split(", ")
            if reactions[i][0] == channel:
                if reactions[i][1] == reaction:
                    reactions.pop(i)
                    delcount += 1
            reactions[i] = ", ".join(reactions[i])

        if delcount == 0:
            await client.send_message(message.channel, content = "That channel didn't have that reaction!")
            return()
        else:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "w") as reactfile:
                reactfile.write("\n".join(reactions))
            await client.send_message(message.channel, content = "Deleted reaction from channel!")
            print("%s just deleted a reaction from a channel.\n" % message.author)



    #list channel reactions
    if msg[:21] == ".listchannelreactions" or msg == ".lcr":
        try:
            with open(("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Toaster 2.0 (Python)/Server Files/%s-channelreactions.txt" % message.server.name), "r", encoding="UTF-8") as reactfile:
                reactions = reactfile.read().split("\n")
        except:
            await client.send_message(message.channel, content = "This server doesnt have any reactions yet!")
            return()

        for i in range(len(reactions)-1):
            reactions[i] = reactions[i].split(", ")
            reactions[i][0] = "<#%s>" % reactions[i][0]
            reactions[i] = " -> ".join(reactions[i])

        try:
            await client.send_message(message.channel, content = "\n".join(reactions))
            print("%s just got the reactions for %s.\n" % (message.author, message.server.name))
        except:
            await client.send_message(message.channel, content = "This server doesnt have any reactions yet!")



    #list servers (not in help message)
    if msg[:12] == ".listservers" or msg == ".ls":
        activeServers = client.servers
        servers = []
        for i in activeServers:
            servers.append(i.name)
        await client.send_message(message.channel, content = "\n".join(servers))
        print("%s just got the client servers.\n" % message.author)



    #weebify
    if msg[:5] == ".weeb":
        input = msg[6:]
        final = []
        lastletter = ""

        if input == "":
            await client.send_message(message.channel, content = "You didnt supply a message!")
            return()

        for letter in input:
            templetter = letter
            if letter == "o" and lastletter != "o":
                templetter = "owo"
            elif letter == "o" and lastletter == "o":
                templetter = ""

            if letter in {"r", "l"}:
                templetter = "w"

            lastletter = letter
            final.append(templetter)

        await client.send_message(message.channel, content = "".join(final))
        print("%s just weebified '%s'" % (message.author, input))



    #generate random invite
    if msg[:16] == ".genrandominvite" or msg[:4] == ".gri":
        try:
            args = msg.split(" ")
            args.pop(0)
            num = args[0]
            owo = 1
        except:
            nothing = "nothing"
            owo = 0
        lalphabet = "abcdefghijklmnopqrstuvwxyz"
        ualphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        inv = []
        final = []
        if owo == 1:
            for i in range(int(num)):
                inv = []
                for i in range(ri(5,7)):
                    which = ri(0,2)
                    if which == 0:
                        which2 = ri(0,25)
                        inv.append(str(lalphabet[which2]))
                    elif which == 1:
                        which2 = ri(0,25)
                        inv.append(str(ualphabet[which2]))
                    elif which == 2:
                        which2 = ri(0,9)
                        inv.append(str(which2))
                final.append("https://discord.gg/%s" % "".join(inv))
        else:
            for i in range(ri(5,7)):
                which = ri(0,2)
                if which == 0:
                    which2 = ri(0,25)
                    inv.append(str(lalphabet[which2]))
                elif which == 1:
                    which2 = ri(0,25)
                    inv.append(str(ualphabet[which2]))
                elif which == 2:
                    which2 = ri(0,9)
                    inv.append(str(which2))
            final.append("https://discord.gg/%s" % "".join(inv))
        await client.send_message(message.channel, content = "\n".join(final))
        print("%s just got a random invite.\n" % message.author)






#my super spooky way of hiding my token in a local file xd
with open('H:/Misc/token3.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
