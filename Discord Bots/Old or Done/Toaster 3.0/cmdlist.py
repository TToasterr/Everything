class command:
    def __init__(self, who, name, rname, alias, desc, type, code):
        self.who = who
        self.name = name
        self.rname = rname
        self.alias = alias
        self.desc = desc
        self.type = type
        self.code = code



linebreak = "\n"



#help
help = command("anyone","help","t.help","?","Lists all commands.","general","")



#say
say = command("anyone","say","t.say [message]","say","Makes the bot say whatever you want.","fun","""
def cmd(msg, message, me, wks):
    global cmdOut

    if msg[:5] == "t.say":
        cmdOut = msg[6:]
        print(\"%s made the bot say \'%s\' \" % (message.author, msg[6:]))
    else:
        cmdOut = msg[4:]
        print(\"%s made the bot say \'%s\' \" % (message.author, msg[4:]))
""")



#invite
invite = command("anyone","invite","t.invite","inv","Gives you an invite link for the bot.","general","""
def cmd(msg, message, me, wks):
    global cmdOut

    cmdOut = "https://discordapp.com/oauth2/authorize?client_id=507155028948287490&scope=bot"
    print(\"%s got an invite link. \" % message.author)
""")



#vaporwave
vaporwave = command("anyone","vaporwave","t.vaporwave [message], [amount of spaces]","vwave","Vaporwaves your message with the given amount of spaces.","fun","""
def cmd(msg, message, me, wks):
    global cmdOut

    try:
        args = msg[12:] if msg[:11] == "t.vaporwave" else msg[7:]
        args = args.split(", ")
        input = args[0]
        spaceAmm = args[1]
    except:
        cmdOut = "You didnt use enough arguments!"
        print(\"%s tried to vaporwave but didn't use enough args. \" % (message.author))
        return()

    final = []

    for char in input:
        final.append(char)

    spaces = " " * int(spaceAmm)

    final = spaces.join(final)

    cmdOut = final
    print(\"%s vaporwaved '%s'. \" % (message.author, input))
""")



#suggest
suggest = command("anyone","suggest","t.suggest [message]","sug","Suggests something to the author of the bot. \nKeep it to command ideas.","general","""
def cmd(msg, message, me, wks):
    global cmdOut, suggestion

    failed = 0

    try:
        suggestion = msg[10:] if msg[:9] == "t.suggest" else msg[6:]
    except:
        failed = 1

    doMsgOut = True
    if not failed:
        cmdOut = "Your suggestion was sent!"
        print(\"%s suggested '%s'. \" % (message.author, suggestion))

    else:
        cmdOut = "You didn't give a suggestion!"
        print(\"%s tried to suggest but didnt give a suggestion. \" % (message.author))
""")



#stalk
stalk = command("mods","stalk","t.stalk","st","Turns on or off stalking for the server you do it in. \nPrints every message into console.","general","""
def cmd(msg, message, me, wks):
    global cmdOut

    if message.author.server_permissions.administrator or message.author.server_permissions.manage_server:
        if int(wks.cell("A1").value) == 0:
            wks.cell("A1").value = 1
            cmdOut = "Stalking has been turned on for this server!"
            print("%s turned stalking on for %s" % (message.author, message.server.name))
        else:
            wks.cell("A1").value = 0
            cmdOut = "Stalking has been turned off for this server!"
            print("%s turned stalking off for %s" % (message.author, message.server.name))

    else:
        cmdOut = "You dont have the right permissions to toggle stalking for this server."
        print("%s tried to toggle stalking but didnt have permission." % message.author)
""")



#botstats
botstats = command("anyone","botstats","t.botstats","bs","Gives you the bot statistics.","general","""
def cmd(msg, message, me, wks):
    global cmdOut

    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    cmdOut = "This bot is in %s server(s), with %s users." % (len(client.servers), sum)
    print("%s just got the bot stats." % message.author)
""")



#addresponse
addresponse = command("mods","addresponse","t.addresponse [trigger], [response]","addres","Adds an autoresponse to the server.","autores","""
def cmd(msg, message, me, wks):
    global cmdOut

    if message.author.server_permissions.administrator or message.author.server_permissions.manage_server:
        args = msg[14:] if msg[:13] == "t.addresponse" else msg[9:]
        args = args.split(", ")
        trigger = args[0]
        response = args[1]
        done = 0

        autoresponses = wks.range("B1:B50")
        for x in autoresponses:
            x = str(x[0])
            x = x[6:]
            x = x[:-1]
            x = x.split(" ")

            if x[1] == "''" and done == 0:
                celll = x[0]
                done = 1

        wks.cell(celll).value = ("%s -->> %s" % (trigger, response))

        cmdOut = "Sucesfully added trigger '%s' with response '%s'." % (trigger, response)
        print("%s added an autoresponse to %s." % (message.author, message.server.name))

    else:
        cmdOut = "You dont have the right permissions to add a response to this server."
        print("%s tried to add a response but didnt have permission." % message.author)
""")



