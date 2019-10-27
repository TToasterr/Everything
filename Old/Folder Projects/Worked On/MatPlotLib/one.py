import matplotlib.pyplot as plt
import numpy as np
from math import *
from random import randint as ri

array1 = [[[((sin(i) * cos(o)) * 2) + (p * 0.01) for i in range(10)] for o in range(10)] for p in range(10)]
# array2 = [[[(i * cos(o)) + (p * 0.01) for i in range(10)] for o in range(10)] for p in range(10)]
# array3 = [[[(i * tan(o)) + (p * 0.01) for i in range(10)] for o in range(10)] for p in range(10)]


print(array1)

for p in array1:
    for o in p:
        # plt.plot(o, p, 'k', lw=0.1)
        plt.plot(o, p, lw=0.5)

plt.show()


# print("\n\n", array2)
#
# for p in array2:
#     for o in p:
#         # plt.plot(o, p, 'k', lw=0.1)
#         plt.plot(o, p, lw=0.5)
#
# plt.show()
#
#
# print("\n\n", array3)
#
# for p in array3:
#     for o in p:
#         # plt.plot(o, p, 'k', lw=0.1)
#         plt.plot(o, p, lw=0.5)
#
# plt.show()
