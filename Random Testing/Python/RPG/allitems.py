weapons = ["Melee","Ranged","Magic"]

class Item:
    def __init__(self, name, power, type, rarity, bufftype, buffammount):
        self.name = name
        self.power = power
        self.type = type
        self.rarity = rarity
        self.bufftype = bufftype
        self.buffammount = buffammount

    def printName(self):
        print(self.name)

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

        if self.bufftype != "None":
            print("+%s to %s" % (self.buffammount, self.bufftype))


minor_heal_pot = Item("Minor Healing Potion", 10, "Potion", "Very Common", "None", 0)
lesser_heal_pot = Item("Lesser Healing Potion", 20, "Potion", "Common", "None", 0)
heal_pot = Item("Healing Potion", 50, "Potion", "Uncommon", "None", 0)
greater_heal_pot = Item("Greater Healing Potion", 100, "Potion", "Rare", "None", 0)
massive_heal_pot = Item("Massive Healing Potion", 200, "Potion", "Legendary", "None", 0)

rusty_sword = Item("Rusty Sword", 2, "Melee", "Starter", "None", 0)
rusty_armor = Item("Rusty Armor", 3, "Armor", "Starter", "None", 0)

dagger = Item("Dagger", 4, "Melee", "Very Common", "None", 0)
leather_armor = Item("Leather Armor", 4, "Armor", "Very Common", "None", 0)

shortbow = Item("Short Bow", 3, "Ranged", "Common", "None", 0)
shortsword = Item("Shortsword", 5, "Melee", "Common", "None", 0)

item_array = [
    minor_heal_pot,
    lesser_heal_pot,
    heal_pot,
    greater_heal_pot,
    massive_heal_pot,
    rusty_sword,
    rusty_armor,
    dagger,
    leather_armor,
    shortbow,
    shortsword
]
item_name_array = [
    "minor_heal_pot",
    "lesser_heal_pot",
    "heal_pot",
    "greater_heal_pot",
    "massive_heal_pot",
    "rusty_sword",
    "rusty_armor",
    "dagger",
    "leather_armor",
    "shortbow",
    "shortsword"
]
