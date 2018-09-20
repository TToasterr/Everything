xs = [2,-3,1,0,-5]

def answer(xs):
    output = 1
    nums = []
    negCount = 0

    for i in xs:
    #for the number of values in input array
        print "xs[", i, "] =",xs[i], "\n"
        if i == 0:
        #THIS CHUNK: if number is 0, set it to 1
        #if number is 0

            ii = 1
            #number = 1

            nums.append(ii)
            #append current number to number list

        elif i < 0:
        #THIS CHUNK: if the number is negative, check if there have been other negatives. if there have, switch them both to positive and add them to the number list. If there havent, just 'bookmark' the number so the next one can make it positive
        #if number is negative

            if negCount > 1:
            #if negative count is more than 1

                iii *= negative
                #multiply the current negative by the last one

                nums.append(iii)
                #append current number to number list

                negCount = 0
                #reset negative count

            else:
            #if first negative

                negCount += 1
                #add 1 to negative count

                negative = i
                #set 'negative' to current number

        else:
        #THIS CHUNK: if number is positive, append it to the number list
        #if positive

            nums.append(i)
            #append it to number list

        print i
        #print number


    if negCount == 1:
    #THIS CHUNK: if theres a leftover negative, multiply it with everything else like normal (like a positive would be)
    #if leftover negative at end of function

        output *= negative
        #multiply everything by it


    for xd in nums:
    #THIS CHUNK: multiply all numbers together
    #for numbers in number list

        printedOutput = output * xd
        print ""
        print output, "*", xd, ' = ', printedOutput
        output *= xd
        #multiply the numbers together


    print ""
    print output
    return output

answer(xs)
