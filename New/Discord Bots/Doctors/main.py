from random import *
import asyncio as a
import discord
import sys
import os

def clear(): return os.system('cls')
sys.path.append("H:/Misc")
client = discord.Client()

@client.event
async def on_ready():
    clear()

@client.event
async def on_message(message):
    content = message.content
    guild = message.guild
    channel = message.channel
    author = message.author
    args = content.split(" ")

    if "doctor" in content:
        responses = ["i diagnose you with dead", "bro you been eaten apples", "bro your like 2 foot 4 how do you even get that short"]
        await channel.send(choice(responses))

    elif "sick" in content:
        responses = ["well maybe if you visted me then you wouldnt be dying", "youve probably been visting those other 4/5 you bumbling moron", "ill have you know i graduated top of my class in dental school"]
        await channel.send(choice(responses))

    elif content.startswith("\\choose"):
        await channel.send(choice(args[1:]))

with open('H:/Misc/doctorToken.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)