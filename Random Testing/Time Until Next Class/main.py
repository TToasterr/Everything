import time

currentTime = int(input("What time is it? \n"))
time = 0

format = "\n"*50

start = 750
p1 = 925
p2 = 1115
lunch = 1200
p3 = 1335
p4 = 1435

def setTime():
    global time
    if time > 59 and time < 100:
        time -= 100
        time += 60
    elif time > 159 and time < 200:
        time -= 100
        time += 60

if currentTime < start:
    print(format)
    print("School hasn't started yet!")

elif currentTime < p1:
    time = p1 - currentTime

    setTime()

    print(format)
    print("There is %s left in period 1!" % time)

elif currentTime < p2:
    time = p2 - currentTime

    setTime()

    print(format)
    print("There is %s left in period 2!" % time)

elif currentTime < lunch:
    time = lunch - currentTime

    setTime()

    print(format)
    print("There is %s left in lunch!" % time)

elif currentTime < p3:
    time = p3 - currentTime

    setTime()

    print(format)
    print("There is %s left in period 3!" % time)

elif currentTime < p4:
    time = p4 - currentTime

    setTime()

    print(format)
    print("There is %s left in period 4!" % time)

else:
    print(format)
    print("School is over!")
