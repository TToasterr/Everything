import time
from datetime import datetime

timee = 0

start = 750
p1 = 925
p2 = 1115
lunch = 1200
p3 = 1335
p4 = 1435

def setTime():
    global timee
    if timee > 59 and timee < 100:
        timee -= 100
        timee += 60
    elif timee > 159 and timee < 200:
        timee -= 100
        timee += 60

def doThing():
    global timee
    global hours
    global minutes

    if timee < 10:
        hours = "00"
        minutes = "0" + str(timee)
    elif timee < 100:
        hours = "00"
        minutes = timee
    elif timee < 1000:
        hours = str(timee)[:1]
        minutes = str(timee)[1:]
    else:
        hours = str(timee)[:2]
        minutes = str(timee)[2:]

def exist():
    global timee
    global hours
    global minutes
    global currentTime
    global start
    global p1
    global p2
    global lunch
    global p3
    global p4

    currentTime = int(datetime.now().strftime("%H%M"))

    if currentTime < start:
        timee = start - currentTime

        setTime()
        doThing()

        print("School hasn't started yet! It starts in %s:%s" % (hours, minutes))

    elif currentTime < p1:
        timee = p1 - currentTime

        setTime()
        doThing()

        print("There is %s:%s left in period 1!" %(hours,   minutes))

    elif currentTime < p2:
        timee = p2 - currentTime

        setTime()
        doThing()

        print("There is %s:%s left in period 2!" %(hours,   minutes))

    elif currentTime < lunch:
        timee = lunch - currentTime

        setTime()
        doThing()

        print("There is %s:%s left in lunch!" % (hours, minutes))

    elif currentTime < p3:
        timee = p3 - currentTime

        setTime()
        doThing()

        print("There is %s:%s left in period 3!" %(hours,   minutes))

    elif currentTime < p4:
        timee = p4 - currentTime

        setTime()
        doThing()

        print("There is %s:%s left in period 4!" %(hours,   minutes))

    else:
        print("School is over!")

while 1:
    exist()
    time.sleep(0.5)
