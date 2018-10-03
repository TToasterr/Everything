from time import sleep as slp
import discord
import sys
# sys.path.append("H:/Misc")



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
    await client.change_presence(game=discord.Game(name="Idea Bot ||  //help"))



@client.event
async def on_message(message):

    if message.content.startswith("//help"):
        await client.send_message(message.channel, content = help)
        print("%s asked for help." % message.author)



    elif message.content.startswith('//idea'):
        idea = message.content[7:]
        with open('ideas.txt', 'a+') as ideas:
            ideas.write(idea)
            ideas.write('\n--\n')
            ideas.write('4444')
            ideas.write('\n-----\n')

        await client.send_message(message.channel, content = 'Your idea has been added!')



    elif message.content.startswith('//listideas'):
        msg = []
        final = []

        with open('ideas.txt', 'r+') as ideas:

            ideas = ideas.read().split('---')
            votes = ''.join(ideas)
            votes = votes.split('--')
            del votes[::2]

            for i in range(len(ideas) - 1):
                final.append(str(i))
                final.append('\n')
                final.append(ideas[i])

                for number in range(5):
                    if votes[i][number] == '0':
                        msg.append('👎')
                    elif votes[i][number] == '1':
                        msg.append('🤷')
                    elif votes[i][number] == '2':
                        msg.append('👍')
                    elif votes[i][number] == '4':
                        msg.append('no vote')

                final.append(', '.join(msg))
                msg = []

                final.append('\n**--------------------------**\n')

            await client.send_message(message.channel, content = ''.join(final))



    elif message.content.startswith('//vote'):
        msg = message.content.split(' ')
        msg.pop(0)
        try:
            ideanumber = int(msg[0])
            votenumber = int(msg[1])
            vote = msg[2]
        except:
            await client.send_message(message.channel, content = 'You didnt use enough arguments!')
            return

        # if not ("489996858865745932" in [y.id for y in message.author.roles]):
        #     await client.send_message(message.channel, content = 'You dont have the correct permission to vote!')
        #     return

        if not (vote == 'yes' or vote == 'no' or vote == 'maybe' or vote == 'none'):
            await client.send_message(message.channel, content = 'You didnt use a correct voting type! Make sure to do "yes", "no", or "maybe".')
            return

        if vote == 'yes':
            vote = 2
        elif vote == 'maybe':
            vote = 1
        elif vote == 'no':
            vote = 0
        elif vote == 'none':
            vote = 4

        with open('ideas.txt', 'r+') as ideas:

            ideas = ideas.read().split('---')
            votes = ''.join(ideas)
            votes = votes.split('--')
            del votes[::2]

            for x in range(len(list(votes[ideanumber]))):
                for i in list(votes[ideanumber]):
                    if i == '\n':
                        xd = 'xd'
                    else:
                        if i == votenumber:
                            votes[ideanumber][x] = vote

        await client.send_message(message.channel, content = 'Your vote has been added.')



# with open('H:/Misc/token2.txt', 'r') as myfile:
    # token = myfile.read()
client.run('NDk2NTI5NDU2MTc4MDAzOTg3.DpU8iw.nDF1AvaGHN9mATWUws8x5VTK-R8')
