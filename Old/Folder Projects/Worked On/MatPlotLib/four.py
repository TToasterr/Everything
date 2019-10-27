import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from random import *
from time import *
import numpy as np

rScores = [
-4,
-4,
-2,
-2,
-2,
-2,
-1,
-1,
-1,
2
]
gScores = [
-4,
-1,
-1,
-1,
-1,
1,
1,
1,
2
]
bScores = [
-1,
1,
1,
2,
2,
2,
4,
4,
4,
4,
4
]

plt.ion()

# while 1:
plt.clf()
# rScores.append(choice([-4, -2, -1, 1, 2, 4]))

rHist = plt.hist(rScores, facecolor='red', alpha=0.5)
gHist = plt.hist(gScores, facecolor='green', alpha=0.5)
bHist = plt.hist(bScores, facecolor='blue', alpha=0.5)

plt.xticks(np.arange(-4, 4, 1))

plt.draw()
plt.pause(50)
# plt.close()