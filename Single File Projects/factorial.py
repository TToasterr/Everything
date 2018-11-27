number = int(input("What number would you like the additorial for?\n\n"))

thing = 1
print("")

for i in range(number + 1):
    if i != 0:
        thing *= i

print("")
print(thing)
