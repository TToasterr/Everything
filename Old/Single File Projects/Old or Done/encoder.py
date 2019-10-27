import random as r

which = input("Would you like to encode or decode? \n")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
doneOnce = False
decodeKey = []

if which == "encode" or which == "en" or which == "e":
    startingMsg = input("What message would you like to encode? \n")

    timesToReencode = r.randint(3,10)

    for a in range(timesToReencode):
        if doneOnce:
            startingMsg = output
        output = []

        numForward = r.randint(1,25)

        decodeKey.append(numForward)

        for pos in range(len(startingMsg)):
            if startingMsg[pos] == " ":
                output.append(" ")

            for letter in range(len(alphabet) - 26):
                if startingMsg[pos] == alphabet[letter]:
                    output.append(alphabet[letter + numForward])

        doneOnce = True

    print(*output, sep="")
    print(*decodeKey, sep="|")

if which == "decode" or which == "de" or which == "d":
    startingMsg = input("What message would you like to decode? \n")
    decodeKey = input("What is the decoding key? \n").split("|")
    output = startingMsg

    for a in decodeKey:
        startingMsg = output
        output = []

        for pos in range(len(startingMsg)):
            if startingMsg[pos] == " ":
                output.append(" ")

            for letter in range(len(alphabet) - 26):
                if startingMsg[pos] == alphabet[letter]:
                    output.append(alphabet[int(letter) - int(a)])

    print(*output, sep="")
