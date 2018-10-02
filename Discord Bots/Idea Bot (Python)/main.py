from time import sleep as slp
import discord
import praw
import pandas as pd
import sys
sys.path.append("H:/Misc")



client = discord.Client()
help = """**//help** - shows this.
**//idea [idea]** - add an idea to the idea list.
**//listideas** - lists all ideas, with numbers.
**//vote [idea number] [vote number] [yes/no/maybe]** - lets you vote on an idea."""



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users." % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="Idea Bot | //help"))



@client.event
async def on_message(message):

    if message.content.startswith("//help"):
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)



    elif message.content.startswith('//idea'):
        idea = message.content[7:]
        with open('ideas.txt', 'a+') as ideas:
            ideas.write(idea)
            ideas.write('\n---\n')

        with open('votes.txt', 'a+') as votes:
            votes.write('4444')
            votes.write('\n---\n')

        await client.send_message(message.channel, content = 'Your idea has been added!')



    elif message.content.startswith('//listideas'):
        msg = []

        with open('ideas.txt', 'r') as ideas:

            with open('votes.txt', 'r') as votes:

                ideas = ideas.read().split('---')
                votes = votes.read().split('---')

                for i in range(len(ideas) - 1):
                    await client.send_message(message.channel, content = i)

                    await client.send_message(message.channel, content = ideas[i])

                    for number in range(len(votes[i]) - 1):
                        if votes[i][number] == '0':
                            msg.append('👎')
                        elif votes[i][number] == '1':
                            msg.append('🤷')
                        elif votes[i][number] == '2':
                            msg.append('👍')
                        elif votes[i][number] == '4':
                            msg.append('no vote')


                    sepe = ', '
                    await client.send_message(message.channel, content = sepe.join(msg))
                    msg = []

                    await client.send_message(message.channel, content = '--------------')
                    slp(3)



    elif message.content.startswith('//vote'):
        message = message.content.split(' ')
        message.pop(0)
        try:
            ideanumber = message[0]
            votenumber = message[1]
            vote = messate[2]
        except:
            await client.send_message(message.channel, content = 'You didnt use enough arguments!')
            return

        if not ("489996858865745932" in [y.id for y in message.author.roles]):
            await client.send_message(message.channel, content = 'You dont have the correct permission to vote!')
            return

        if not (vote == 'yes' or vote == 'no' or vote == 'maybe'):
            await client.send_message(message.channel, content = 'You didnt use a correct voting type! Make sure to do "yes", "no", or "maybe".')
            return

        if vote == 'yes':
            vote = 2
        elif vote == 'maybe':
            vote = 1
        elif vote == 'no':
            vote = 0

        with open('votes.txt', 'r') as votess:
            votes = votess.read().split('---')
            votes[ideanumber][votenumber] = vote
            with open('tempvotes.txt', 'w+') as tempvotes:
                tempvotes.write(votes)
                
        with open('votes.txt', 'w') as votess:
            with open('tempvotes.txt', 'r') as tempvotes:
                tempvotes = tempvotes.read()
                votess.write(tempvotes)
                
        await client.send_message(message.channel, content = 'Your vote has been added.')



with open('H:/Misc/token2.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
