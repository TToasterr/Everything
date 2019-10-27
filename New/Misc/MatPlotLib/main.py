from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
level = [37, 28, 25, 17, 15, 15, 13, 12, 11, 9, 8, 8, 8, 8, 8, 8, 6, 5, 5, 4]
xp = [124.5, 60.5, 43.5, 17.2, 13.7, 9.3, 8.2, 6.5, 3.7, 3.7, 3.6, 3.2, 3, 2.9, 2.9, 2.1, 1.6, 1.2, 0.9, 0.4]
messages = [62, 30, 22, 8.5, 6.8, 6.5, 4.6, 4, 3.2, 1.8, 1.8, 1.8, 1.5, 1.4, 1.4, 1.4, 1, 0.7, 0.6, 0.4]
people = ["Toaster", "Nate", "Jonathan", "Connor M", "Isa", "Quinn", "Will", "Liam", "Satchel", "Tarnished", "Soundwave", "Sauron", "Dylan", "stwafes", "Xavier", "Jimmy", "Tre", "Connor A", "FireDragon", "Vlalkosei"]

# -----------------------------------------------------------------------------

for i in range(20):
    xp[i] = xp[i]*10
    messages[i] = messages[i]*10

levelline = plt.plot(ranks, level, label="Level")
xpline = plt.plot(ranks, xp, label="XP")
messagesline = plt.plot(ranks, messages, label="Messages")

# -----------------------------------------------------------------------------

plt.xlabel("Rank")
plt.legend(handles=[xpline[0], levelline[0], messagesline[0]])

for x in range(20):
    # ax.annotate(people[x], xy=[ranks[x],93], textcoords="data")
    ax.annotate(level[x], xy=[ranks[x],level[x]], textcoords="data")
    ax.annotate(int(xp[x]*1000), xy=[ranks[x],xp[x]], textcoords="data")
    ax.annotate(int(messages[x]*100), xy=[ranks[x],messages[x]], textcoords="data")

plt.show()