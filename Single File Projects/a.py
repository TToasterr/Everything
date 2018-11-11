from random import choice as ch
from random import randint as ri
import webbrowser

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",'p','q','r','s','t','u','v','w','x','y','z']
upAlphabet = [letter.upper() for letter in alphabet]

print("")

for num in range(25):
    thingg = []

    for i in range(24):
        thing = ri(0,2)
        if thing == 0:
            thingg.append(ch(alphabet))
        elif thing == 1:
            thingg.append(ch(upAlphabet))
        elif thing == 2:
            thingg.append(str(ri(0,9)))

    url = "".join(thingg)
    final = "https://www.youtube.com/channel/%s" % url
    new = 2
    print(url)
    webbrowser.open(final, new=new)
