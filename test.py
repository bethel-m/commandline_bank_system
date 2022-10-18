from collections import UserString
import unittest
from rbank_functions import Bank
from ruser_functions import User

class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

        # user1 details
        surname = 'Joe'
        first_name = 'Paul'
        email = 'paul@gmail.com'
        account_number=12345
        password = 'abcdefgh'
        pin=1234
        self.fullname = surname + ' ' + first_name
        self.user1 = Bank.create_user(surname,first_name,email,account_number,password,pin)

        #user2 details
        self.user2 = Bank.create_user("mike","towsend",'mike@gmail.com',231212,"asdfasdf",9090)
        self.user2.balance = 200

        #list of users
        self.users = [self.user1,self.user2]

        # user_functions tests

        #test that the user exists with correct informations
    def test_user_exists(self):
        self.assertTrue(self.user1) #test user exists
        self.assertIsInstance(self.user1,User) 
        self.assertEqual(self.user1.first_name,'Paul')
        self.assertEqual(self.user1.surname,'Joe')
        self.assertEqual(self.user1.email,'paul@gmail.com')
        self.assertEqual(self.user1.account_number,12345)
        self.assertEqual(self.user1.password,'abcdefgh')
        self.assertEqual(self.user1.pin,1234)
        self.assertEqual(self.user1.balance,0)
    
    # tests that deposit method works  
    def test_deposit(self):   
        self.assertEqual(self.user1.deposit(300),self.user1.balance,300)
        self.assertEqual(self.user1.balance,300)

    # tests that deposit method does not accept wrong entries
    def test_cannot_deposit_negative_amount_or_zero(self):
        with self.assertRaises(ValueError): # test for depositing negative numbers
            self.user1.deposit(-23)
        with self.assertRaises(ValueError): # test for depositing zero
            self.user1.deposit(0)

    # tests that withdraw method works 
    def test_withdraw(self):
        self.assertEqual(self.user2.withdraw(50),150)
        self.assertEqual(self.user2.balance,150) #checks balance
    

    # tests that the withdraw method does not accepts wrong entries
    def test_illegal_withdrawals(self):
        self.assertEqual(self.user1.withdraw(50),"insufficient funds") #withdrawing more than the users balance
        with self.assertRaises(ValueError): # withdrawing zero
            self.user2.withdraw(0)
        with self.assertRaises(ValueError): #withdrawing a negative number
            self.user2.withdraw(-23)

    # Tests that the user account details are correct
    def test_account_details(self):
        self.assertEqual(self.user2.get_account_details(),["mike towsend",231212,200])

    # tests that send_money method works ,and it sends money, given an amount(positive number) and
    # and a user instance, by incrementing the user instances balance by the amount
    def test_send_money(self):
        self.assertEqual(self.user2.send_money(50,self.user1),"money sent") # correct entries
        self.assertEqual(self.user1.balance,50)                             # check balance
        self.assertEqual(self.user2.send_money(500,self.user1),"insufficient funds") 
        with self.assertRaises(ValueError): #send negative amount
            self.user2.send_money(-40,self.user1)
        with self.assertRaises(ValueError): #send money
            self.user2.send_money(0,self.user1)

    # bank_functions tests

    # test the confirm_transaction method validates only correct pin for the users
    # who want to perform transaction
    def test_confirm_transaction(self):
        self.assertTrue(self.user1.confirm_transaction(1234)) #correct pin
        self.assertFalse(self.user1.confirm_transaction(9999)) # wrong pin
    

    # tests that the find_user method finds a user given an account number and the list of users
    def test_find_user(self):
        self.assertEqual(self.bank.find_user(12345,self.users),self.user1)
        self.assertEqual(self.bank.find_user(87653,self.users),"user does not exist")

    
    # tests that log_user_in method works
    # uses email and password and compares it to the list of users 
    def test_log_user_in(self):
        self.assertTrue(self.bank.log_user_in("paul@gmail.com","abcdefgh",self.users)) # correct email and password
        self.assertFalse(self.bank.log_user_in("unknown@gmail.com","abcdefgh",self.users)) # wrong email and correct password
        self.assertFalse(self.bank.log_user_in("paul@gmail.com","wrong_password",self.users)) # correct email and wrong password
        self.assertFalse(self.bank.log_user_in("unknown@gmail.com","wrong_password",self.users)) # wrong email and password

    # tests that delete_user method works
    # uses user instance and compares it to the users list, if match is found
    # the user is deleted
    def test_delete_user(self):
        self.assertEqual(self.bank.delete_user(self.user1,self.users),"user deleted") #passing a user instance
        self.assertTrue(self.user1 not in self.users) # confirming that user is removed from the list of users


    # tests for main.py file
    


if __name__=="__main__":
    unittest.main()