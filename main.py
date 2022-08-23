from bank_functions import Bank
print("***********************")
print("-----------------------")
print("welcome")
print("do you want to create an account or use your existing account")

while 1:
    print("################################")
    print("perform a transaction")
    print("1 to create account, 2 to use an existing account , 3 to quit")
    answer = int(input("response: "))
    if answer == 1:
        banker = Bank()
        banker.create_user()

    elif answer == 2:

        banker = Bank()
        existing_user = banker.check_user_in()
        if existing_user:
            banker.make_transaction(existing_user)
        else:
            print("not a valid user")
            print("check your surname and password and try again")
    elif answer == 3:
        exit()
    else:
        print("invalid response,please respond again")