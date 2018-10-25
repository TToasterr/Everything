class Item:
    def __init__(self, name, power, type, rarity, bufftype, buffamount):
        self.name = name
        self.power = power
        self.type = type
        self.rarity = rarity
        self.bufftype = bufftype
        self.buffammount = buffamount

    def printItem(self):
        print(self.name)
        print(self.type)

        if self.type in weapons:
            print("%s damage" % self.power)
        elif self.type == "armor":
            print("%s defense" % self.power)
        else:
            print("%s health regen" % self.power)

        print(self.rarity)

        if bufftype != "None":
            print("%s")


minor_heal_pot = Item("Minor Healing Potion", 5, "Potion", "Very Common", "None", 0)

rusty_sword = Item("Rusty Sword", 2, "Melee", "Starter", "None", 0)
rusty_chestplate = Item("Rusty Chestplate", 3, "Armor", "Starter", "None", 0)
