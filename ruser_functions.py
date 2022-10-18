import maskpass

class User:
    def __init__(self, surname, first_name,email, account_number, password, pin, balance=0):
        self.surname = surname
        self.first_name = first_name
        self.email = email 
        self.account_number = account_number
        self.balance = balance
        self.fullname = surname + ' ' + first_name
        self.password = password
        self.pin = pin

    def deposit(self,amount):
        if amount <= 0 :
            raise ValueError
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if self.balance < amount:
            return "insufficient funds"
        elif amount <= 0 :
            raise ValueError
        self.balance -= amount
        return self.balance

    def get_account_details(self):
        return [self.fullname,self.account_number,self.balance]

    def confirm_transaction(self,pin):
        if pin == self.pin:
            return True
        return False

    def send_money(self,amount,user):
        if self.balance < amount:
            return "insufficient funds"
        elif amount <= 0:
            raise ValueError
        self.balance -= amount
        user.balance += amount
        return "money sent"
