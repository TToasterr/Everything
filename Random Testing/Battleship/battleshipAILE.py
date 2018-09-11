import random, time

moveDown = "\n"*22
lineBreak = "\n"

boardSize = 10

gameBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
alphabet = ["A","B","C","D","E","F","G","H","I","J"]

Five = 1
Four = 1
Three = 2
Two = 1

shipsPlaced = 0

hits = 0

def convertToNum():
    if b[0] == "a" or b[0] == "A":
        b[0] = 0
    if b[0] == "b" or b[0] == "B":
        b[0] = 1
    if b[0] == "c" or b[0] == "C":
        b[0] = 2
    if b[0] == "d" or b[0] == "D":
        b[0] = 3
    if b[0] == "e" or b[0] == "E":
        b[0] = 4
    if b[0] == "f" or b[0] == "F":
        b[0] = 5
    if b[0] == "g" or b[0] == "G":
        b[0] = 6
    if b[0] == "h" or b[0] == "H":
        b[0] = 7
    if b[0] == "i" or b[0] == "I":
        b[0] = 8
    if b[0] == "j" or b[0] == "J":
        b[0] = 9

def printBoard():
    print(moveDown)
    print(" ", *alphabet, sep="  ")
    print("  ", "-  " * 10)
    for i in range(boardSize):
        print(i, *gameBoard[i], sep="  ")

def cantPlace():
    d = input("\n\nYou can't place that ship there! Not enough space. \nPress enter to continue. \n")
    if d == "":
        placeShip()

def outOf():
    d = input("\n\nYou don't have any more of that ship! \nPress enter to continue. \n")
    if d == "":
        placeShip()

def placeShip():
    global a
    global b
    global c
    global Five
    global Four
    global Three
    global Two
    global lineBreak
    global shipsPlaced

    if shipsPlaced == 5:
        AI()
        return

    printBoard()
    a = input("\n\nWhat ship would you like to place? \n'listShips' to see what you have. \nFormat like '3'\n")

    if a == "listShips":
        print("\nYou have:", lineBreak, Five, "five long(s)", lineBreak, Four, "four long(s)", lineBreak, Three, "three long(s)", lineBreak, Two, "two long(s)\n\nPress enter to continue.")
        xddd = input()
        if xddd == "":
            placeShip()

    if a == "skip":
        global gameBoard
        gameBoard = [
            [1,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,1,0],
            [0,0,0,0,1,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        AI()
        return

    b = input("\n\nWhere would you like to place it? \nFormat like 'A,0'\n").split(",")

    c = input("\n\nWhat direction would you like it to go? \nFormat like 'left'\n")

    convertToNum()

    # if c == "test":
    #     print(a,b,c)
    #     return

    playerX = int(b[0])
    playerY = int(b[1])

    if a == "5":
        if Five == 0:
            outOf()

        if c == "left":
            if int(b[0]) <= 3:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Five = 0
                while i <= 4:
                    gameBoard[playerY][int(playerX) - i] = 1
                    i += 1
                placeShip()
        if c == "right":
            if int(b[0]) > 6:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Five = 0
                while i <= 4:
                    gameBoard[playerY][int(playerX) + i] = 1
                    i += 1
                placeShip()
        if c == "up":
            if int(b[1]) <= 3:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Five = 0
                while i <= 4:
                    gameBoard[playerY - i][playerX] = 1
                    i += 1
                placeShip()
        if c == "down":
            if int(b[1]) > 5:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Five = 0
                while i <= 4:
                    gameBoard[playerY + i][playerX] = 1
                    i += 1
                placeShip()

    elif a == "4":
        if Four == 0:
            outOf()

        if c == "left":
            if int(b[0]) <= 2:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Four = 0
                while i <= 3:
                    gameBoard[playerY][int(playerX) - i] = 1
                    i += 1
                placeShip()
        if c == "right":
            if int(b[0]) > 7:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Four = 0
                while i <= 3:
                    gameBoard[playerY][int(playerX) + i] = 1
                    i += 1
                placeShip()
        if c == "up":
            if int(b[1]) <= 2:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Four = 0
                while i <= 3:
                    gameBoard[playerY - i][playerX] = 1
                    i += 1
                placeShip()
        if c == "down":
            if int(b[1]) > 6:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Four = 0
                while i <= 3:
                    gameBoard[playerY + i][playerX] = 1
                    i += 1
                placeShip()

    elif a == "3":
        if Three == 0:
            outOf()

        if c == "left":
            if int(b[0]) <= 1:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Three -= 1
                while i <= 2:
                    gameBoard[playerY][int(playerX) - i] = 1
                    i += 1
                placeShip()
        if c == "right":
            if int(b[0]) > 8:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Three -= 1
                while i <= 2:
                    gameBoard[playerY][int(playerX) + i] = 1
                    i += 1
                placeShip()
        if c == "up":
            if int(b[1]) <= 1:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Three -= 1
                while i <= 2:
                    gameBoard[playerY - i][playerX] = 1
                    i += 1
                placeShip()
        if c == "down":
            if int(b[1]) > 7:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Three -= 1
                while i <= 2:
                    gameBoard[playerY + i][playerX] = 1
                    i += 1
                placeShip()

    elif a == "2":
        if Two == 0:
            outOf()

        if c == "left":
            if int(b[0]) == 0:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Two = 0
                while i <= 1:
                    gameBoard[playerY][int(playerX) - i] = 1
                    i += 1
                placeShip()
        if c == "right":
            if int(b[0]) == 9:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Two = 0
                while i <= 1:
                    gameBoard[playerY][int(playerX) + i] = 1
                    i += 1
                placeShip()
        if c == "up":
            if int(b[1]) <= 0:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Two = 0
                while i <= 1:
                    gameBoard[playerY - i][playerX] = 1
                    i += 1
                placeShip()
        if c == "down":
            if int(b[1]) > 8:
                cantPlace()
            else:
                i = 0
                shipsPlaced += 1
                Two = 0
                while i <= 1:
                    gameBoard[playerY + i][playerX] = 1
                    i += 1
                placeShip()

def randomCoord():
    global rand1
    global rand2
    rand1 = random.randint(0,9)
    rand2 = random.randint(0,9)
    botX = rand1
    botY = rand2

def shoot():
    global rand1
    global rand2
    global hits
    randomCoord()
    if gameBoard[rand1][rand2] == 0:
        gameBoard[rand1][rand2] = 2
        printBoard()
    elif gameBoard[rand1][rand2] == 1:
        gameBoard[rand1][rand2] = 3
        printBoard()
        hits += 1
    else:
        shoot()

def AI():
    global hits
    turns = 0
    while turns <= 30:
        if hits == 17:
            print("The AI won!")
            return
        shoot()
        turns += 1
        time.sleep(1)
    if turns == 31:
        print("You won!")
        return

placeShip()
