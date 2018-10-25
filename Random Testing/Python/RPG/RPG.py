from random import randint as ri
from random import choice as ch
import allitems



def newline():
    print("")
def newlines(amount):
    print(""*amount)
def bigboi():
    for i in range(100):
        print("")


class Player:
    def __init__(self, name, equipped, inv, questing, quest, x, y):
        self.name = name
        self.equipped = equipped
        self.inv = inv
        self.questing = questing
        self.quest = quest
        self.x = x
        self.y = y

    def printEquipped(self):
        try:
            print("Main: %s" % self.equipped["main"].name)
        except:
            print("Main: ")
        try:
            print("Side: %s" % self.equipped["side"].name)
        except:
            print("Side: ")
        try:
            print("Armor: %s" % self.equipped["armor"].name)
        except:
            print("Armor: ")

    def printBasics(self):
        print("Name: %s" % self.name)
        newline()
        try:
            print("Main: %s" % self.equipped["main"].name)
        except:
            print("Main: ")
        try:
            print("Side: %s" % self.equipped["side"].name)
        except:
            print("Side: ")
        try:
            print("Armor: %s" % self.equipped["armor"].name)
        except:
            print("Armor: ")

        if self.questing:
            newline()
            print("Quest: %s" % self.quest["goal"])
            print("Quest Item: %s" % self.quest["item"])

        newline()

    def printInv(self):
        print("Inventory: ")
        for item in self.inv:
            item.printName()
        newline()


equipped = {
    "main":allitems.rusty_sword,
    "side":"",
    "armor":allitems.rusty_chestplate
}
inv = [allitems.minor_heal_pot]
quest = {
    "goal":"",
    "item":""
}
bigboi()
name = input("What would you like your players name to be?\n")
player = Player(name, equipped, inv, False, quest, 0, 0)


bigboi()
#Main Loop
while True:
    #get input
    selection = input ("what would you like to do? \n('help' for help) \n")
    #call funcs with input
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
        which = input("Which item would you like to inspect?\n")
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
        newline()

    elif selection == "give":
        found = 0
        corno = input("Do you want to make a custom item?\n")
        bigboi()
        if corno == "yes":
            name = input("Whats the item name?\n")
            newline()
            power = input("Whats the item power?\n")
            newline()
            type = input("Whats the item type?\n")
            newline()
            rarity = input("Whats the item rarity?\n")
            newline()
            bufftype = input("Whats the item bufftype?\n")
            newline()
            buffammount = input("Whats the buff amount?\n")
            bigboi()
            item = allitems.Item(name, power, type, rarity, bufftype, buffammount)
            player.inv.append(item)
        else:
            item = input("Enter the ID of the item:\n")
            if item in allitems.item_name_array:
                for i in range(len(allitems.item_name_array) - 1):
                    if found == 1:
                        do = 'nothing'
                    elif item == allitems.item_name_array[i]:
                        item = allitems.item_array[i]
                        player.inv.append(item)
                        found = 1
                bigboi()
                print("Added item to your inventory.")
                newline()
            else:
                print("That item doesnt exist.")
                newline()
    else:

        print("That's not a command!")
        newline()
