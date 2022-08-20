from bank_functions import Bank

while 1:
    print("***********************")
    print("-----------------------")
    print("welcome")
    print("do you want to create an account or use your existing account")
    print("1 to create account, 2 to use an existing account")
    answer = int(input("response: "))
    if answer == 1:
        banker = Bank()
        banker.create_user()

    elif answer == 2:
        name = input("what is your surname: ")
        password = input("enter your password: ")
        banker = Bank()
        existing_user = banker.check_user_in(name, password)
        if existing_user:
            banker.make_transaction(existing_user)
        else:
            print("not a valid user")
            print("check your surname and password and try again")
