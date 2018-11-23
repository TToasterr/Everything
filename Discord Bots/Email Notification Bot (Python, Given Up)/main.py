from datetime import datetime
from random import randint as ri
from random import choice as ch
import discord
import easyimap
import smtplib
import subprocess
import sys
sys.path.append("H:/Misc")

client = discord.Client()
placeholder = []
last_5_emails = []
current_5_emails = []

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
        user_id = user_login[2]

        try:
            imapper = easyimap.connect('imap.gmail.com', login, password)
        except:
            print("Couldnt log into %s.\n" % login)

        for mail_id in imapper.listids(limit=5):
            mail = imapper.mail(mail_id)
            last_5_emails.append(mail)
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
    global last_5_emails
    current_5_emails = []

    if message.author.bot:
        return()

    if message.content[:14] == "email.addlogin":
        args = message.content[15:].split(", ")
        email = args[0]
        passw = args[1]

        with open("H:/Misc/emaillogins.txt", "a+") as logins:
            logins.write("%s|||%s|||%s\n" % (email, passw, message.author.id))

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
        if user_login != [""]:
            login = user_login[0]
            password = user_login[1]
            user_id = user_login[2]

            current_5_emails = []

            if message.author.id == user_id:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.ehlo()
                smtpObj.starttls()
                # try:
                smtpObj.login(login, password)
                # except:
                #     await client.send_message(message.channel, content = "You haven't enabled less secure apps for the account **%s**!\nPlease do so to use the bot." % (login))
                #     return()

                imapper = easyimap.connect('imap.gmail.com', login, password)

                for mailid in imapper.listids(limit=5):
                    mail = imapper.mail(mailid)
                    current_5_emails.append(mail)

                if last_5_emails == [] or last_5_emails == [""] or last_5_emails == "":
                    await client.send_message(message.channel, content = "Logged into **%s** succesfully!" % login)
                    return

                print([email.title for email in current_5_emails])
                for email_num in range(len(current_5_emails)):
                    print(email_num)
                    if current_5_emails[email_num].message_id != last_5_emails[email_num].message_id:
                        await client.send_message(message.channel, content = "<@%s>\n**From:** %s\n**Subject:** %s\n**Body:** %s" % (message.author.id, current_5_emails[email_num].from_addr, current_5_emails[email_num].title, current_5_emails[email_num].body))
                        print("%s got a new email!\n" % message.author)
                last_5_emails = current_5_emails



with open('H:/Misc/token5.txt', 'r') as myfile:
    token = myfile.read()
client.run(token)
