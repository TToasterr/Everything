from math import *
import numpy as np
import matplotlib.pyplot as plt
from random import randint as ri

for x in range(1):
    for i in range(4):
        array = [(sin(x) * (sin(i))) for x in range(51)]
        plt.plot(array, 'k--', lw=1, aa=True)

    plt.show()
