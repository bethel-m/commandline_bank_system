import random
import maskpass
from ruser_functions import User
users = []
# creates a bank class


class Bank:
    def create_user(surname, first_name, acc_no,email, password, pin):
        user = User(surname, first_name, acc_no,email, password, pin)
        return user 
    def generate_account_number(self):
        print("generating account number .....")
        start_index = 1000000000
        end_index = 9999999999
        number = random.randint(start_index, end_index)
        return number

    def get_user_info(self):
        print("please answer the following questions")
        print("what is your surname")
        surname = input("surname::")
        print("what is your first name")
        first_name = input("first name::")
        print("enter your email address")
        email = input("email::")
        
    def find_user(self,acc_num,users_list):
        for user in users_list:
            if user.account_number == acc_num:
                return user
        return "user does not exist"

    def log_user_in(self,email,password,users_list):
        for i in users_list:
            if i.email == email and i.password == password:
               return True
        return False

    def delete_user(self,user,users_list):
        for i in users_list:
            if i == user:
                users_list.remove(user)
            return "user deleted"


        
             
