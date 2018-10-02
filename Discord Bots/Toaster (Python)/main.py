import discord
import praw
import pandas as pd
import random
import time
import sys
sys.path.append("H:/Misc")
import redditStuff as rs

client = discord.Client()
help = """**-help** - shows this \n**-ping** - pings the bot
**-invite** - gives an invite link so you can add the bot to more servers.
**-poll [message]** - creates a poll.
**-meme** - pulls a random image from r/dankMemes or r/memes. There is some delay.
**-susquote** - pulls a random image from r/suspiciousquotes. There is some delay.
**-vw [message]** - vaporwave-ifies your message.
**-encode [message]** - encodes the message and DMs you the message and decode key.
**-decode, [message], [decode key]** - decodes the message and DMs you the decoded message."""



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users." % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Toaster | -help"))



@client.event
async def on_message(message):

    if message.channel.id == "494640468152549376":
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")
        await client.add_reaction(message, "🤷")



    if message.content.startswith("-help"):
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)



    if message.content.startswith("-ping"):
        await client.send_message(message.channel, content = "Pong!")
        print("%s pinged the bot." % message.author)



    if message.content.startswith("-invite"):
        await client.send_message(message.channel, content = "Invite me with this link! \nhttps://discordapp.com/oauth2/authorize?client_id=488570938581975041&scope=bot")
        print("%s is possibly inviting the bot to a new server!" % message.author)



    if message.content.startswith("-decode"):
        args = message.content.split(", ")
        args.pop(0)
        startingMsg = args[0]
        verystartmsg = startingMsg
        decodeKey = args[1].split("|")
        output = startingMsg
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if not message.channel.is_private:
            await client.delete_message(message)

        for a in decodeKey:
            startingMsg = output
            output = []

            for pos in range(len(startingMsg)):
                if startingMsg[pos] == " ":
                    output.append(" ")

                for letter in range(len(alphabet) - 26):
                    if startingMsg[pos] == alphabet[letter]:
                        output.append(alphabet[int(letter) - int(a)])

        sepe = ""
        a = []
        for i in output:
            a.append(i)

        await client.send_message(message.author, sepe.join(a))
        print("%s just decoded '%s' to get '%s'!" % (message.author, verystartmsg, sepe.join(a)))



    if message.content.startswith("-encode"):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        startingMsg = message.content
        startingMsg = startingMsg[8:]
        verystartmsg = startingMsg
        timesToReencode = random.randint(3,10)
        doneOnce = False
        decodeKey = []
        if not message.channel.is_private:
            await client.delete_message(message)

        for a in range(timesToReencode):
            if doneOnce:
                startingMsg = output
            output = []

            numForward = random.randint(1,25)

            decodeKey.append(numForward)

            for pos in range(len(startingMsg)):
                if startingMsg[pos] == " ":
                    output.append(" ")

                for letter in range(len(alphabet) - 26):
                    if startingMsg[pos] == alphabet[letter]:
                        output.append(alphabet[letter + numForward])

            doneOnce = True

        a = []
        sepe = ""
        for i in output:
            a.append(i)
        a2 = []
        sepe2 = "|"
        for i in decodeKey:
            a2.append(str(i))

        await client.send_message(message.author, sepe.join(a))
        await client.send_message(message.author, sepe2.join(a2))

        print("%s just encoded '%s' to get '%s'!" % (message.author, verystartmsg, sepe.join(a)))
        print("The decode key is:")
        print(*decodeKey, sep="|")



    if message.content.startswith("-vw") or message.content.startswith("-vw"):
        if not message.channel.is_private:
            await client.delete_message(message)
        msg = [message.content[4:]]
        vMessage = message.content[4:]
        vMessage = vMessage.replace(" ", "")
        a = []
        sepe = "  "
        for i in vMessage:
            a.append(i)

        await client.send_message(message.channel, sepe.join(a))
        print("%s just vaporwaved \"%s\"" % (message.author, *msg))



    if message.content.startswith("-jonathan"):
        args = message.content.split(", ")
        jonathan = "<@136664437431074816>"
        try:
            a = args[3]
        except:
            print("%s tried to ping jonathan but didn't input enough arguments!" % message.author)
            await client.send_message(message.channel, content = "You didn't use enough arguments! Do -help for help, you **VERY FINE MEMBER OF THE LBGT COMMUNITY**.")
            return

        try:
            interval = float(args[1])
        except:
            print("%s tried to ping jonathan but didnt use a number as the interval!" % message.author)
            if args[1] == "":
                args[1] = None
            await client.send_message(message.channel, content = "%s isn't a number! Try again you **RATHER LARGE GAY CHILD**." % args[1])
            return

        try:
            amount = int(args[2])
        except:
            print("%s tried to ping jonathan but didnt use a number as the amount!" % message.author)
            if args[2] == "":
                args[2] = None
            await client.send_message(message.channel, content = "%s isn't a number! Try again you **REALLY REALLY NOT STRAIGHT MEMBER OF THE HUMAN SPECIES**." % args[2])
            return

        msg = args[3]
        highLimit = 100
        lowLimit = 1

        if amount > highLimit:
            print("%s tried to ping jonathan but used too high of an amount." % message.author)
            await client.send_message(message.channel, content = "You can't send more than %s messages! Nice try you **LARGE HOMOSEXUAL**." % highLimit)
            return

        if amount < lowLimit:
            print("%s tried to ping jonathan but used too low of an amount." % message.author)
            await client.send_message(message.channel, content = "You can't send a negative (or zero) amount of messages! Nice try you **LARGE HOMOSAPIEN**.")
            return

        print("Pinging Jonathan %s times, with message '%s', at a speed of %s" % (amount, msg, interval))

        for i in range(amount):
            await client.send_message(message.channel, content = "%s: %s %s" % (i+1, jonathan, msg))
            time.sleep(interval)



    if message.content.startswith("-poll"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

        print("%s called a poll." % message.author)



    if message.content.startswith("Idea:"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")
        await client.add_reaction(message, "🤷")

        print("%s had an idea." % message.author)



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
            print("%s tried to start a stream without the 'Toaster' role." % message.author)
            await client.send_message(message.channel, content = "You don't have the correct role to do this!")



    if message.content.startswith("-meme"):
        rand1 = random.randint(0,1)
        if rand1 == 0:
            subreddit = rs.reddit.subreddit('dankMemes')
        else:
            subreddit = rs.reddit.subreddit('memes')

        top_subreddit = subreddit.hot(limit = 200)
        posts = []

        for submission in top_subreddit:
            posts.append(submission.url)

        rand1 = random.randint(0,len(posts)-1)
        randpost = posts[rand1]

        await client.send_message(message.channel, content = randpost)
        print("%s called a meme." % message.author)



    if message.content.startswith("-susquote"):
        subreddit = rs.reddit.subreddit('suspiciousquotes')

        top_subreddit = subreddit.top(limit = 200)
        posts = []

        for submission in top_subreddit:
            posts.append(submission.url)

        rand1 = random.randint(0,len(posts)-1)
        randpost = posts[rand1]

        await client.send_message(message.channel, content = randpost)
        print("%s called a suspicious quote." % message.author)



with open('H:/Misc/token.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
