from turtle import *
from math import *

print("Drawing...")
speed(100000000000000000000000)

color("white", "gray")
begin_fill()
while 1:
    forward(200)
    left(200)
    if abs(pos()) < 1:
        break

end_fill()
done()

getscreen()._root.mainloop()
