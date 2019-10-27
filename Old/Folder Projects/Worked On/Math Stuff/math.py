from PIL import Image as image
from bs4 import BeautifulSoup
from io import BytesIO
import requests
import urllib
import os


def clear(): return os.system('cls')


clear()
page_link = "https://www.slader.com/textbook/9780133185829-geometry-common-core/" + input("What is the page number?\n") + "/"
clear()
questions = input("What are the questions?\n").split(", ")
clear()

page = urllib.request.urlopen(page_link).read()
soup = BeautifulSoup(page, 'html.parser')

page_questions = ("%s" % (soup.findAll('span', attrs={'class': 'answer-number'}))).split("<span class=\"answer-number\">")

page_questions = " ".join(page_questions)
page_questions = "\n".join(page_questions.split("</span>, ")).split("</span>]")[0].split("[ ")[1].replace(" ", "")

for number in page_questions.split("\n"):
    if number.replace(".", "") in questions:
        answer = ("%s" % (soup)).split("%s</span>" % number)[1].split("</p>")[0].replace("<p class=\"answer\">", "").strip()
        print(number, end=' ')
        if "<img alt=\"\" class=\"image-large\"" in answer:
            answer = answer.split("<img alt=\"\" class=\"image-large\"")[0].strip().replace("<img alt=\"\" class=\"image-reg\" src=\"", "").replace("\"/>", "")
        print(answer)

# print(page_questions)
