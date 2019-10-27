from math import sin as sin
from time import sleep as s
x = 1
while 1:
    print(x, '   ', end='')
    print(sin(x))
    x = x + 1
    s(0.05)
