from newlines import *

class Player:
    def __init__(self, name, equipped, inv, health, questing, quest, x, y):
        self.name = name
        self.equipped = equipped
        self.inv = inv
        self.health = health
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
        print("Health: %s" % self.health)
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

    def printInv(self):
        print("Inventory: ")
        for item in self.inv:
            item.printName()
