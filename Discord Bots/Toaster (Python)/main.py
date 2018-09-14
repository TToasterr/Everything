import discord
import praw
import pandas as pd
import random
import time
import sys
sys.path.append("C:/Users/matth/Desktop/Everything")
import redditStuff as rs

client = discord.Client()
help = "**-help** - shows this \n**-ping** - pings the bot \n**-invite** - gives an invite link so you can add the bot to more servers. \n**-jonathan, [time interval], [amount of times], [message]** - pings jonathan the amount of times specified. Because of Discord spam limits, sends messages in bursts of 5. \n**-poll [message]** - creates a poll. \n**-meme** - pulls a random image from r/dankMemes or r/memes. There is some delay. \n**-susquote** - pulls a random image from r/suspiciousquotes. There is some delay."



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
    if message.author == client.user:
        return

    if message.content.startswith("-help"):
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)

    if message.content.startswith("-ping"):
        await client.send_message(message.channel, content = "Pong!")
        print("%s pinged the bot." % message.author)

    if message.content.startswith("-invite"):
        await client.send_message(message.channel, content = "Invite me with this link! \nhttps://discordapp.com/oauth2/authorize?client_id=488570938581975041&scope=bot")
        print("%s is possibly inviting the bot to a new server!" % message.author)

    if message.content.startswith("-timeLeft"):
        import time
        from datetime import datetime

        currentTime = int(datetime.now().strftime("%H%M"))
        time = 0

        start = 1350
        p1 = 1525
        p2 = 1715
        lunch = 1800
        p3 = 1935
        p4 = 2035

        def setTime():
            global time
            if time > 59 and time < 100:
                time -= 100
                time += 60
            elif time > 159 and time < 200:
                time -= 100
                time += 60

        if currentTime < start:
            await client.send_message(message.channel, content = "%s got the time left in this period, but school hasn't started yet!" % message.author)
            print("%s just got the time left!" % message.author)

        elif currentTime < p1:
            time = p1 - currentTime

            setTime()

            await client.send_message(message.channel, content = "%s got the time left in this period, and there was %s left in period 1!" % (message.author, time))
            print("%s just got the time left!" % message.author)

        elif currentTime < p2:
            time = p2 - currentTime

            setTime()

            await client.send_message(message.channel, content = "%s got the time left in this period, and there was %s left in period 2!" % (message.author, time))
            print("%s just got the time left!" % message.author)

        elif currentTime < lunch:
            time = lunch - currentTime

            setTime()

            await client.send_message(message.channel, content = "%s got the time left in this period, and there was %s left in lunch!" % (message.author, time))
            print("%s just got the time left!" % message.author)

        elif currentTime < p3:
            time = p3 - currentTime

            setTime()

            await client.send_message(message.channel, content = "There are %s left in period 3!" % time)
            print("%s just got the time left!" % message.author)

        elif currentTime < p4:
            time = p4 - currentTime

            setTime()

            await client.send_message(message.channel, content = "There are %s left in period 4!" % time)
            print("%s just got the time left!" % message.author)

        else:
            await client.send_message(message.channel, content = "School is over!")
            print("%s just got the time left!" % message.author)



    if message.content.startswith("-timeLeft"):
        import time
        from datetime import datetime

        currentTime = int(datetime.now().strftime("%H%M"))
        time = 0

        start = 1350
        p1 = 1525
        p2 = 1715
        lunch = 1800
        p3 = 1935
        p4 = 2035

        def setTime():
            global time
            if time > 59 and time < 100:
                time -= 100
                time += 60
            elif time > 159 and time < 200:
                time -= 100
                time += 60

        if currentTime < start:
            await client.send_message(message.channel, content="%s got the time left in this period, but school hasn't started yet!" % message.author)
            print("%s got the time left." % message.author)

        elif currentTime < p1:
            time = p1 - currentTime

            setTime()

            await client.send_message(message.channel, content="%s got the time left in this period, and there was %s left in period 1!" % (message.author, time))
            print("%s got the time left." % message.author)

        elif currentTime < p2:
            time = p2 - currentTime

            setTime()

            await client.send_message(message.channel, content="%s got the time left in this period, and there was %s left in period 2!" % (message.author, time))
            print("%s got the time left." % message.author)

        elif currentTime < lunch:
            time = lunch - currentTime

            setTime()

            await client.send_message(message.channel, content="%s got the time left in this period, and there was %s left in lunch!" % (message.author, time))
            print("%s got the time left." % message.author)

        elif currentTime < p3:
            time = p3 - currentTime

            setTime()

            await client.send_message(message.channel, content="There are %s left in period 3!" % time)
            print("%s got the time left." % message.author)

        elif currentTime < p4:
            time = p4 - currentTime

            setTime()

            await client.send_message(message.channel, content="There are %s left in period 4!" % time)
            print("%s got the time left." % message.author)

        else:
            await client.send_message(message.channel, content="School is over!")
            print("%s got the time left." % message.author)



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



with open('C:/Users/matth/Desktop/Everything/token.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
