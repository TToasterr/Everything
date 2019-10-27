import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from PIL import Image
from random import *
import asyncio as a
import pandas as pd
import numpy as np
from time import *
import threading
import discord
import psutil
import sys

sys.path.append("H:/Misc")
client = discord.Client()



a = np.zeros((256, 256, 256))

a[:,:,:] = False;

nonzeros = [];



async def editSubp(client, msgg, color):
    emojis = [
    "😍",
    "😁",
    "🙂",
    "😕",
    "😟",
    "🤢"
    ]
    time = 20

    for i in range(time):
        msgtext = []
        score = 0
        cache_msg = discord.utils.get(client.cached_messages, id=msgg.id)

        for reaction in cache_msg.reactions:
            msgtext.append("%sx%s" % (reaction.emoji, int(reaction.count) - 1))
            if reaction.emoji == emojis[0]:
                score += 4 * (int(reaction.count) - 1)
            elif reaction.emoji == emojis[1]:
                score += 2 * (int(reaction.count) - 1)
            elif reaction.emoji == emojis[2]:
                score += 1 * (int(reaction.count) - 1)
            elif reaction.emoji == emojis[3]:
                score -= 1 * (int(reaction.count) - 1)
            elif reaction.emoji == emojis[4]:
                score -= 2 * (int(reaction.count) - 1)
            elif reaction.emoji == emojis[5]:
                score -= 4 * (int(reaction.count) - 1)

        time -= 1
        if time == 0:
            await msgg.edit(content=(str(color) + "\n\n**SCORE**: %s" % score))
            a[color[0]][color[1]][color[2]] = score
            nonzeros.append((color[0],color[1],color[2]))
        else:
            await msgg.edit(content=(str(color) + "\n\n**TIME LEFT**: %s\n**SCORE**: %s" % (time, score)))
        await a.sleep(1)


@client.event
async def on_ready():
    # activeServers = client.servers
    # sum = 0
    # for s in activeServers:
    #     sum += len(s.members)
    print("Bot started!\n")
    # await client.change_presence(game=discord.Game(name="Toaster 3.0 | t.help"))



# @client.event
# async def on_server_join(server):
#     print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message):
    if message.author.bot:
        return()



    content = message.content
    channel = message.channel
    author = message.author

    timeBetweenScoring = 5



    if content == "help pls":
        print("Help sent!")
        await channel.send("""**color pls** - get one color to rate
**palette pls** - get six colors to rate how well they go together""")


    elif content == "color pls":
        print("Color sent!")
        color = list(np.random.choice(range(256), size=3))
        w, h = 100, 100
        img = Image.new('RGB', (w, h), color=(color[0], color[1], color[2]))
        img.save('images/color.png')

        msgg = await channel.send(str(color) + "\n\n**SCORE**: 0", file=discord.File("images/color.png"))
        await msgg.add_reaction("😍")
        await msgg.add_reaction("😁")
        await msgg.add_reaction("🙂")
        await msgg.add_reaction("😕")
        await msgg.add_reaction("😟")
        await msgg.add_reaction("🤢")

        await editSubp(client, msgg, color)


    elif content == "palette pls":
        print("Palette sent!")
        files = []
        text = []
        for i in range(6):
            color = list(np.random.choice(range(256), size=3))
            w, h = 50, 50
            img = Image.new('RGB', (w, h), color=(color[0], color[1], color[2]))
            img.save('images/color%s.png' % i)
            files.append(discord.File("images/color%s.png" % i))
            text.append(str(color))

        msgg = await channel.send(",\n".join(text) + "\n\n**SCORE**: 0", files=files)
        await msgg.add_reaction("😍")
        await msgg.add_reaction("😁")
        await msgg.add_reaction("🙂")
        await msgg.add_reaction("😕")
        await msgg.add_reaction("😟")
        await msgg.add_reaction("🤢")

        await editSubp(client, msgg, ",\n".join(text))

    elif content == "rating counts pls":
        print("Graphs sent!")
        files = []

        plt.ion()
        plt.clf()
        plt.xticks(np.arange(-4, 4, 1))
        rHist = plt.hist(rScores, facecolor='red', alpha=0.5)
        plt.savefig("images/redHist.png", bbox_inches="tight")

        plt.clf()
        plt.xticks(np.arange(-4, 4, 1))
        gHist = plt.hist(gScores, facecolor='green', alpha=0.5)
        plt.savefig("images/greenHist.png", bbox_inches="tight")

        plt.clf()
        plt.xticks(np.arange(-4, 4, 1))
        bHist = plt.hist(bScores, facecolor='blue', alpha=0.5)
        plt.savefig("images/blueHist.png", bbox_inches="tight")

        files.append(discord.File("images/redHist.png"))
        files.append(discord.File("images/greenHist.png"))
        files.append(discord.File("images/blueHist.png"))

        msgg = await channel.send(files = files)





with open('H:/Misc/colortoken.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
