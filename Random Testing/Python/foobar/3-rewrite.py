# xs = [2,-3,1,0,-5]
# xs = [-2, -3, 4, -5]
xs = [2, 0, 2, 2, 0]

def answer(xs):
    negativeAmount = 0
    breaker = "--------------------------"
    output = 1

    for i in range(len(xs)):
        print "----BEFORE:----"
        print "i:",i
        print "xs[i]:",xs[i]
        print "xs:", xs

        if xs[i] == 0:
            xs[i] = 1

        elif xs[i] < 0:
            if negativeAmount == 1:
                xs[i] = (xs[i] * lastNegative)
                xs[lastNegativePos] = 1
                negativeAmount = 0

            else:
                lastNegative = xs[i]
                lastNegativePos = i
                negativeAmount += 1


        print "----AFTER:----"
        print "i:",i
        print "xs[i]:",xs[i]
        print "xs:", xs
        print breaker

    for i in range(len(xs)):
        output *= xs[i]

    print breaker
    print output
    return output

answer(xs)
