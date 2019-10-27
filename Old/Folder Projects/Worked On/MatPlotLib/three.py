from math import *
import numpy as np
import matplotlib.pyplot as plt
from random import randint as ri

array = [[[(x * x * y) for x in range(10)] for y in range(10)] for z in range(10)]

for z in array:
    for y in z:
        plt.plot(y, 'k--', lw=1, aa=True)

plt.show()
