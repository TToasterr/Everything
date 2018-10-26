import sys
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Random Testing/Python/RPG/Classes")
sys.path.append("C:/Users/matth/Documents/GitHub/Everything/Random Testing/Python/RPG/Functions")

from random import randint as ri
from random import choice as ch
import itemlist
from newlines import *
from playerclass import Player
import inspectitem
from inspectitem import inspectItem
from giveitem import giveItem
from equipping import equipItem
from printmap import printMap

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
player = Player(name, equipped, inv, 10, False, quest, 0, 0)

#-----------------------------------------------------------------------
#The main loop

bigboi()
while True:
    selection = input ("What would you like to do? \n")
    bigboi()



    if selection == "stats":
        player.printBasics()
        newline()



    elif selection == "help":
        print("List of Commands:")
        print("stats")
        print("inv")
        print("equip")
        print("inspect item")
        print("move")
        print("toggle minimap")
        print("look around")
        newlines(2)



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
        inspectItem(player)



    elif selection == "inventory" or selection == "inv":
        player.printInv()
        newline()



    elif selection == "give":
        giveItem(player)



    elif selection == "equip":
        equipItem(player)
    
    
    
    else:
        print("That's not a command!")
        newline()
