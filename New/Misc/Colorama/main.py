from colorama import Fore
from random import *
from time import *
import colorama

colorama.init()
string = "abcdefghijklmnopqrstuvwxyz"
string = list(string)
arr = []
shuffle(string)

# num = 26 * 5000
num = 26 * 25 * 24 * 23 * 22 * 21 * 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
start = time()
start1 = time()
x = 0

for i in range(num):
    shuffle(string)
    temp = "".join(string)
    while temp in arr:
        shuffle(string)
        temp = "".join(string)
    arr.append(temp)
    # if i % 10000 == 0:
    #     print(f"{Fore.WHITE}[{Fore.YELLOW}{ctime()}{Fore.WHITE}] STRING NUMBER {Fore.GREEN}{i}{Fore.WHITE}/{Fore.RED}{num}{Fore.WHITE} GENERATED IN {Fore.CYAN}{timee}")

    timee1 = time() - start1
    # print(str(timee1).split("."))
    if str(timee1).split(".")[0] == "1":
        timee = time() - start
        print(f"\n{Fore.WHITE}[{Fore.YELLOW}{ctime()}{Fore.WHITE}] {Fore.GREEN}{i-x}{Fore.WHITE} STRINGS GENERATED IN THE PAST {Fore.CYAN}{timee1}s")
        print(f"{Fore.WHITE}[{Fore.YELLOW}{ctime()}{Fore.WHITE}] {Fore.GREEN}{i}{Fore.WHITE} STRINGS TOTAL, IN {Fore.CYAN}{timee}s")
        print(f"{Fore.WHITE}[{Fore.YELLOW}{ctime()}{Fore.WHITE}] {Fore.RED}{num - i}{Fore.WHITE} STRINGS TO GO")
        # start = time()
        start1 = time()
        x = i

# arr.sort()
# for name in arr:
#     # if name.startswith("Q"):
#     print(name)