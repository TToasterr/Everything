while 1:
    print("\n")
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))

    top = a*c
    bottom = b
    factors = []

    for i in range(1, top + 1):
       if top % i == 0:
           factors.append(i)

    for i in factors:
        for x in factors:
            if x * i == top:
                if x + i == bottom:
                    print("(%sx, %s)(%sx, %s)" % (str(a), str(x), str(a), str(i)))