#delresponse
delresponse = command("mods","delresponse","t.delresponse [trigger]","delres","Deletes an autoresponse from the server.","autores","""
def cmd(msg, message, me, wks):
    global cmdOut

    if message.author.server_permissions.administrator or message.author.server_permissions.manage_server:
        trigger = msg[14:] if msg[:13] == "t.delresponse" else msg[9:]
        done = 0

        autoresponses = wks.range("B1:B50")
        for x in autoresponses:
            x = str(x[0])
            x = x[6:]
            x = x[:-1]
            x = x.split(" ")

            try:
                if x[1] == "'%s" % trigger and done == 0:
                    celll = x[0]
                    done = 1
            except:
                do = "nothing"

        try:
            wks.cell(celll).value = ""

            cmdOut = "Sucesfully deleted trigger '%s'." % (trigger)
            print("%s deleted an autoresponse from %s." % (message.author, message.server.name))
        except:
            cmdOut = "That trigger doesnt exist!"
            print("%s tried to delete an autoresponse from %s that didnt exist." % (message.author, message.server.name))

    else:
        cmdOut = "You dont have the right permissions to delete a response from this server."
        print("%s tried to delete a response but didnt have permission." % message.author)
""")



#listresponses
listresponses = command("anyone","listresponses","t.listresponses","listresps","Lists all autoresponses for the server.","autores","""
def cmd(msg, message, me, wks):
    global cmdOut

    final = []

    autoresponses = wks.range("B1:B50")
    for x in autoresponses:
        x = str(x[0])
        x = x[6:]
        x = x[:-1]
        x = x.split(" ")

        if x[1] != "''":
            x.pop(0)
            final.append(" ".join(x))

    if final != []:
        cmdOut = "\\n".join(final)
        print("%s listed autoresponses for %s." % (message.author, message.server.name))
    else:
        cmdOut = "There are no autoresponses on this server."
        print("%s listed autoresponses for %s." % (message.author, message.server.name))
""")



#Toggle message storage
toggleStorage = command("mods","togglestorage","t.togglestorage","tstore","Toggles on or off the storage of messages for the server. \n\nStoring messages will let you use a command that randomly picks a message and sends it.","strg","""
def cmd(msg, message, me, wks):
    global cmdOut

    if message.author.server_permissions.administrator or message.author.server_permissions.manage_server:
        try:
            store = int(wks.cell("A2").value)
            if store == 0:
                wks.cell("A2").value = 1
            else:
                wks.cell("A2").value = 0
        except:
            wks.cell("A2").value = 0
            store = 1

        out = "on" if store == 0 else "off"
        cmdOut = "Message storing changed to %s." % out
        print("%s toggled message storage for %s" % (message.author, message.server.name))

    else:
        cmdOut = "You dont have the right permissions to toggle message storing foe this server."
        print("%s tried to toggle message storage but didnt have permission." % message.author)
""")



getMsg = command("anyone","getmsg","t.getmsg","gmg","If message storage is turned on, it will give a random message in storage.","strg","""
def cmd(msg, message, me, wks):
    from random import choice as ch
    global cmdOut

    if wks.cell("A2").value == "0":
        cmdOut = "Message storage isnt on for this server!"
        print("%s tried to get a random message, but message storage wasnt turned on." % message.author)
        return()

    with open("C:/Users/matth/Documents/GitHub/Everything/Discord Bots/Bot Limbo/Toaster 3.0/server message storage/%s.txt" % message.server.name, "r") as serverFile:
        uwu = serverFile.read().split(linebreak)

    cmdOut = ch(uwu)
    print("%s got a random message from %s" % (message.author, message.server.name))
""")



weeb = command("anyone","weeb","t.weeb [message]","wb","Weebifies your message! Changes all 'r's and 'l's to w, and all 'o's to owo.","fun","""
def cmd(msg, message, me, wks):
    global cmdOut
    input = msg[7:] if msg[:6] == "t.weeb" else msg[5:]
    final = []
    lastletter = ""

    if input == "":
        cmdOut = "You didnt supply a message."
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

    cmdOut = "".join(final)
    print("%s just weebified '%s'" % (message.author, input))
""")



choose = command("anyone","choose","t.choose [choice 1], [choice 2]...","ch","Chooses between the given choices.","general","""
def cmd(msg, message, me, wks):
    global cmdOut
    from random import choice as ch

    choices = msg[9:].split(", ") if msg[9] != " " else msg[5:].split(", ")
    cmdOut = ch(choices)
    print("%s made the bot choose between '%s'" % (message.author, ", ".join(choices)))
""")



default = command("anyone","name","rname","alias","desc","type","""
def cmd(msg, message, me, wks):
    global cmdOut
""")



#afk and statuses
#suggestions list
#'approve' suggestions
#removing suggestions



cmdArr = [
help,
say,
invite,
vaporwave,
suggest,
botstats,
stalk,
addresponse,
delresponse,
listresponses,
toggleStorage,
getMsg,
weeb,
choose
]
