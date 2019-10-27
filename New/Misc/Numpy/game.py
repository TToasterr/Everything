from random import *
import numpy as np
from time import *
import os

def clear(): return os.system('cls')
gameboard = ["-" for i in range(10)]
gameboard[0] = "C"
gameboard[9] = "O"
playerpos = 5
gameboard[playerpos] = "█"
scoreboard = [0 for i in range(10)]
scoreboard2 = [str(scoreboard[i]) for i in range(len(scoreboard))]
for i in range(len(scoreboard2)):
    if int(scoreboard2[i]) >= 0:
        scoreboard2[i] = scoreboard2[i] + "  "
    else:
        scoreboard2[i] = scoreboard2[i] + " "
unfinished = True
score = 0

while 1:
    clear()
    if (scoreboard[playerpos-1] == 0) and (scoreboard[playerpos+1] == 0):
        gameboard[playerpos] = "-"
        playerpos = playerpos + choice([1, -1])
    elif (scoreboard[playerpos-1] > scoreboard[playerpos+1]):
        gameboard[playerpos] = "-"
        playerpos = playerpos - 1
    elif (scoreboard[playerpos+1] > scoreboard[playerpos-1]):
        gameboard[playerpos] = "-"
        playerpos = playerpos + 1
    else:
        gameboard[playerpos] = "-"
        playerpos = playerpos + choice([1, -1])
    if (gameboard[playerpos] == "O"):
        gameboard = ["-" for i in range(10)]
        gameboard[0] = "C"
        gameboard[9] = "O"
        score = score - 1
        scoreboard[playerpos] = scoreboard[playerpos] - 1
        playerpos = 5
    elif (gameboard[playerpos] == "C"):
        gameboard = ["-" for i in range(10)]
        gameboard[0] = "C"
        gameboard[9] = "O"
        score = score + 1
        scoreboard[playerpos] = scoreboard[playerpos] + 1
        playerpos = 5

    gameboard[playerpos] = "█"
    scoreboard = list(np.linspace(scoreboard[0], scoreboard[9], 10))
    scoreboard2 = [str(scoreboard[i]) for i in range(len(scoreboard))]
    for i in range(len(scoreboard2)):
        if float(scoreboard2[i]) >= 0:
            scoreboard2[i] = scoreboard2[i] + "  "
        else:
            scoreboard2[i] = scoreboard2[i] + " "

    print("".join(gameboard))
    print("".join(scoreboard2))
    print()
    print(score)
    # print(str(scoreboard[playerpos-1]) + ", " + str(scoreboard[playerpos+1]))
    # print(scoreboard[playerpos-1] > scoreboard[playerpos+1])
    # print(scoreboard[playerpos+1] > scoreboard[playerpos-1])
    # sleep(0.5)