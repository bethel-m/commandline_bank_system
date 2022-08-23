import random
import maskpass
from user_functions import User
users = []
# creates a bank class


class Bank:
    # collects users information, generate a unique account number and creates a user instance by calling the User class
    # stores the instance in the users list
    def create_user(self):
        print("welcome, what is your name")
        surname = input("surname: ")
        while (len(surname) <= 0):
            print("please enter a valid name")
        first_name = input("firstname: ")
        while (len(first_name) <= 0):
            print("please enter a valid name")

        print("create a password please-(use left ctrl on your keyboard to toggle visibility) ")
        password = maskpass.advpass()
        acc_no = self.generate_account_number()
        print(f"your account number is: {acc_no}")
        # while acc_no in users:
        #    acc_no = self.generate_account_number()
        #    print(acc_no)

        print("create a transaction pin (use left ctrl on your keyboard to toggle visibility)")
        pin = maskpass.advpass(prompt="enter a pin :")
        new_user = User(surname, first_name, acc_no, password, pin)
        users.append(new_user)

    # checks if the user exists in the users lists
    # returns the user instance if the user exists and false if the user does not exist

    def check_user_in(self):
        name = input("what is your surname: ")
        print("use the left ctrl on your keyboard to toggle visibility")
        password = maskpass.advpass(prompt="enter your password: ")
        for i in range(len(users)):
            if ((users[i].surname == name) and (users[i].password == password)):
                print('user available')
                return users[i]
        print("user not available")
        return False

    def delete_user():
        pass

    # generates a 10 digit random number
    def generate_account_number(self):
        start_index = 1000000000
        end_index = 9999999999
        number = random.randint(start_index, end_index)
        return number

    # calls a User method according to perform a transaction according to the user input

    def make_transaction(self, user):
        print("what transaction do you want to perform")
        print("1:account details 2:deposit 3:withdraw 4:send money")

        transaction = int(input("response: "))
        if transaction == 1:
            user.account_details()
        elif transaction == 2:
            amount = float(input("how much deposit: "))
            user.deposit(amount)
        elif transaction == 3:
            amount = float(input("how much to withdraw: "))
            user.withdraw(amount)
        elif transaction == 4:
            amount = float(input("amount to send: "))
            account_no = int(input("recipient account number: "))
            user.send_money(amount, account_no, users)
        else:
            print("invalid input")
