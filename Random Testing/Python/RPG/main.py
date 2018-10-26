import sys
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Random Testing/Python/RPG/Classes")
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Random Testing/Python/RPG/Functions")

from random import randint as ri
from random import choice as ch
import itemlist
from newlines import *
from playerclass import Player
from inspectitem import inspectItem

#-----------------------------------------------------------------------
#Making the player

equipped = {
    "main":itemlist.rusty_sword,
    "side":"",
    "armor":itemlist.rusty_armor
}
inv = [itemlist.minor_heal_pot]
quest = {
    "goal":"",
    "item":""
}
bigboi()
name = input("What would you like your players name to be? \n")
player = Player(name, equipped, inv, False, quest, 0, 0)

#-----------------------------------------------------------------------
#The main loop

bigboi()
while True:
    selection = input ("What would you like to do? \n")
    bigboi()



    if selection == "stats":
        player.printBasics()
        newline()



    elif selection == "move":
        print("pretend you moved")
        newline()



    elif selection == "toggle minimap":
        print("pretend you toggled your minimap")
        newline()



    elif selection == "look around":
        print("wow the void looks nice today")
        newline()



    elif selection == "inspect item":
        found = 0
        player.printEquipped()
        newline()
        player.printInv()
        newline()
        which = input("Which item would you like to inspect? \n")
        newline()
        for item in player.inv:
            if found == 1:
                do = "nothing"
            elif item.name == which:
                bigboi()
                found = 1
                item.printItem()
                newline()
        for item in player.equipped:
            if found == 1:
                do = "nothing"
            else:
                try:
                    if player.equipped[item].name == which:
                        bigboi()
                        found = 1
                        player.equipped[item].printItem()
                        newline()
                except:
                    do = "nothing"
        if found == 0:
            bigboi()
            print("There isnt an item with that name!")
            newline()



    elif selection == "inventory" or selection == "inv":
        player.printInv()
        newline()



    elif selection == "help":
        print("List of Commands:")
        print("stats")
        print("move")
        print("toggle minimap")
        print("look around")
        print("inspect item")
        print("inventory")
        print("help")
        newlines(2)



    elif selection == "give":
        found = 0
        corno = input("Do you want to make a custom item? \n")
        bigboi()
        if corno == "yes":
            name = input("Whats the item name? \n")
            newline()
            power = input("Whats the item power? \n")
            newline()
            type = input("Whats the item type? \n")
            newline()
            rarity = input("Whats the item rarity? \n")
            newline()
            bufftype = input("Whats the item bufftype? \n")
            newline()
            buffammount = input("Whats the buff amount? \n")
            bigboi()
            item = itemlist.Item(name, power, type, rarity, bufftype, buffammount)
            player.inv.append(item)
        else:
            item = input("Enter the ID of the item:\n")
            if item in itemlist.item_name_array:
                for i in range(len(itemlist.item_name_array) - 1):
                    if found == 1:
                        do = 'nothing'
                    elif item == itemlist.item_name_array[i]:
                        item = itemlist.item_array[i]
                        player.inv.append(item)
                        found = 1
                bigboi()
                print("Added item to your inventory.")
                newline()
            else:
                bigboi()
                print("That item doesnt exist.")
                newline()



    else:
        print("That's not a command!")
        newline()
