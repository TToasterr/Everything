from datetime import datetime
from random import randint as ri
from random import choice as ch
import discord
import sys
import easyimap
import smtplib
import subprocess
sys.path.append("H:/Misc")

client = discord.Client()
placeholder = []

with open ("H:/Misc/emaillogins.txt", "r+") as logins:
    all_logins = logins.read().split("\n")

# try:
for login in all_logins:
    thing = login.split("|||")
    placeholder.append(thing)
    all_logins = placeholder

for user_login in all_logins:
    if user_login == [""]:
        do = "nothing"
    else:
        login = user_login[0]
        password = user_login[1]

        try:
            imapper = easyimap.connect('imap.gmail.com', login, password)
        except:
            print("Couldnt log into %s.\n" % login)

        for mail_id in imapper.listids(limit=1):
            mail = imapper.mail(mail_id)
            last_email_id = mail.message_id
# except:
#     print("The email list was empty!")
#     last_email_id = ""



@client.event
async def on_ready():
    activeServers = client.servers
    sum = 0
    for s in activeServers:
        sum += len(s.members)
    print("Bot started in %s server(s), with %s users.\n" % (len(client.servers), sum))
    await client.change_presence(game=discord.Game(name="IDFK"))



@client.event
async def on_server_join(server):
    print("The bot just joined the server '%s'\n" % server.name)



@client.event
async def on_message(message):
    global last_email_id
    email_id = ""

    if message.author.bot:
        return()

    if message.content[:14] == "email.addlogin":
        args = message.content[15:].split(", ")
        email = args[0]
        passw = args[1]

        with open("H:/Misc/emaillogins.txt", "a+") as logins:
            logins.write("%s|||%s\n" % (email, passw))

        print("%s added a new email to the bot." % message.author)
        print("Email: %s" % email)
        print("Pass: %s" % passw)
        print("")
        return

    with open ("H:/Misc/emaillogins.txt", "r+") as logins:
        all_logins = logins.read().split("\n")

    placeholder = []

    for login in all_logins:
        thing = login.split("|||")
        placeholder.append(thing)
        all_logins = placeholder

    for user_login in all_logins:
        if user_login == [""]:
            do = "nothing"
        else:
            login = user_login[0]
            password = user_login[1]

            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            # try:
            smtpObj.login(login, password)
            # except:
            #     await client.send_message(message.channel, content = "You haven't enabled less secure apps for the account **%s**!\nPlease do so to use the bot." % (login))
            #     return()

            imapper = easyimap.connect('imap.gmail.com', login, password)

            for mailid in imapper.listids(limit=1):
                mail = imapper.mail(mailid)
                email_id = mail.message_id

            if email_id != last_email_id:
                if last_email_id == "":
                    await client.send_message(message.channel, content = "Logged into **%s** succesfully!" % login)
                    return
                last_email_id = email_id
                for mail_id in imapper.listids(limit=1):
                    mail = imapper.mail(mail_id)
                await client.send_message(message.channel, content = "<@%s>\n**From:** %s\n**Subject:** %s\n**Body:** %s" % (message.author.id, mail.from_addr, mail.title, mail.body))

                print("%s got a new email!\n" % message.author)



with open('H:/Misc/token5.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
