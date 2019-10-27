import subprocess
import sys
import os

def clear(): return os.system('cls')
sys.path.append("C:/Windows/System32/drivers/etc")

clear()

with open("C:/Windows/System32/drivers/etc/hosts", "a") as hosts:
    hosts.write("127.0.0.1 youtube.com")