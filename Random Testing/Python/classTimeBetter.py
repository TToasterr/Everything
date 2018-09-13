import time
from datetime import datetime

currentTime = int(datetime.now().strftime("%H%M"))
time = 0

start = 1350
p1 = 1525
p2 = 1715
lunch = 1800
p3 = 1935
p4 = 2035

def setTime():
    global time
    if time > 59 and time < 100:
        time -= 100
        time += 60
    elif time > 159 and time < 200:
        time -= 100
        time += 60

def doThing():
    global time
    global hours
    global minutes

    if time < 100:
        hours = "00"
        minutes = time
    elif time < 1000:
        hours = time[:1]
        minutes = time[1:]
    else:
        hours = time[:2]
        minutes = time[2:]
        
if currentTime < start:
    print("School hasn't started yet!")

elif currentTime < p1:
    time = p1 - currentTime

    setTime()
    doThing()

    print("There is %s:%s left in period 1!" % (hours,minutes))

elif currentTime < p2:
    time = p2 - currentTime

    setTime()
    doThing()

    print("There is %s:%s left in period 2!" % (hours,minutes))

elif currentTime < lunch:
    time = lunch - currentTime

    setTime()
    doThing()

    print("There is %s:%s left in lunch!" % (hours,minutes))

elif currentTime < p3:
    time = p3 - currentTime

    setTime()
    doThing()

    print("There is %s:%s left in period 3!" % (hours,minutes))

elif currentTime < p4:
    time = p4 - currentTime

    setTime()
    doThing()

    print("There is %s:%s left in period 4!" % (hours,minutes))

else:
    print("School is over!")

    
