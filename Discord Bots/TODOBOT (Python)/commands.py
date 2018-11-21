class command:
    def __init__(self, name, use, desc, category, who, function):
        self.name = name
        self.use = use
        self.desc = desc
        self.category = category
        self.who = who
        self.function = function

    def getHelp(self):
        global embed
        embed = discord.Embed(title=(self.name), description=(self.use), color=0x00ff00)
        embed.add_field(name="-", value="%s\n\nAlias: %s\nWho can use it: %s" % (self.desc, self.alias, self.who))

    def returnError(self, error):
        global embed
        embed = discord.Embed(title=(self.name), description=(self.use), color=0x00ff00)
        embed.add_field(name="-", value="**Error:**\n%s" % error)



help = command("help", "td.help [command name]", "Gives the help for the specified command.", "general", "anyone", """
embed = ""
messageOut = ""
genCommands = []

embed = discord.Embed(title=(help.name), description=(help.use), color=0x00ff00)
for command in commandList:
    if command.category == "general":
        genCommands.append(command)
embed.add_field(name="General Commands", value="\\n".join([(command.name) for command in genCommands]), inline=False)
""")

addreminder = command("addreminder", "td.addreminder [reminder name], [reminder message], [HHMM in military time]", "Adds a reminder at the time of day given.", "general", "anyone", """
embed = ""
messageOut = ""
done = 0

try:
    args = msg[15:].split(", ")
    name = args[0]
    mssg = args[1]
    time = args[2]
except:
    addreminder.returnError("You didn't supply enough arguments!\\nMake sure to check your commas.")
    done = 1

if done == 0:
    embed = discord.Embed(title=(addreminder.name), description=(addreminder.use), color=0x00ff00)
    embed.add_field(name="-", value="Sucesfully added reminder with name **%s**!" % name, inline=False)
""")

addrecreminder = command("addrecreminder", "td.addrecreminder [reminder name], [reminder message], [HHMM in military time]", "Adds a recurring reminder at the time of day given.\nThis means that every day, the reminder will be said.", "general", "anyone", """
embed = ""
messageOut = ""
done = 0

try:
    args = msg[18:].split(", ")
    name = args[0]
    mssg = args[1]
    time = args[2]
except:
    addrecreminder.returnError("You didn't supply enough arguments!\\nMake sure to check your commas.")
    done = 1

if done == 0:
    embed = discord.Embed(title=(addreminder.name), description=(addreminder.use), color=0x00ff00)
    embed.add_field(name="-", value="Sucesfully added recurring reminder with name **%s**!" % name, inline=False)
""")


commandList = [
    help,
    addreminder,
    addrecreminder
]
