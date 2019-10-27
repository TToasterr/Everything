from colorama import Fore
from random import *
from time import *
import colorama
import os

colorama.init()
def clear(): return os.system('cls')

arr = []
arrlen = 100
# max = 26
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet = "█▓▒░"
# alphabet = list(alphabet)
alphabet = [f"{Fore.RED}b", f"{Fore.RED}r", f"{Fore.YELLOW}u", f"{Fore.YELLOW}h", " ", f"{Fore.GREEN}y", f"{Fore.GREEN}o", f"{Fore.CYAN}u", f"{Fore.CYAN}r", " ", f"{Fore.BLUE}m", f"{Fore.BLUE}o", f"{Fore.MAGENTA}m", f"{Fore.MAGENTA}."]
max = len(alphabet)-1
# arrlen = max


# while 1:
arr = []

for i in range(arrlen):
    arr.append(randint(0,max))

for i in range(len(arr)-1):
    for x in range(len(arr)-1):
        if (arr[x] > arr[(x+1)]):
            temp = arr[x+1]
            arr[x+1] = arr[x]
            arr[x] = temp
    # print("\n" * 100)
    for z in arr:
        print(alphabet[z], end="")
        # print(z, end="")
    print()
    sleep(0.01)

# for i in range(arrlen-1):
#     for x in range(arrlen-1):
#         if (arr[x] < arr[(x+1)]):
#             temp = arr[x]
#             arr[x] = arr[x+1]
#             arr[x+1] = temp
#     # print("\n" * 100)
#     for z in arr:
#         print(alphabet[z], end="")
#     print()
#     # sleep(0.001)