from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
from datetime import datetime
import gspread
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
p = pprint.PrettyPrinter()

sheet = client.open("Torsten Allowance").sheet1
temp1 = sheet.col_values(1)
date = str(datetime.now().date()).replace("-", "/").split("/")
today = datetime.now().strftime("%A")
date.append(date[0])
del date[0]

date = "/".join(date)
date = date.split("/")
date[0] = int(date[0])
date[1] = int(date[1])
date[2] = int(date[2])

if today == "Sunday":
    date[1] -= 1
elif today == "Monday":
    date[1] -= 2
elif today == "Tuesday":
    date[1] -= 3
elif today == "Wednesday":
    date[1] -= 4
elif today == "Thursday":
    date[1] -= 5
elif today == "Friday":
    date[1] -= 6

date[0] = str(date[0])
date[1] = str(date[1])
date[2] = str(date[2])
date = "/".join(date)

row = temp1.index(date) + 1
print("\nLast Week:")
print(sheet.cell(row - 1, 5).value)
print("\nCurrent:")
print(sheet.cell(row, 5).value)
print("\nNext Week:")
print(sheet.cell(row + 1, 5).value + "\n")

for i in range(5):
    print(sheet.cell(row + (i + 2), 5).value)

print("\n----------------------------\n\nIncome this week:")
print("$" + str(float(sheet.cell(row + 1, 5).value[1:].replace(",", "")) - float(sheet.cell(row, 5).value[1:].replace(",", ""))))
print("\nIncome next week:")
print("$" + str(float(sheet.cell(row + 2, 5).value[1:].replace(",", "")) - float(sheet.cell(row + 1, 5).value[1:].replace(",", ""))) + "\n")

for i in range(5):
    print("$" + str(float(sheet.cell(row + (i + 3), 5).value[1:].replace(",", "")) - float(sheet.cell(row + (i + 2), 5).value[1:].replace(",", ""))))

# money = []
# numbe = []
#
# for i in range(100):
#     money.append(float(sheet.cell(13+i, 5).value[1:].replace(",", "")))
#     numbe.append(i+1)
#
# plt.plot(numbe, money)
# plt.show()
