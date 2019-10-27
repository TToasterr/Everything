from random import *
import asyncio as a
from time import *
import discord
import sys
import os

def clear(): return os.system('cls')
sys.path.append("H:/Misc")
client = discord.Client()



game = "off"
gametype = "none"
players = {}
deck = [
"ace of diamonds",
"two of diamonds",
"three of diamonds",
"four of diamonds",
"five of diamonds",
"six of diamonds",
"seven of diamonds",
"eight of diamonds",
"nine of diamonds",
"ten of diamonds",
"jack of diamonds",
"queen of diamonds",
"king of diamonds"
]
tempdeck = [
"ace of diamonds",
"two of diamonds",
"three of diamonds",
"four of diamonds",
"five of diamonds",
"six of diamonds",
"seven of diamonds",
"eight of diamonds",
"nine of diamonds",
"ten of diamonds",
"jack of diamonds",
"queen of diamonds",
"king of diamonds"
]

for card in tempdeck:
    deck.append("%s hearts" % card[:-9])
for card in tempdeck:
    deck.append("%s clubs" % card[:-9])
for card in tempdeck:
    deck.append("%s spades" % card[:-9])




@client.event
async def on_ready():
    clear()
    print("\n" + "Cardbot started!" + "\n")



@client.event
async def on_message(message):
    global game, gametype, players, deck, tempdeck


    if message.author.bot: # if the author is a bot
        return() # ignore it


    private = False
    content = message.content

    if content.startswith("||cb"):
        content = content[2:-2]
        private = True
        await message.delete()

    guild = message.guild
    channel = message.channel
    author = message.author
    args = content.split(" ")






    if content == "cb.help":
        print("[%s] Help sent" % guild.name)
        await channel.send("""\
`cb.help` - This message

`cb.start <public/private>` - Start a game.
`cb.join` - Join the game, if the game is public
`cb.add <player>` - Add a player to the game
`cb.leave` - Leave the game. This puts all your cards on the bottom of the deck
`cb.kick <player>` - Kick a player from the game. This puts all their cards on the bottom of the deck
`cb.close` - If the game is public, stops letting people join
`cb.stop` - Stops the game. All hands go back into the deck

`cb.shuffle` - Shuffle the deck (Does not shuffle cards already in players hands)
`cb.reset` - Reset the deck (Takes all cards from players hands and sorts the deck)
`cb.deal <amount>` - Deal some amount of cards to every player in the game
`cb.draw <amount> [player]` - Draw some amount of cards from the deck and put them in your hand (by default) or someone elses hand
`cb.take <amount> <player> [hand/deck]` - Take some amount of cards from another player and put them in your hand (by default) or the deck
`cb.hand` - Look at your hand
`cb.play <card>` - Play a card from your hand
""")



    elif "credit" in content or "number" in content or "give" in content:
        await channel.send("give me your credit card number")

    elif content.startswith("cb.start"): # if the message starts with cb.start
        if 1 < len(args): # if theres at least one argument
            gametype = args[1] # set the gametype to the argument
            game = "on" # set the game to on
            players[author.name] = [] # add the player to the 'players' dict and make their hand empty ([])
            await channel.send("%s game has been started!" % args[1].title()) # send the message
        else: # else (theres no arguments)
            await channel.send("You must specify either a public or private game!") # tell em they did somin wrong

    elif content == "cb.join": # if the message is cb.join
        if game == "on": # if the game is on
            if gametype == "public": # if the game is public
                players[author.name] = [] # add the player to the players dict and make their hand empty
                await channel.send("%s has joined the game!" % author.name) # send a success message
            else: # else (game is private)
                await channel.send("The game is private! Someone who is already in the game must use cb.addplayer to add you!") # tell em
        else: # else (game is off)
            await channel.send("There is no game currently going on! Use cb.start to start one!") # tell em

    elif content.startswith("cb.add"): # if the message starts with cb.add
        if game == "on": # if the game is on
            if 1 < len(args): # if theres at least 1 argument
                if 0 < len(message.mentions): # if theres at least 1 mention
                    person = message.mentions[0] # get the user mentioned
                    players[person.name] = [] # add the mentioned user to the players dict
                    await channel.send("%s has been added to the game!" % person.name) # tell em
                else: # else (nobody got mentioned)
                    await channel.send("You must mention the person you want to add!") # tell em
            else: # else (there arent any arguments)
                await channel.send("Please specify a player to add to the game!") # tell em
        else: # else (the game isnt on)
            await channel.send("There is no game currently going on! Use cb.start to start one!") # tell em

    elif content == "cb.leave":
        if game == "on":
            if author.name in players:
                if players[author.name] != []:
                    for card in players[author.name]:
                        deck.append(card)
                del players[author.name]
                await channel.send("You have succesfully left the game!")
            else:
                await channel.send("You are not in the ongoing game!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")

    elif content.startswith("cb.kick"):
        if game == "on":
            if 1 < len(args):
                if 0 < len(message.mentions):
                    person = message.mentions[0]
                    if players[person.name] != []:
                        for card in players[person.name]:
                            deck.append(card)
                    del players[person.name]
                    await channel.send("%s has been kicked from the game!" % player.name)
                else:
                    await channel.send("You must mention the person you want to kick!")
            else:
                await channel.send("Please specify a player to kick!")
        else:
            await channel.send("There is no game currently going on! use cb.start to start one!")

    elif content == "cb.close":
        if game == "on":
            if gametype == "public":
                gametype = "private"
                await channel.send("The game has been closed to further players!")
            else:
                await channel.send("The game is already private!")
        else:
            await channel.send("There is no game currently going on! use cb.start to start one!")

    elif content == "cb.stop":
        if game == "on":
            game = "off"
            gametype = "none"
            players = {}
            await channel.send("The game has been turned off!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")



    elif content == "cb.shuffle":
        print("[%s] Deck shuffled" % guild.name)
        shuffle(deck)
        await channel.send("The deck has been shuffled!")

    elif content == "cb.reset":
        players = {}
        game = "off"
        gametype = "none"
        deck = [
        "ace of diamonds",
        "two of diamonds",
        "three of diamonds",
        "four of diamonds",
        "five of diamonds",
        "six of diamonds",
        "seven of diamonds",
        "eight of diamonds",
        "nine of diamonds",
        "ten of diamonds",
        "jack of diamonds",
        "queen of diamonds",
        "king of diamonds"
        ]
        for card in tempdeck:
            deck.append("%s hearts" % card[:-9])
        for card in tempdeck:
            deck.append("%s clubs" % card[:-9])
        for card in tempdeck:
            deck.append("%s spades" % card[:-9])
        await channel.send("All players hands have been cleared and the deck has been sorted!")

    elif content.startswith("cb.deal"):
        if game == "on":
            if 1 < len(args):
                for i in range(int(args[1])):
                    for player in players:
                        players[player].append(deck[0])
                        del deck[0]
                await channel.send("All players have been given %s cards!" % args[1])
            else:
                await channel.send("Please specify an amount of cards to deal to each player!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")

    elif content.startswith("cb.draw"):
        if game == "on":
            if 2 < len(args):
                if 0 < len(message.mentions):
                    person = message.mentions[0]
                    for i in range(int(args[1])):
                        players[person.name].append(deck[0])
                        del deck[0]
                    await channel.send("%s has been given %s cards!" % (person.name, args[1]))
                else:
                    await channel.send("You must mention the person you want to draw cards!")
            elif 1 < len(args):
                for i in range(int(args[1])):
                    players[author.name].append(deck[0])
                    del deck[0]
                await channel.send("%s has drawn %s cards!" % (author.name, args[1]))
            else:
                await channel.send("Please specify an amount of cards to draw!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")

    elif content.startswith("cb.take"):
        if game == "on":
            if 3 < len(args):
                if 0 < len(message.mentions):
                    person = message.mentions[0]
                    if int(args[1]) < len(players[person.name]):
                        if args[3] not in ["hand", "deck"]:
                            await channel.send("Please use either 'hand' or 'deck' as the third argument!")
                            return()
                        for i in range(int(args[1])):
                            ch = choice(players[person.name])
                            if args[3] == "hand":
                                players[author.name].append(ch)
                            else:
                                deck.append(ch)
                            players[person.name].remove(ch)
                        await channel.send("%s took %s card(s) from %s!" % (author.name, args[1], person.name))
                    else:
                        await channel.send("That person doesnt have that many cards!")
                else:
                    await channel.send("You must mention the person you want to take from!")
            elif 2 < len(args):
                if 0 < len(message.mentions):
                    person = message.mentions[0]
                    if int(args[1]) < len(players[person.name]):
                        for i in range(int(args[1])):
                            ch = choice(players[person.name])
                            players[author.name].append(ch)
                            players[person.name].remove(ch)
                        await channel.send("%s took %s card(s) from %s!" % (author.name, args[1], person.name))
                    else:
                        await channel.send("That person doesnt have that many cards!")
                else:
                    await channel.send("You must mention the person you want to take from!")
            else:
                await channel.send("Please make sure to specify and amount of cards, and the player to take from!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")

    elif content.startswith("cb.hand"):
        if game == "on":
            await channel.send("%s's hand:\n||" % author.name + "\n".join(players[author.name]) + "||")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")

    elif content.startswith("cb.play"):
        if game == "on":
            if 1 < len(args):
                if args[1] in players[author.name]:
                    deck.insert(0, args[1])
                    players[author.name].remove(args[1])
                    if private:
                        await channel.send("%s played a card!" % (author.name, args[1]))
                    else:
                        await channel.send("%s played a %s!" % (author.name, args[1]))
                else:
                    await channel.send("You dont have that card!")
            else:
                await channel.send("Please specify a card to play!")
        else:
            await channel.send("There is no game currently going on! Use cb.start to start one!")



    elif content == "cb.showdeck":
        print("[%s] Deck sent" % guild.name)
        await channel.send("\n".join(deck))

    elif content.startswith("cb.debug"):
        print("[%s] Send debug" % guild.name)
        await channel.send("""\
`message.author`: %s
`message.author.name`: %s
`message.guild`: %s
`message.channel`: %s
`message.content`: %s

`game`: %s
`gametype`: %s
`players`: %s
""" % (message.author, message.author.name, message.guild, message.channel, str(message.content), game, gametype, players))



with open('H:/Misc/cardtoken.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)