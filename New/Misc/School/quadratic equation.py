while 1:
    print("\n")
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))

    x = (-b) / (2*a)

    print("\n\ny-int:      " + str(c))
    print("\nx:          -%s / 2*%s" % (b, a))
    print("x:          %s / %s" % (-b, 2*a))
    print("x:          " + str(x))

    y = (a * (x) ** 2) + (b * x) + c
    print("\ny:          (%s * %s²) + (%s * %s) + %s" % (a, x, b, x, c))
    print("y:          %s + %s + %s" % (a * x ** 2, b * x, c))
    print("y:          " + str(y))

    print("\nvert form:  y = %s(x + %s)² - %s" % (a, x, y))