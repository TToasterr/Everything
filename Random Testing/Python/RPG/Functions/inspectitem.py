from newlines import *

def inspectItem():
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
