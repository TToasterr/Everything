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
hpUpItem = "▲"
attUpItem = "●"
key = "%s: wall \n%s: floor \n%s: player \n%s: monster \n%s: health up \n%s: attack up \n" % (wall,floor,player,monster,hpUpItem,attUpItem)
types = ["Gremlin","Orc","Skeleton","Toaster","Zombie","Crazed Miner"]
healthMax = [200, 250, 300, 350, 400, 450]
attMax = [200, 250, 300, 400, 600, 900]
attUp = 0
hpUpp = 0
enHpMax = [500, 600, 750]
enAttMax = [75, 100, 150]
health = healthMax[hpUpp]



#----------------------------------------------------------------------------------------------------------



def printBoard():
    global boards
    global key
    global stats
    print(key)
    print(stats)
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
        powerUpf()
        if tile == 1:
            playerPos = [7,5]
        if tile == 2:
            playerPos = [2,4]



def powerUpf():
    global hpUpItem
    global attUpItem
    global wall
    global coordsX
    global coordsY
    global powerUp
    global powerUpType

    powerUp = random.randint(0,1)
    if powerUp == 0:
        powerUp = False
        print("You don't get a power up! \n")
    else:
        print("You got a power up! \n")
        powerUpType = random.randint(0,1)
        if powerUpType == 0:
            powerUpType = hpUpItem
        else:
            powerUpType = attUpItem
        powerUpPlace()

def powerUpPlace():
    global powerUp
    global coordsX
    global coordsY
    global powerUpType
    global boards

    if powerUp:
        powerUpCoords()
        if boards[tile][coordsX][coordsY] == wall or boards[tile][coordsX][coordsY] == monster or boards[tile][coordsX][coordsY] == player:
            powerUpPlace()

        else:
            boards[tile][coordsX][coordsY] = powerUpType



def powerUpCoords():
    global coordsX
    global coordsY
    coordsX = random.randint(0,9)
    coordsY = random.randint(0,9)



def attackUp():
    global attMax
    global attUp
    attUp += 1



def hpUp():
    global healthMax
    global hpUpp
    hpUpp += 1



#----------------------------------------------------------------------------------------------------------



def fightInput():
    global finp
    finp = input("Please input a command. \n")



def getStats():
    global enType
    global enHealth
    global enHpMax
    global tile

    enType = random.randint(0,len(types)-1)
    enType = types[enType]
    enHealth = random.randint(50,enHpMax[tile])



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
    global healthMax
    global hpUpp

    if health <= 0:
        print(a)
        print("Oof, you died.")
        sys.exit()

    if enHealth <= 0:
        health = healthMax[hpUpp]
        monsterCount[tile] -= 1
        print(a)
        print("You killed the monster, and were healed to full health. \n")
        yoinks()



def fight():
    global finp
    global a
    global health
    global enHealth
    global AttMax
    global enAttMax
    global tile
    global attUp
    global hpUpp

    printFight()
    checkHealths()
    fightInput()

    if finp == "help":
        print(a)
        print("Input 'attack' or 'heal' to attack or heal. \n")
        fight()

    if finp == "attack" or finp == "a":
        dmgd = random.randint(1,attMax[attUp])
        enHealth -= dmgd
        dmgt = random.randint(1,enAttMax[attUp])
        health -= dmgt
        print(a)
        print("You dealt %s damage. \n\nThe monster hit back, and dealt %s damage. \n" % (dmgd, dmgt))
        fight()

    if finp == "heal" or finp == "h":
        dmgt = random.randint(1,enAttMax[attUp])
        health -= dmgt
        healAmm = random.randint(0,100)
        health += healAmm

        if health >= healthMax[hpUpp]:
            health = healthMax[hpUpp]
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
    global hpUpItem
    global attUpItem
    global stats

    stats = "HEALTH MAX: %s \nATTACK MAX: %s" % (healthMax[hpUpp],attMax[attUp])
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

        elif boards[tile][playerPos[0]-1][playerPos[1]] == hpUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an HP up! \n")
            hpUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]-1][playerPos[1]] == attUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an ATTACK up! \n")
            attackUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]-1][playerPos[1]] == monster:
            health = healthMax[hpUpp]
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

        elif boards[tile][playerPos[0]+1][playerPos[1]] == hpUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an HP up! \n")
            hpUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]+1][playerPos[1]] == attUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[0] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an ATTACK up! \n")
            attackUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]+1][playerPos[1]] == monster:
            health = healthMax[hpUpp]
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

        elif boards[tile][playerPos[0]][playerPos[1]-1] == hpUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an HP up! \n")
            hpUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]-1] == attUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] -= 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an ATTACK up! \n")
            attackUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]-1] == monster:
            health = healthMax[hpUpp]
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

        elif boards[tile][playerPos[0]][playerPos[1]+1] == hpUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an HP up! \n")
            hpUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]+1] == attUpItem:
            boards[tile][playerPos[0]][playerPos[1]] = floor
            playerPos[1] += 1
            boards[tile][playerPos[0]][playerPos[1]] = player
            print(a)
            print("You got an ATTACK up! \n")
            attackUp()
            yoinks()
            return

        elif boards[tile][playerPos[0]][playerPos[1]+1] == monster:
            health = healthMax[hpUpp]
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
powerUpf()
yoinks()
