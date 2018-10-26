Map = [
    [0 for x in range(25)] for y in range(25)
]


def printMap ():
    for y in range(len(Map)):
        for x in range(len(Map)):
            if Map[x][y] == 0:
                print("▓▓", end = "")
        print("")
