import sys
import easyimap
import smtplib
from datetime import datetime

time = datetime.now()
login = sys.argv[1]
password = sys.argv[2]
emails = [""]
pmails = [""]
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login,password)
time2 = datetime.now()
timel = time2 - time
print("logged in in %s seconds." % timel)

time = datetime.now()
imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=5):
    mail = imapper.mail(mail_id)
    emails.append(mail.message_id)

time2 = datetime.now()
timel = time2 - time
print("got emails in %s seconds." % timel)
print("Running!")

while 1:
    num = 0
    time = datetime.now()

    pmails = [""]

    for mail_id in imapper.listids(limit=5):
        mail = imapper.mail(mail_id)
        pmails.append(mail.message_id)
        # emails.append(mail)
        # print(mail.from_addr)
        # print(mail.to)
        # print(mail.title)
        # print(mail.body)
        # print(mail.attachments)

    masd = pmails[0]
    easd = emails[0]

    if not (pmails[1] == emails[1]):
        for mail_id in imapper.listids(limit=1):
            mail = imapper.mail(mail_id)
        print()
        print("NEW MESSAGE FROM")
        print(mail.from_addr)
        print()
        print("SUBJECT:")
        print(mail.title)
        print()
        print("BODY:")
        print(mail.body)

        if "jonathan" in mail.from_addr:
            smtpObj.sendmail(login, "jonathan.triplett@studentlaschools.net", ('Subject: %s\ndont email me or my son ever again.' % mail.title))
            print()
            print("Responding with 'dont email me or my son ever again.'")

        if "torsten" in login:
            if "nathanyl" in mail.from_addr:
                smtpObj.sendmail(login, "nathanyl.golden@studentlaschools.net", ("Subject: Re: admins large oof\nHaha that's awesome!"))
                print()
                print("Responding with 'Haha that\'s awesome!'")
                print()

        if "nathanyl" in login:
            if "torsten" in mail.from_addr:
                smtpObj.sendmail(login, "torsten.heavner@studentlaschools.net", ("Subject: Re: admins large oof\nHaha that's awesome!"))
                print()
                print("Responding with 'Haha that\'s awesome!'")
                print()

        emails = pmails

    time2 = datetime.now()
    timel = time2 - time
    print("checked mail in %s seconds." % timel)
