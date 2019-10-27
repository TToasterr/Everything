from random import * # Just importing everything
import asyncio as a
from time import *
import discord
import sys
import os

# -----------------------------------------------------------------------------

def clear(): return os.system('cls') # Making it so you can do clear() to clear the console
sys.path.append("H:/Misc") # Add the folder where the token will be to the path
client = discord.Client() # Make a new discord client

# -----------------------------------------------------------------------------

@client.event
async def on_ready(): # When the bot loads up
    clear() # Clear the console
    print("\nThe infant detonator has arrived\n") # Welcome message

# -----------------------------------------------------------------------------

@client.event
async def on_message(message): # When the bot recieved a message
    if message.author.bot: # If the message is from a bot
        return() # Ignore it

    authorUsername = message.author.name # Putting all the message variables into easier variables
    channelname = message.channel.name
    channel = message.channel
    content = message.content.lower()
    author = message.author

    num = randint(0, 2) # Generate a random number, 0 1 2

    # This next part is just a condensed version of the NEXT next part, checking whether it should print stuff in console
    if content == "ok boomer" or "boomer" in content or content.split(" ")[0] in ["i", "im", "i'm", "lets", "let's"]:
        print("A BOOMER MOMENT HAS OCCURED - %s (%s)" % (num, num==1))
    for i in [" i ", "i'm", "lets", "let's", "should"]:
        if i in content:
            print("A BOOMER MOMENT HAS OCCURED - %s (%s)" % (num, num==1))


    # Basically, 1/3 of the time, if you said some trigger, the bot will respond
    if num == 1: # If the random number is 1
        if content == "ok boomer": # If the message is only "ok boomer"
            await channel.send("thats my line, ___***boomer***___") # Respond
        elif "boomer" in content: # If the word "boomer" is in the message
            await channel.send("shut up boomer") # Respond
        elif content.split(" ")[0] in ["i", "im", "i'm", "lets", "let's"]: # If the first word of the message is i, im, or lets
            await channel.send("ok boomer") # Respond
        else: # Else (none of those are in the message)
            # Basically, if " i ", "i'm", "lets", "let's", or "should" is anywhere in the message, respond
            for i in [" i ", "i'm", "lets", "let's", "should"]: # For each item in an array of words
                if i in content: # If the message has the word in it
                    await channel.send("ok boomer") # Respond
                    return() # Dont respond again

# -----------------------------------------------------------------------------

with open("H:/Misc/boomertoken.txt", "r") as f: # Open the file the token is stored in
    token = f.read() # Read the file to a variable
client.run(token) # Run the bot, with the token