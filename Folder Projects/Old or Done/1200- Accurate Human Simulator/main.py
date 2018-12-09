import random, words

spicyness = 1

def help():
    print("\nspicy - Toggles spicyness on or off. Is on by default. \n")
    print("go - gives a random sentence\n")

def quote():
    a = random.randint(0,len(startingNouns))
    b = random.randint(0,len(adverbs))
    c = random.randint(0,len(verbs))
    d = random.randint(0,len(adjectives))
    e = random.randint(0,len(nouns))
    f = random.randint(0,len(startingNouns))

    one = startingNouns[a-1]
    two = adverbs[b-1]
    three = verbs[c-1]
    four = adjectives[d-1]
    five = nouns[e-1]
    six = startingNouns[f-1]

    if four.startswith("a"):
        middle = "an"
    else:
        middle = "a"

    print("\n\"", one, two, three, middle, four, five, "\" \n-", six)

def simple():
    a = random.randint(0,len(startingNouns))
    b = random.randint(0,len(endingVerbs))

    one = startingNouns[a-1]
    two = endingVerbs[b-1]

    print("\n", one, two)

def average():
    a = random.randint(0,len(adjectives))
    b = random.randint(0,len(nouns))
    c = random.randint(0,len(endingVerbs))

    one = adjectives[a-1]
    two = nouns[b-1]
    three = endingVerbs[c-1]

    print("\n", one, two, three)

def complexish():
    a = random.randint(0,len(adjectives))
    b = random.randint(0,len(nouns))
    c = random.randint(0,len(verbs))
    d = random.randint(0,len(nouns))

    one = adjectives[a-1]
    two = nouns[b-1]
    three = verbs[c-1]
    four = nouns[d-1]

    print("\n", one, two, three, four)

def memey():
    a = random.randint(0,len(nouns))
    b = random.randint(0,len(verbs))
    c = random.randint(0,len(adjectives))
    d = random.randint(0,len(nouns))

    one = nouns[a-1]
    two = verbs[b-1]
    three = adjectives[c-1]
    four = nouns[d-1]

    print("\n", one, two, three, four)

def go():
    a = random.randint(0,4)
    if a == 0:
        quote()
    if a == 1:
        simple()
    if a == 2:
        average()
    if a == 3:
        complexish()
    if a == 4:
        memey()

#------------------------------------------------------------------

while True:
    x = input("\nInput 'help' for a list of commands. \n")
    #constantly listens for input

    if spicyness == 1:
        startingNouns = words.startingNouns
        nouns = words.nouns
        adjectives = words.adjectives
        endingVerbs = words.endingVerbs
        verbs = words.verbs
        adverbs = words.adverbs
    #setting spiciness

    if spicyness == 0:
        startingNouns = words.FFstartingNouns
        nouns = words.FFnouns
        adjectives = words.FFadjectives
        endingVerbs = words.FFendingVerbs
        verbs = words.FFverbs
        adverbs = words.FFadverbs
    #setting spiciness

    if x == "help":
        help()
    if x == "go" or x == "":
        go()
    if "spicy" in x:
        if spicyness == 1:
            spicyness = 0
            print("Spicyness off!")
        elif spicyness == 0:
            spicyness = 1
            print("Spicyness on!")
    if "spicy" not in x and "go" not in x and "help" not in x and not x == "":
        print("\nPlease input a correct command! Do 'help' for help. \n")
