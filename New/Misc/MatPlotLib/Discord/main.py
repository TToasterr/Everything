import matplotlib.pyplot as plt
import numpy as np

file = open("messages2.txt", encoding="utf8")
text = file.read()
file.close()

n = 0
array = text.split("\n\n")
# print(array)

for i in range(len(array)):
    try:
        array[i-n] = array[i-n][1:3]
        try:
            temp = int(array[i-n][0])
            temp = int(array[i-n][1])
        except:
            del array[i-n]
            n = n + 1
    except:
        del array[i-n]
        n = n + 1


array = np.array(array)
unique, counts = np.unique(array, return_counts=True)

# print(unique)
# print(counts)

# print("\n".join(array))
plt.plot(unique, counts)
plt.show()