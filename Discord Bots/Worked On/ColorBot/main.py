import discord
import sys
import pandas as pd
from PIL import Image
import numpy as np
from time import *
import psutil

sys.path.append("H:/Misc")
client = discord.Client()


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



	msg = message.content



	if msg == "help pls":
		await message.channel.send("""**color pls** - get one color to rate
**palette pls** - get two colors to rate how well they go together
**[number] colors pls** - get any amount of colors, 1-9, and rate how well they go together""")
		print("Help sent!")
	elif msg == "color pls":
		color = list(np.random.choice(range(256), size=3))
		w, h = 100, 100
		img = Image.new('RGB', (w, h), color=(color[0], color[1], color[2]))
		img.save('images/color.png')
		msgg = await message.channel.send(color, file=discord.File("images/color.png"))
		await msgg.add_reaction("😍")
		await msgg.add_reaction("😁")
		await msgg.add_reaction("🙂")
		await msgg.add_reaction("😕")
		await msgg.add_reaction("😟")
		await msgg.add_reaction("🤢")
		print("Color sent!")

	elif msg == "palette pls":
		color1 = list(np.random.choice(range(256), size=3))
		color2 = list(np.random.choice(range(256), size=3))
		w, h = 100, 100
		img1 = Image.new('RGB', (w, h), color=(color1[0], color1[1], color1[2]))
		img1.save('images/color1.png')
		img2 = Image.new('RGB', (w, h), color=(color2[0], color2[1], color2[2]))
		img2.save('images/color2.png')
		files = [
			discord.File("images/color1.png"),
			discord.File("images/color2.png")
		]
		msgg = await message.channel.send(str(color1) + ",\n" + str(color2), files=files)
		await msgg.add_reaction("😍")
		await msgg.add_reaction("😁")
		await msgg.add_reaction("🙂")
		await msgg.add_reaction("😕")
		await msgg.add_reaction("😟")
		await msgg.add_reaction("🤢")
		print("Colors to compare sent!")

	elif msg[2:] == "colors pls":
		files = []
		for i in range(int(msg[0])):
			color = list(np.random.choice(range(256), size=3))
			w, h = 50, 50
			img = Image.new('RGB', (w, h), color=(color[0], color[1], color[2]))
			img.save('images/color%s.png' % i)
			files.append(discord.File("images/color%s.png" % i))

		msgg = await message.channel.send(files=files)
		await msgg.add_reaction("😍")
		await msgg.add_reaction("😁")
		await msgg.add_reaction("🙂")
		await msgg.add_reaction("😕")
		await msgg.add_reaction("😟")
		await msgg.add_reaction("🤢")
		print("%s colors sent!" % msg[0])



with open('H:/Misc/colortoken.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
