import discord
import random

client = discord.Client()
help = "-help - shows this \n-ping - pings the bot \n-whoami - gives users name and account creation date \n-annoyJonathan [amount of times] - pings jonathan the amount of times specified. Because of Discord spam limits, sends messages in bursts of 5. \n-poll [message] - creates a poll."



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

    if message.content.startswith("-annoyJonathan"):
        howmany = int(message.content[14:])
        
        jonathan = "<@136664437431074816>"
        
        if howmany < 10 and howmany > 0:
            msg = message.content[16:]
        elif howmany < 99:
            msg = message.content[17:]
        elif howmany > 99:
            await client.send_message(message.channel, content = "That amount is too high! Please try again you ***LARGE HOMOSEXUAL***.")
            return
        else:
            await client.send_message(message.channel, content = "That amount is too low! Please try again you ***LARGE HOMOSEXUAL***.")
            return
        
        msgNum = 1
        for i in range(howmany):
            await client.send_message(message.channel, content = "%s: %s %s" % (msgNum, jonathan, msg))
            msgNum += 1

    if message.content.startswith("-poll"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")



with open('C:/Users/matth/Desktop/Everything/token.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
