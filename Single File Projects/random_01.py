from time import sleep
from random import randint as ri

testArray = [['%s' % "  ".join(['%s' % ((x + 1 * (z + 1)) + y)
                                for x in range(20)]) for y in range(40)] for z in range(1500)]

for i in testArray:
        sleep(0.015)
        print()

        # for x in i:
        # 	print("|" * x)
        # 	sleep(0.1)
        print("\n".join(i))
