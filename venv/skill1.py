'''

Banking System using OOP
Parent Class  : User  --> Holds details about user ,  has a function to show show_user_details

Child class  : Bank --> Stores details about the account balance, amount, and allows fpr deposits, withdraw and veiw balance

'''
class User():
    def __init__(self,name,age,gender,phno,mail):
        self.name=name
        self.age=age
        self.gender=gender
        self.phno=phno
        self.mail=mail
    def show_details(self):
        print("Personal Details:\n")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Phone Number:",self.phno)
        print("Email:",self.mail)

#Creating Child Class
class Bank(User):
    def __init__(self,name,age,gender,phno,mail):
        super().__init__(name,age,gender,phno,mail)
        self.balance = 0
    def deposit(self,amount):
        print('You have deposited',amount,'Sucessfully')
        self.balance = self.balance + amount
        print('Account Balance has been updated:',self.balance)
    def withdraw(self,amount):
        if self.balance >= amount:
            print("Your withdrawal amount",amount," has been successful")
            self.balance = self.balance - amount
            print("Your balance:",self.balance)
        else:
            print("You have insuffitient amount")
    def viewbalance(self):
        self.show_details()
        print("Your balance:", self.balance)

class MobileBank(User):
    def __init__(self,name,age,gender,phno,mail):
        super().__init__(name,age,gender,phno,mail)
        self.balance = 0
    def deposit(self,amount):
        print('You have deposited',amount,'Sucessfully')
        self.balance = self.balance + amount
        print('Account Balance has been updated:',self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Your withdrawal amount", amount, " has been successful")
            self.balance = self.balance - amount
            print("Your balance:", self.balance)
        else:
            print("You have insuffitient amount")

    def viewbalance(self):
        self.show_details()
        print("Your balance:", self.balance)


class InternetBank(User):
    def __init__(self,name,age,gender,phno,mail):
        super().__init__(name,age,gender,phno,mail)
        self.balance = 0


    def deposit(self,amount):
        print('You have deposited',amount,'Sucessfully')
        self.balance = self.balance + amount
        print('Account Balance has been updated:',self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Your withdrawal amount", amount, " has been successful")
            self.balance = self.balance - amount
            print("Your balance:", self.balance)
        else:
            print("You have insuffitient amount")

    def viewbalance(self):
        self.show_details()
        print("Your balance:", self.balance)


def AddUsers():

    global ba
    global mba
    global iba

    while True:
        n = int(input("Do you want to create an :\n1.Bank Account\n2.Mobile Bank Account\n3.Internet Bank Account\nEnter any other number to exit:"))
        #n = int(input("Are you willing to add a user?\n1.Yes\n2.No\n"))
        if n!=1 and  n!=2 and n!=3:
            break
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender:")
        if n==1:
            ba.append(Bank(name, age, gender, None, None))
        elif n==2:
            no = int(input("Mobile Number: "))
            mba.append(MobileBank(name, age, gender, no, None))
        elif n==3:
            no = int(input("Mobile Number: "))
            mail = input("Email ID: ")
            iba.append(InternetBank(name, age, gender, no, mail))


def DO():

    global ba
    global mba
    global iba

    while True:
        n = int(input("Are you willing to Display the bank details:\n1.Yes\n2.No\n"))
        if n ==1:
            b = int(input("Select the bank\n1.Ordinary Bank Account\n2.Mobile Bank Account\n3.Internet Bank Account\nEnter any other number to exit"))
            if b==1:
                for i in ba:
                    i.viewbalance()
                    print("\n---------------------------------------------------------------\n")
            elif b==2:
                for i in mba:
                    i.viewbalance()
                    print("\n---------------------------------------------------------------\n")
            elif b==3:
                for i in iba:
                    i.viewbalance()
                    print("\n---------------------------------------------------------------\n")

        while True:
            n = int(input("What do you what to do:\n1.Deposit Amount\n2.WithDraw Amount\n3.View Balance\nenter any other number to exit"))
            if n != 1 and n != 2 and n != 3:
                break
            #for deposit
            if n==1:
                b = int(input("Select the bank\n1.Ordinary Bank Account\n2.Mobile Bank Account\n3.Internet Bank Account\nEnter any other number to exit"))
                if b == 1:
                    while True:
                        name = input("Enter name:")
                        flag =0
                        for i in ba:
                            if name == i.name:
                                amt = int(input("Enter the amount that you wat to deposit:"))
                                i.deposit(amt)
                                flag =1
                        if flag == 0:
                            print("Invalid Name!")
                            n= int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
                elif b==2:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        flag = 0
                        for i in mba:
                            if name == i.name and no == i.phno:
                                amt = int(input("Enter the amount that you wat to deposit:"))
                                i.deposit(amt)
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
                elif b==3:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        mail = input("Enter MailID:")
                        flag = 0
                        for i in iba:
                            if name == i.name and no == i.phno and mail == i.mail:
                                amt = int(input("Enter the amount that you wat to deposit:"))
                                i.deposit(amt)
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
            # for WithDraw
            if n == 2 :
                b = int(input("Select the bank\n1.Ordinary Bank Account\n2.Mobile Bank Account\n3.Internet Bank Account\nEnter any other number to exit"))
                if b == 1:
                    while True:
                        name = input("Enter name:")
                        flag =0
                        for i in ba:
                            if name == i.name:
                                amt = int(input("Enter the amount that you wat to deposit:"))
                                i.withdraw(amt)
                                flag =1
                        if flag == 0:
                            print("Invalid Name!")
                            amt = int(input("Enter the amount that you want to Withdraw:"))
                            if n == 2:
                                break
                        else:
                            break
                elif b==2:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        flag = 0
                        for i in mba:
                            if name == i.name and no == i.phno:
                                amt = int(input("Enter the amount that you want to Withdraw:"))
                                i.withdraw(amt)
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
                elif b==3:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        mail = input("Enter MailID:")
                        flag = 0
                        for i in iba:
                            if name == i.name and no == i.phno and mail == i.mail:
                                amt = int(input("Enter the amount that you want to Withdraw:"))
                                i.withdraw(amt)
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
            # for viewbalance
            if n == 3:
                b = int(input("Select the bank\n1.Ordinary Bank Account\n2.Mobile Bank Account\n3.Internet Bank Account\nEnter any other number to exit"))
                if b == 1:
                    while True:
                        name = input("Enter name:")
                        flag = 0
                        for i in ba:
                            if name == i.name:

                                i.viewbalance()
                                flag = 1
                        if flag == 0:
                            print("Invalid Name!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
                elif b == 2:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        flag = 0
                        for i in mba:
                            if name == i.name and no == i.phno:

                                i.viewbalance()
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break
                elif b == 3:
                    while True:
                        name = input("Enter name:")
                        no = int(input("Enter Mobile number:"))
                        mail = input("Enter MailID:")
                        flag = 0
                        for i in iba:
                            if name == i.name and no == i.phno and mail == i.mail:

                                i.viewbalance()
                                flag = 1
                        if flag == 0:
                            print("Invalid Credintials!")
                            n = int(input("Do you want to try again:\n1.Yes\n2.No\n"))
                            if n == 2:
                                break
                        else:
                            break

        n = int(input("Do you want to exit\n1.Yes\n2.No\n"))
        if n==1:
            break






ba = []
mba = []
iba = []

n = int(input("Are you willing to create a Bank account?\n1.Yes\n2.No\n"))
if n == 1:
    AddUsers()

n = int(input("Are you willing to display the user accounts or perform any other operations?\n1.Yes\n2.No\n"))
if n==1:
    DO()

