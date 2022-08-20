

class User:
    def __init__(self, surname, first_name, account_number, password, pin, balance=0):
        self.surname = surname
        self.first_name = first_name
        self.account_number = account_number
        self.balance = balance
        self.fullname = surname + ' ' + first_name
        self.password = password
        self.pin = pin

    # shows the account details of the user

    def account_details(self):
        proceed = self.confirm_transaction()
        if proceed:
            print(self.fullname)
            print(self.account_number)
            print(self.balance)
        else:
            print("incorect transaction pin")
    # allows the user to withdraw if the user has a balance greater than 0

    def withdraw(self, amount):
        if amount < 0:
            print("sorry enter an amount greater than $0")
        elif amount > self.balance:
            print("sorry insufficient fund")
        else:
            # proceed contains a bool true if the pin is correct and false otherwise
            proceed = self.confirm_transaction()
            if proceed:
                self.balance -= amount
                print("you withdrew $" + str(amount))
                print("your balance is $" + str(self.balance))
            else:
                print("incorrect transaction pin")

    # enables the user deposit money in the account
    def deposit(self, amount):
        if amount < 0:
            print("deposit only amounts greater than $0")
        else:
            self.balance += amount
            print("you deposited $" + str(amount))
            print("your new balance is $" + str(self.balance))

    def confirm_transaction(self):
        print("enter your transaction pin")
        pin = int(input("pin: "))
        if self.pin == pin:
            return True
        else:
            return False

    def send_money(self, amount, account_no, users):
        for i in users:
            if i.account_number == account_no:
                print(f"continue transaction to {i.fullname}")
                print("1:yes  2:NO")
                response = int(input("response: "))
                if response == 1:
                    print("Executing**")
                    proceed = self.confirm_transaction()
                    if proceed:
                        if amount > self.balance:
                            print("insufficient balance")
                        else:
                            self.balance -= amount
                            i.balance += amount
                            print(f"you sent {amount} to {i.fullname}")
                            print(f"your balance is {self.balance}")
                    else:
                        print("incorrect pin")
