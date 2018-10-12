from datetime import datetime as dt
from time import sleep as s

while 1:
    now = str(dt.now())
    a = now.split(":")
    a[0] = str(a[0])[11:]
    a[0] = int(a[0])

    if a[0] > 12:
        a[0] -= 12

    a[0] = str(a[0])
    now = ":".join(a)

    print(now)
    s(0.0001)
