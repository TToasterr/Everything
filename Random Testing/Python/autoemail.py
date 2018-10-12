import sys
import easyimap
import smtplib
from datetime import datetime

time = datetime.now()
login = sys.argv[1]
password = sys.argv[2]
emails = []
pmails = []
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login,password)
time2 = datetime.now()
timel = time2 - time
print("logged in in %s seconds." % timel)

time = datetime.now()
imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=1000):
    mail = imapper.mail(mail_id)
    emails.append(mail)
    # print(mail.from_addr)
    # print(mail.to)
    # print(mail.title)
    # print(mail.body)
    # print(mail.attachments)

time2 = datetime.now()
timel = time2 - time
print("got emails in %s seconds." % timel)
print("Running!")

while 1:
    pmails = []
    emailamount = len(emails)
    pmailamount = len(pmails)

    time = datetime.now()
    for mail_id in imapper.listids(limit=500):
        mail = imapper.mail(mail_id)
        pmails.append(mail)

        pmailamount = len(pmails)

    time2 = datetime.now()
    timel = time2 - time
    print("got emails in %s seconds." % timel)

    if not pmailamount == emailamount:
        aaa = pmails[0]
        print()
        print("NEW MESSAGE FROM")
        print(aaa.from_addr)
        print()
        print()
        print("SUBJECT:")
        print(aaa.title)
        print()
        print("BODY:")
        print(aaa.body)

        if aaa.from_addr == "JONATHAN TRIPLETT <jonathan.triplett@studentlaschools.net>":
            smtpObj.sendmail(login, "jonathan.triplett@studentlaschools.net", ('Subject: %s\ndont email me or my son ever again.' % aaa.title))

        if "nathanyl" in aaa.from_addr:
            smtpObj.sendmail(login, "nathanyl.golden@studentlaschools.net", ("Subject: Re: admins large oof\nHaha that's awesome!"))

        if "torsten" in aaa.from_addr:
            smtpObj.sendmail(login, "torsten.heavner@studentlaschools.net", ("Subject: Re: admins large oof\nHaha that's awesome!"))

        emails = pmails
        print("Email amount:")
        print(len(emails))
