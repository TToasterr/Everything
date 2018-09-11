import random, time, sys

moveDown = "\n"*22
#moves the board down so it looks nice instead of just stacking on top of each other

boardSize = 10
#p self explanatory

gameBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
alphabet = ["A","B","C","D","E","F","G","H","I","J"]
#generates board and alphabet

Five = 1
Four = 1
Three = 2
Two = 1
#the number of ships you have to place

shipsPlaced = 0
#how many ships youve placed

hits = 0
#how many times the bot has hit you

lastHit = 0
b4LastHit = 0
lastCoords = [0,0]
#what the last shot was (1 for hit, 0 for miss)
#what the hit before the last hit was (but also sorta just turned into a counter)
#where the last shot was

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
#converts a to 0, b to 1, etc. for coordinates

def printBoard():
    print(moveDown)
    print(" ", *alphabet, sep="  ")
    print("  ", "-  " * 10)
    for i in range(boardSize):
        print(i, *gameBoard[i], sep="  ")
#prints the board

def cantPlace():
    d = input("\n\nYou can't place that ship there! Not enough space. \nPress enter to continue. \n")
    if d == "":
        placeShip()
#gets called if you try to place something off of the board

def outOf():
    d = input("\n\nYou don't have any more of that ship! \nPress enter to continue. \n")
    if d == "":
        placeShip()
#gets called if you try to place a ship you dont have any more of

def reduceShip():
    global shipL
    global Three
    global Four
    global Five
    global Two

    if shipL == 5:
        Five = 0
    elif shipL == 4:
        Four = 0
    elif shipL == 3:
        Three -= 1
    elif shipL == 2:
        Two = 0
#gets called every time you place a ship, reduces the number that you have left

def placeShip():
    global a
    global b
    global c
    global Five
    global Four
    global Three
    global Two
    global shipsPlaced
    global shipL
	global direc

    if shipsPlaced == 5:
        AI()
        return

    printBoard()
    a = input("\n\nWhat ship would you like to place? \n'listShips' to see what you have. \nFormat like '3'\n")

    if a == "listShips":
        print("\nYou have:\n", Five, "five long(s)\n", Four, "four long(s)\n", Three, "three long(s)\n", Two, "two long(s)\n\nPress enter to continue.")
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
	#sets playerx and playery to the coordinates they chose

    shipL = int(a)
    direc = c
	#sets the ship length and direction

    if shipL == 5 and Five == 0:
        outOf()
    elif shipL == 4 and Four == 0:
        outOf()
    elif shipL == 3 and Three == 0:
        outOf()
    elif shipL == 2 and Two == 0:
        outOf()
	#test for if player is out of ship
    else:
        if playerX < (shipL - 1) and c == "left":
            cantPlace()
        elif playerX > ((10 - shipL) + 1) and c == "right":
            cantPlace()
        elif playerY < (shipL - 1) and c == "up":
            cantPlace()
        elif playerY > ((10 - shipL) + 1) and c == "down":
            cantPlace()
		#test for if the ship runs into a wall
        else:
            reduceShip()
            if direc == "left":
                i = 0
                while i < (shipL):
                    gameBoard[playerY][int(playerX) - i] = 1
                    i += 1
                placeShip()
            elif direc == "right":
                i = 0
                while i < (shipL):
                    gameBoard[playerY][int(playerX) + i] = 1
                    i += 1
                placeShip()
            elif direc == "up":
                i = 0
                while i < (shipL):
                    gameBoard[playerY - i][playerX] = 1
                    i += 1
                placeShip()
            elif direc == "down":
                i = 0
                while i < (shipL):
                    gameBoard[playerY + i][playerX] = 1
                    i += 1
                placeShip()
			#places the ship

def randomCoord():
    global rand1
    global rand2
    rand1 = random.randint(0,9)
    rand2 = random.randint(0,9)
#generates a random set of coordinates
	
def shoot():
    global rand1
    global rand2
    global hits
    global lastHit
    global b4LastHit

    randomCoord()
    if gameBoard[rand1][rand2] == 0:
        gameBoard[rand1][rand2] = 2
        printBoard()
        print("The bot missed!")
        lastHit = 0
    elif gameBoard[rand1][rand2] == 1:
        gameBoard[rand1][rand2] = 3
        printBoard()
        print("The bot hit!")
        lastHit = 1
        lastCoords = [rand1, rand2]
        hits += 1
	#if the bot hits a ship, print it and set lastHit and lastCoords
    else:
        shoot()
	#if the bot hits somewhere its already shot, reshoot

def AI():
    global hits
    turns = 0
    while turns <= 30:
        if hits == 17:
            print("The AI won!")
            sys.exit()
        shoot()
        turns += 1
        time.sleep(1)
	#does 30 turns, 1 second long, with random coords
    if turns == 31:
        print("\n\nYou won!")
        sys.exit()
	#if the bot does 30 turns without sinking all ships, you win

placeShip()
#runs everything always
