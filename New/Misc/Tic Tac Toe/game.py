from random import *
from time import *

board = [["-" for i in range(3)] for i in range(3)]

def printb():
    for i in board:
        for x in i:
            print(x, end=" ")
        print()

# printb()
i = 0

while 1:
    inn = input("\n")

    inn = int(inn)-1
    row = 0

    if inn > 5:
        row = 2
        inn = inn - 6
    elif inn > 2:
        row = 1
        inn = inn - 3

    while board[row][inn] != "-":
        inn = input("\n")
        inn = int(inn)-1
        row = 0

        if inn > 5:
            row = 2
            inn = inn - 6
        elif inn > 3:
            row = 1
            inn = inn - 3

    if i == 0:
        i = 1
        board[row][inn] = "o"
    elif i == 1:
        i = 0
        board[row][inn] = "x"
    printb()