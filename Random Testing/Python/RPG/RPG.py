from random import randint as ri
from random import choice as ch
import allitems


weapons = ["Melee","Ranged","Magic"]


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

    def printBasics(self):
        print("Name: %s" % self.name)
        newline()
        print("Main: %s" % self.equipped["main"])
        print("Side: %s" % self.equipped["side"])
        print("Armor: %s" % self.equipped["armor"])

        if self.questing:
            newline()
            print("Quest: %s" % self.quest["goal"])
            print("Quest Item: %s" % self.quest["item"])

        newline()

    def printInv(self):
        print("Inventory: ")
        for item in self.inv:
            item.printItem()
        newline()


equipped = {
    "main":allitems.rusty_sword,
    "side":"",
    "armor":allitems.rusty_chestplate
}
inv = [allitems.minor_heal_pot]
quest = {
    "goal":"be gay",
    "item":"the gay totem"
}
player = Player(input("What would you like your players name to be?\n"), equipped, inv, True, quest, 0, 0)


bigboi()
#Main Loop
while True:
    #get input
    selection = input ("what would you like to do? \n('help' for help) \n")
    #call funcs with input
    bigboi()
    if selection == "move":
        print("pretend you moved")
        newline()
    elif selection == "toggle minimap":
        print("pretend you toggled your minimap")
        newline()
    elif selection == "look around":
        print("wow the void looks nice today")
        newline()
    elif selection == "inventory":
        player.printInv()
        newline()
    elif selection == "help":
        print("List of Commands:")
        print("move")
        print("toggle minimap")
        print("look around")
        print("inventory")
        print("help")
        newline()
    else:
        print("That's not a command!")
        newline()
