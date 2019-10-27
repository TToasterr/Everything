import matplotlib.pyplot as plt
import numpy as np

masses = [7.2, 13, 10.9, 18.77]
densities = [1.4, 2.1, 5.4, 9.3]
periods = [2, 3, 5, 6]

fig = plt.figure()
ax2 = fig.add_subplot(111)

massline = plt.plot(periods, masses, label="Mass")
densityline = plt.plot(periods, densities, label="Density")

massbestfit = plt.plot(periods, np.poly1d(np.polyfit(periods, masses, 1))(periods), label="Line of best fit (Mass)")
densitybestfit = plt.plot(periods, np.poly1d(np.polyfit(periods, densities, 1))(periods), label="Line of best fit (Density)")

# plt.plot(4, 12, 'ro')

plt.xlabel("Period")
plt.ylabel("Grams")
plt.legend(handles=[massline[0], densityline[0], massbestfit[0], densitybestfit[0]])

ax = plt.gca()
line1 = ax.lines[2]
line2 = ax.lines[3]
# print(line1, " ", line2)
arr1 = line1.get_ydata()
arr2 = line2.get_ydata()

one = (arr1[1] + arr1[2]) / 2
two = (arr2[1] + arr2[2]) / 2

plt.plot(4, one, 'ro')
plt.plot(4, two, 'ro')

gmdensity = 5.323
plt.plot(4, 5.323, 'ro')

ax2.annotate("  Germanium Mass (%sg)" % round(one, 2), xy=[4, one], textcoords="data")
ax2.annotate("  Germanium Density (%sg)" % round(two, 2), xy=[4, two], textcoords="data")
ax2.annotate("  Germanium ACTUAL Density (5.323g)" % round(two, 2), xy=[4, 5.323], textcoords="data")

print(one)
print(two)

plt.show()