from random import choice as ch
from random import randint as ri
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",'p','q','r','s','t','u','v','w','x','y','z']
upAlphabet = [letter.upper() for letter in alphabet]

print("")

for num in range(10000):
    thingg = []

    for i in range(22):
        thing = ri(0,15)
        if thing < 5:
            thingg.append(ch(alphabet))
        elif thing < 10:
            thingg.append(ch(upAlphabet))
        elif thing < 15:
            thingg.append(str(ri(0,9)))
        elif thing < 16:
            thingg.append(ch(["_","-"]))

    url = "".join(thingg)
    final = "https://www.youtube.com/channel/UC%s" % url
    new = 2
    page = urlopen(final)
    soup = BeautifulSoup(page, 'html.parser')

    html = soup.find("a", {"class":"spf-link branded-page-header-title-link yt-uix-sessionlink"})
    channel_name = html.text
    print(channel_name)

    if channel_name != "":
        webbrowser.open(final, new=new)
        print("\n\n--------------------\n%s \nexists.\nChannel Name: %s\n--------------------" % (final, channel_name))
    else:
        print("\n\n%s \ndoesnt exist." % final)
