import time, math
format = "\n"*50
i = -1
accList = []

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.bal = balance

    def printAccount(self):
        print("Account: ", self.name)
        print("Balance: ", self.bal)
        print("---------------------------")

def interest():
    if i > -1:
        for item in accList:
            accList[i].bal += (accList[i].bal*0.05)

def exist():
    global accList
    global i

    inp = input("What would you like to do? \nInput 'list commands' for help. \n")

    if inp == "list commands":
        print(format)
        print("Commands: \nlist commands - lists commands \nlist accounts - lists all current accounts \nadd account - adds an account \nremove account - removes an account \ndeposit - deposits money to an account \nwithdraw - withdraws money from an account \n")
        exist()

    elif inp == "exist()":
        print(format)
        print("I dont wanna xd \nbut fine \n")
        interest()
        exist()

    elif inp == "list accounts":
        print(format)
        if accList == []:
            print("You don't have any accounts yet! \n")
            interest()
            exist()

        else:
            xd = 0
            while xd < len(accList):
                print(xd, ":")
                accList[xd].printAccount()
                xd += 1
            interest()
            exist()

    elif inp == "add account":
        print(format)
        accName = input("What would you like the account name to be? \n")
        print(format)
        try:
            accBal = int(input("What is the accounts balance? \n"))
        except:
            print(format)
            print("That isnt a correct balance! Please make sure to input a number. \n")
            interest()
            exist()
            return

        i += 1
        accList.append(Account(accName, accBal))
        print(format)
        accList[i].printAccount()
        interest()
        exist()

    elif inp == "remove account":
        def removeAcc():
            global i
            accList.pop(int(whichAcc))
            i -= 1
            interest()
            exist()

        print(format)
        whichAcc = input("Which account would you like to remove? \nPlease input as a number. \nInput 'list accounts' to list accounts. \n")
        if whichAcc == "list accounts":
            print(format)

            if accList == []:
                print("You don't have any accounts yet! \n")
                interest()
                exist()

            else:
                xd = 0
                while xd < len(accList):
                    print(xd, ":")
                    accList[xd].printAccount()
                    xd += 1
                interest()
                exist()
        else:
            print(format)
            try:
                accList[int(whichAcc)].printAccount

            except:
                print("That account doesnt exist! Do 'list accounts to list your accounts.")
                interest()
                exist()
                return

            removeAcc()

    elif inp == "deposit":
        def howMuch():
            howMuch = input("How much would you like to deposit? \n")
            accList[int(whichAcc)].bal += int(howMuch)
            print(format)
            accList[int(whichAcc)].printAccount()
            interest()
            exist()

        print(format)
        whichAcc = input("Which account would you like to deposit to? \nInput as a number. \nInput 'list accounts' for a list of accounts. \n")
        if whichAcc == "list accounts":
            print(format)

            if accList == []:
                print("You don't have any accounts yet! \n")
                interest()
                exist()

            else:
                xd = 0
                while xd < len(accList):
                    print(xd, ":")
                    accList[xd].printAccount()
                    xd += 1
                interest()
                exist()

        else:
            print(format)
            try:
                accList[int(whichAcc)].printAccount()

            except:
                print("That account doesnt exist! Do 'list accounts' to list your accounts. \n")
                interest()
                exist()
                return

            howMuch()

    elif inp == "withdraw":
        def howMuch():
            howMuch = input("How much do you want to withdraw? \n")
            accList[int(whichAcc)].bal -= int(howMuch)
            print(format)
            accList[int(whichAcc)].printAccount()
            interest()
            exist()

        print(format)
        whichAcc = input("Which account would you like to withdraw from? \nInput as a number. \nInput 'list accounts' for a list of accounts. \n")
        if whichAcc == "list accounts":
            print(format)

            if accList == []:
                print("You don't have any accounts yet! \n")
                interest()
                exist()

            else:
                xd = 0
                while xd < len(accList):
                    print(xd, ":")
                    accList[xd].printAccount()
                    xd += 1
                interest()
                exist()

        else:
            print(format)
            try:
                accList[int(whichAcc)].printAccount()

            except:
                print("That account doesn't exist! Do 'list accounts' to list your accounts. \n")
                interest()
                exist()
                return

            howMuch()
    
    else:
        print(format)
        print("That command doesn't exist! Please try again. \n")
        interest()
        exist()

print(format)
exist()
