import discord
import random
import time

client = discord.Client()
help = "**-help** - shows this \n**-ping** - pings the bot \n**-whoami** - gives users name and account creation date \n**-jonathan, [time interval], [amount of times], [message]** - pings jonathan the amount of times specified. Because of Discord spam limits, sends messages in bursts of 5. \n**-poll [message]** - creates a poll."



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-help"):
        await client.send_message(message.channel, content = help)

    if message.content.startswith("-ping"):
        await client.send_message(message.channel, content = "Pong!")

    if message.content.startswith("-whoami"):
        await client.send_message(message.channel, content = "You're **%s**! \nYou've been on discord since `%s`" % (message.author, message.author.created_at))

    if message.content.startswith("-jonathan"):
        args = message.content.split(", ")
        jonathan = "<@136664437431074816>"
        try:
            a = args[3]
        except:
            print("A user tried to ping jonathan but didn't input enough arguments!")
            await client.send_message(message.channel, content = "You didn't use enough arguments! Do -help for help, you **VERY FINE MEMBER OF THE LBGT COMMUNITY**.")
            return

        try:
            interval = float(args[1])
        except:
            print("A user tried to ping jonathan but didnt use a number as the interval!")
            if args[1] == "":
                args[1] = None
            await client.send_message(message.channel, content = "%s isn't a number! Try again you **RATHER LARGE GAY CHILD**." % args[1])
            return

        try:
            amount = int(args[2])
        except:
            print("A user tried to ping jonathan but didnt use a number as the amount!")
            if args[2] == "":
                args[2] = None
            await client.send_message(message.channel, content = "%s isn't a number! Try again you **REALLY REALLY NOT STRAIGHT MEMBER OF THE HUMAN SPECIES**." % args[2])
            return

        msg = args[3]
        highLimit = 100
        lowLimit = 1

        if amount > highLimit:
            print("A user tried to ping jonathan but used too high of an amount.")
            await client.send_message(message.channel, content = "You can't send more than %s messages! Nice try you **LARGE HOMOSEXUAL**." % highLimit)
            return

        if amount < lowLimit:
            print("A user tried to ping jonathan but used too low of an amount.")
            await client.send_message(message.channel, content = "You can't send a negative (or zero) amount of messages! Nice try you **LARGE HOMOSAPIEN**.")
            return

        print("Pinging Jonathan %s times, with message '%s', at a speed of %s" % (amount, msg, interval))

        for i in range(amount):
            await client.send_message(message.channel, content = "%s: %s %s" % (i+1, jonathan, msg))
            time.sleep(interval)

    if message.content.startswith("-poll"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    if message.content.startswith("-streaming"):

        if "450865638576095232" in [y.id for y in message.author.roles]:
            args = message.content.split(", ")

            try:
                game = args[1]
            except:
                print("Toaster tried to announce a stream but didnt use enough arguments.")
                await client.send_message(message.channel, content = "You didn't input enough arguments!")
                return

            if game == "testing":
                print("Toaster announced a test stream.")
                await client.send_message(client.get_channel("451206133810724864"), content = "Toaster would be live, but this is just a test announcement!")
                return

            print("Toaster announced a stream, with %s as the game." % game)

            await client.send_message("451206133810724864", content = "Toaster is live, playing %s! Check it out: \nhttps://www.twitch.tv/ttoasterrr")

        else:
            print("Someone tried to start a stream without the 'Toaster' role.")
            await client.send_message(message.channel, content = "You don't have the correct role to do this!")



with open('C:/Users/matth/Desktop/Everything/token.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
