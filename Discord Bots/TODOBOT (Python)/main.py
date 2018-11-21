from datetime import datetime
from random import randint as ri
from random import choice as ch
import discord
import asyncio
import sys
import threading
sys.path.append("H:/Misc")



def background_time_function():
    global currentTime
    while True:
        currentTime = str(datetime.now().strftime("%H:%M:%S"))

def background_command_refresh():
    global commandList
    while True:
        with open("commands.py", "r") as file:
            commands = file.read()
            exec(commands, globals())

time_function = threading.Thread(target=background_time_function)
time_function.start()
command_refresh = threading.Thread(target=background_command_refresh)
command_refresh.start()



client = discord.Client()



async def background_reminder(name, mesg, time, message):
    await client.wait_until_ready()
    while not client.is_closed:
        if int(datetime.now().strftime("%H%M")) == int(time):
            await client.send_message(message.channel, content = "<@%s>\n**Reminder:** %s\n**Message:** %s" % (message.author.id, name, mesg))
            return()
        await asyncio.sleep(60)

async def background_recurring_reminder(name, mesg, time, message):
    await client.wait_until_ready()
    while not client.is_closed:
        if int(datetime.now().strftime("%H%M")) == int(time):
            await client.send_message(message.channel, content = "**Reminder:** %s\n**Message:** %s" % (name, mesg))
        await asyncio.sleep(60)



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="td.help"))



@client.event
async def on_server_join(server):
    print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message):
    global currentTime
    global msg

    msg = message.content
    # print("[%s] %s: %s\n" % (currentTime, message.author, message.content))

    if msg[:3] != "td.":
        return

    for command in commandList:
        if msg[3:(len(command.name) + 3)] == command.name:
            def do_command():
                global embed
                global messageOut
                global message
                global commandList
                global done
                exec(command.function, globals())

            command_function = threading.Thread(target=do_command)
            command_function.start()

            if embed != "":
                await client.send_message(message.channel, embed = embed)

            if messageOut != "":
                await client.send_message(message.channel, content = messageOut)

            if command.name == "addreminder" and done == 0:
                client.loop.create_task(background_reminder(name, mssg, time, message))

            if command.name == "addrecreminder" and done == 0:
                client.loop.create_task(background_recurring_reminder(name, mssg, time, message))

            print("[%s] %s did the %s command.\n" % (currentTime, message.author, command.name))



with open('H:/Misc/todobot.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
