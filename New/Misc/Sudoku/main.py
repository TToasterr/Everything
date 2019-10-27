from random import *
from time import *
import numpy as np

board = np.zeros((9, 3, 3))
# print("\n".join(board[0]))
# print(board)

def printb():
    for i in range(3):
        for x in range(3):
            for y in range(3):
                board[i][x][y] = str(randint(1,9))
            print(board[i][x], end=" ")
        print()

printb()