import random
import sys

a = "\n"*50
boards = [
    [
        ["█","█","█","█","█","█","█","█","█","█"],
        ["█","█","█","░","░","░","█","█","█","█"],
        ["█","█","░","░","░","░","█","□","█","█"],
        ["█","░","░","░","░","░","░","░","█","█"],
        ["█","░","░","░","░","░","█","█","█","█"],
        ["█","░","░","█","█","░","█","░","□","█"],
        ["█","░","█","█","░","░","█","░","░","█"],
        ["█","░","█","□","░","░","░","░","█","█"],
        ["█","□","█","█","░","░","░","░","█","█"],
        ["█","█","█","█","█","█","█","█","█","█"]
    ],
    [
        ["█","█","█","█","█","█","█","█","█","█"],
        ["█","□","█","█","░","░","░","█","█","█"],
        ["█","░","█","░","░","░","░","░","█","█"],
        ["█","░","█","░","□","█","█","░","█","█"],
        ["█","░","█","░","█","█","█","░","█","█"],
        ["█","░","░","░","░","░","░","░","□","█"],
        ["█","█","█","░","░","░","░","░","░","█"],
        ["█","█","█","░","░","░","░","░","░","█"],
        ["█","□","░","░","░","░","░","█","█","█"],
        ["█","█","█","█","█","█","█","█","█","█"]
    ],
      [
          ["█","█","█","█","█","█","█","█","█","█"],
          ["█","█","█","░","░","░","░","█","█","█"],
          ["█","█","░","░","░","░","░","░","█","█"],
          ["█","█","█","░","░","█","█","░","░","█"],
          ["█","█","□","░","░","█","□","░","░","█"],
          ["█","█","█","█","░","░","░","░","█","█"],
          ["█","█","█","█","█","░","░","░","█","█"],
          ["█","█","█","░","░","░","█","█","█","█"],
          ["█","□","░","░","░","█","█","█","█","█"],
          ["█","█","█","█","█","█","█","█","█","█"]
      ]
]
monsterCount = [4,4,3]
tile = 0
playerPos = [2,4]
boards[tile][playerPos[0]][playerPos[1]] = "■"
wall = "█"
floor = "░"
player = "■"
monster = "□"
types = ["Gremlin","Orc","Skeleton","Toaster"]
health = 200



#----------------------------------------------------------------------------------------------------------



def printBoard():
    global boards
    for i in boards[tile]:
        print(*i, sep="  ")



def getInp():
    global inp
    inp = input("Please input a command. \n")



def checkMCount():
    global monsterCount
    global tile
    global playerPos

    if monsterCount[tile] == 0:
        tile += 1
        if tile == 1:
            playerPos = [7,5]
        if tile == 2:
            playerPos = [2,4]



#----------------------------------------------------------------------------------------------------------



def fightInput():
    global finp
    finp = input("Please input a command. \n")



def getStats():
    global enType
    global enHealth

    enType = random.randint(0,len(types)-1)
    enType = types[enType]
    enHealth = random.randint(50,500)



def printFight():
    global enType
    global enHealth
    global health

    print("ENEMY TYPE: \n%s \n\nENEMY HEALTH: \n%s \n\n\n\nYOUR HEALTH: \n%s \n" % (enType, enHealth, health))



def checkHealths():
    global health
    global enHealth
    global tile
    global monsterCount

    if health <= 0:
        print(a)
        print("Oof, you died.")
        sys.exit()

    if enHealth <= 0:
        health = 200
        monsterCount[tile] -= 1
        print(a)
        print("You killed the monster, and were healed to full health. \n")
        yoinks()



def fight():
    global finp
    global a
    global health
    global enHealth

    printFight()
    checkHealths()
    fightInput()

    if finp == "help":
        print(a)
        print("Input 'attack' or 'heal' to attack or heal. \n")
        fight()

    if finp == "attack":
        dmgd = random.randint(1,200)
        enHealth -= dmgd
        dmgt = random.randint(1,75)
        health -= dmgt
        print(a)
        print("You dealt %s damage. \n\nThe monster hit back, and dealt %s damage. \n" % (dmgd, dmgt))
        fight()

    if finp == "heal":
        dmgt = random.randint(1,75)
        health -= dmgt
        healAmm = random.randint(0,100)
        health += healAmm

        if health >= 200:
            health = 200
            print(a)
            print("You were already at, or healed to, full health! \n\nThe monster hit you while you were healing, and dealt %s damage. \n" % dmgt)
        else:
            print(a)
            print("You healed for %s health. \n\nThe monster hit you while you were healing, and dealt %s damage. \n" % (healAmm, dmgt))
        fight()

    else:
        print(a)
        print("That isn't a command. \n")
        fight()



#----------------------------------------------------------------------------------------------------------



def yoinks():
    global inp
    global tile
    global floor
    global monster
    global player
    global playerPos
    global boards
    global a
    global health

    checkMCount()
    boards[tile][playerPos[0]][playerPos[1]] = player
    printBoard()
    getInp()

    if inp == "help":
        print(a)
        print("Input 'w', 'a', 's', and 'd' and press enter to move.")
        yoinks()

    if inp == "w":
        if boards[tile][playerPos[0]-1][playerPos[1]] == wall:
            print(a)
            print("You can't walk into a wall.")
            yoinks()
            return

        elif boards[tile][playerPos[0]-1][playerPos[1]] == monster:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            getStats()
            fight()
            return

        else:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            yoinks()
            return

    if inp == "s":
        if boards[tile][playerPos[0]+1][playerPos[1]] == wall:
            print(a)
            print("You can't walk into a wall.")
            yoinks()
            return

        elif boards[tile][playerPos[0]+1][playerPos[1]] == monster:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            getStats()
            fight()
            return

        else:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            yoinks()
            return

    if inp == "a":
        if boards[tile][playerPos[0]][playerPos[1]-1] == wall:
            print(a)
            print("You can't walk into a wall.")
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]-1] == monster:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            getStats()
            fight()
            return

        else:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            yoinks()
            return

    if inp == "d":
        if boards[tile][playerPos[0]][playerPos[1]+1] == wall:
            print(a)
            print("You can't walk into a wall.")
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]+1] == monster:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            getStats()
            fight()
            return

        else:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            yoinks()
            return

    if inp == "heal":
        healAmm = random.randint(0,100)
        health += healAmm

        if health >= 200:
            health = 200
            print(a)
            print("You were already at, or healed to, full health! \n")
            yoinks()
        else:
            print(a)
            print("You healed for %s health. \n\nYOUR HEALTH: \n%s" % (healAmm, health))
            yoinks()

    else:
        print(a)
        print("That isn't a command.")
        yoinks()



#----------------------------------------------------------------------------------------------------------



print(a)
yoinks()
