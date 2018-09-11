import random

moveDown = "\n"

boardSize = 10
hits = 0

gameBoard = [[0 for x in range(boardSize)] for y in range(boardSize)]
alphabet = ["A","B","C","D","E","F","G","H","I","J"]

def printBoard():
    print(moveDown * 20)
    print(" ", *alphabet, sep="  ")
    print("  ", "-  " * 10)
    for i in range(boardSize):
        print(i, *gameBoard[i], sep="  ")

boardLayout01 = [
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,1,1,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,1,1,1,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0]
]
boardLayout02 = [
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
boardLayout03 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,1,1,1],
    [1,1,0,0,0,0,0,0,0,0]
]

yaay = random.randint(0,2)
if yaay == 0:
    boardLayout = boardLayout01
elif yaay == 1:
    boardLayout = boardLayout02
elif yaay == 2:
    boardLayout = boardLayout03

def guess():
    global hits
    a = input("Where would you like to attack? \nPlease format like 'A,0' \n\n").split(",")

    if a[0] == "a" or a[0] == "A":
        a[0] = 0
    if a[0] == "b" or a[0] == "B":
        a[0] = 1
    if a[0] == "c" or a[0] == "C":
        a[0] = 2
    if a[0] == "d" or a[0] == "D":
        a[0] = 3
    if a[0] == "e" or a[0] == "E":
        a[0] = 4
    if a[0] == "f" or a[0] == "F":
        a[0] = 5
    if a[0] == "g" or a[0] == "G":
        a[0] = 6
    if a[0] == "h" or a[0] == "H":
        a[0] = 7
    if a[0] == "i" or a[0] == "I":
        a[0] = 8
    if a[0] == "j" or a[0] == "J":
        a[0] = 9
    
    shotPosX = a[1]
    shotPosY = a[0]

    if boardLayout[int(shotPosX)][int(shotPosY)] == 0:
        gameBoard[int(shotPosX)][int(shotPosY)] = 2
        boardLayout[int(shotPosX)][int(shotPosY)] = 2
        print("\nIt's a miss! \n")
        printBoard()
        guess()
    elif boardLayout[int(shotPosX)][int(shotPosY)] == 1:
        gameBoard[int(shotPosX)][int(shotPosY)] = 1
        boardLayout[int(shotPosX)][int(shotPosY)] = 2
        print("\nIt's a hit! \n")
        hits += 1
        printBoard()
        guess()
    elif boardLayout[int(shotPosX)][int(shotPosY)] == 2:
        print("\nYou've already shot there! \n")
        printBoard()
        guess()

while hits < 17:
    printBoard()
    guess()
if hits >= 17:
    print("You win!")

while 1:
    if hits == 17:
        print("\n\nYou win! \n\n")
