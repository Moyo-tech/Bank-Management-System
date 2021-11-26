from datetime import datetime
from datetime import date
from random import randrange
from secrets import randbelow
import collections
import time

# This function would contain the objects and the operations to open an account.


def screen():
    print("-----------------------------------------------")
    print("Welcome to Dangote's Wellings Bank")
    print("-----------------------------------------------")
    print("1.Create an account \n2.Log in to your acccount \n3.Exit")
    # Takes user input according to the options in integer format
    screen_option = int(input())

   # If user option is 1 then it asks what account the user wants to create and calls the function of creating that account
    if screen_option == 1:
        account_creation_option = input(
            "What account would you like to create (Savings or Current): ")
        # accepts any format of the option the user types in
        if account_creation_option in ["Savings", "savings"]:
            C2 = Savingsaccount()  # this allows us to create the object of the Savings account class, without creating this object we would not be able to run the function of creating savings account
            # calls the create_saving_account function from the savingAccount class
            C2.create_savings_account()

        # accepts any format of the option the user types in
        if account_creation_option in ["Current", "current"]:
            C3 = Currentaccount()  # this allows us to create the object of the currentAccount class, without creating this object we would not be able to run the function of creating current account
            # calls the create_current_account function from the currentAccount class
            C3.create_current_account()

   # If user option is 2 then it asks what account the user wants to login to  and calls the function of logging into that account
    elif screen_option == 2:
        login_option = input(
            "What account would you like to Log_in to (Savings or Current): ")
        if login_option in ["Savings", "savings"]:
            C2 = Savingsaccount()  # we had to create the object again for the same reason as the previous also the previous object was under the if statement and would not show for our function login_savings_account, which is why we had to create it again
            # calls the login_saving_account function from the savingAccount class
            C2.login_savings_account()
        if login_option in ["Current", "current"]:
            C3 = Currentaccount()  # we created another object because the first object was within an if statement and would not be visible to login_current_account()
            C3.login_current_account()

    elif screen_option == 3:
        exit()

    else:
        # incase a user makes a mistake in inputing a value
        print("Please enter the right input value")
        screen()


# Parent class, the parent class contains instance variables Fname, Lname, we set them to be equal to a string because we want to be able to ask for that input and store it, without having to give a positional argument. It also contains 3 methods get Date which gets the month difference between the time the user opned the account and the current time. We also have the exit_bank method which ends the program, and the logout mehtod which allows the user to logout from their account in other to create another account or log in into another account
class Customer:
    def __init__(self, Fname="Please enter your First name:", Lname="Please enter your Last name:"):
        self.Fname = Fname
        self.Lname = Lname

    def getDate(self):
        # collects user input of account creation date
        account_creation_date_entry = input(
            "\nEnter the date you created your account in the format YYYY-MM-DD: ")
        account_creation_date = datetime.strptime(
            account_creation_date_entry, "%Y-%m-%d")  # converts user input to a date format
        present_date = date.today()  # gets the current date

        global month_difference  # We set the month_difference to global because we want to be able to use it in all our program and global allows us to do that
        # calculates the month difference of the present_date from the account_creation _date
        month_difference = (present_date.year - account_creation_date.year) * \
            12 + (present_date.month - account_creation_date.month)
        print(month_difference)

    def exit_bank(self):
        print("Thanks for banking with us, we hope to see you next time. Bye!")
        exit()  # ends the program

    def log_out(self):
        print("You have successfully logged out")
        screen()  # goes back to the screen function which allows the user to create an account or log in into another


# Child class, The child class Savingsaccount contains methods that allows the user to create a savings account, login into their savings account, deposit money, withdraw, and transfer in their savings account. It inherits from the Parent class Customer because it also requires some methods in customer
class Savingsaccount (Customer):
    # we also added new properties that we wanted in the savingsaccount
    def __init__(self, Fname="Please enter your First name:", Lname="Please enter your Last name:", savingsBankdata=collections.defaultdict(dict), savingsBalance=0.00):
        # specifiying that this properties belong to the Parent Class
        super().__init__(Fname, Lname)
        # stores the data of all created accounts and their card details,
        self.savingsBankdata = savingsBankdata
        self.savingsBalance = savingsBalance    # stores the user bank balance

# This methods calculates the interest in the savings account. After 1 months a customer receives an interest of 3%, this method provides the calculation for that
    def interestCalculation(self):
        if month_difference >= 1 and self.savingsBalance > 0:  # this shows that if the month_difference is greater than 1 meaning if the number of months for which the account is greater than one month and the balance in the user account is greater than 0
            # Interest formula = (PRT)/100x12 ; where P stands for the Principal income, R for the interest rate, T for the number of time period
            interest = (self.savingsBalance * 3 *
                        month_difference) / (100 * 12)
            self.savingsBalance += interest  # adds the interest to the current balance
            print(
                f"\n You've earned an interest of ${interest} in your account. Your current balance is ${self.savingsBalance}")
            # calls the function which has a list of operations to perform
            self.operation_to_perform()
        else:
            print("You don't have any interest because you have no money in your account or you haven't reached the interest time limit")
            self.operation_to_perform()

    # function to create savings account
    def create_savings_account(self):
        print("\n")
        # we set the input(self.Fname) to firstname because we want it to store the name given and no longer the string
        firstname = input(self.Fname)
        lastname = input(self.Lname)
        # we set account_name to global because we would like to use it throughout the savingsaccount class
        global account_name
        # formats the input into an account name
        account_name = firstname + " " + lastname

        # generates a random series of numbers that can be used as a cardnumber, the first 400000 stands for the bank IIN then the :010 stands for the numbers that would be generated, all together this would generate a unique 16 digit card number
        card_number = f'400000{randrange ( 1e10 ):010}'
        pin_request = input(
            "Would you like the bank to issue your unique PIN or create your PIN yourself (Issue/Create): ")

        if pin_request == "Issue":
            # generates a unique pin number of 4 digits
            pin_number = f'{randbelow ( 10_000 ):04}'
        elif pin_request == "Create":
            pin_number = input("Enter your desired 4 DIGIT PIN: ")
        else:
            print("Invalid Input please try again")
            self.create_savings_account()

        print(
            f'\nYour card has been created\n ----------SAVINGS ACCOUNT------\nAccount Name:\n{account_name} \nYour card number:\n{card_number}\nYour card PIN:\n{pin_number}')  # Displays the savings account user card information

        # appends the created card to the savingsbankdata , in a nested dictionary format, for easy viewing  this way the user data is stored
        self.savingsBankdata[account_name][card_number] = pin_number
        print(self.savingsBankdata)

        print("\nYou can now log in")
        screen()  # redirects the user to the screen option so they can login

    # function to login into savings account we want the user card details and login details to match so we've created the method as follows
    def login_savings_account(self):
        # since it is a nested dictionary we loop through each key and value, we need the details in the value
        for key, value in self.savingsBankdata.items():
            if isinstance(value, dict):  # checks if dictionary is of type dict
                for card_no, card_pin in value.items():  # decomposes the items in values into 2
                    if key == account_name:  # checks if the key is equal to the acount name
                        global card_login
                        self.getDate()  # redirects to the getdate function
                        # collecting user input
                        card_login = input("Enter your card number: ")
                        pin_login = input("Enter your PIN: ")

                        # checks if the user logindetails matches the card details
                        if card_login == card_no and pin_login == card_pin:
                            print(f'\nYou have successfully logged in')
                            # redirects to the list of operations to perform after logging in
                            self.operation_to_perform()
                        else:
                            print("\n Wrong Card or PIN!")
                            # waits for a little while before recalling the login_savings_account function
                            time.sleep(2)
                            self.login_savings_account()

    # function to deposit into savings account

    def deposit(self):
        # collects user input of the amount to be deposited in int format
        amount = int(input("\nEnter amount to be deposited: "))
        self.savingsBalance += amount  # adds the amount to the user balance
        print(
            f"You depositied ${amount} into your account. Your current balance is ${self.savingsBalance} \n ")
        self.operation_to_perform()

    # function to withdraw from savings account
    def withdraw(self):
        if month_difference >= 6:  # since it is stated that in a savings account the user can only withdraw after 6 months because of the interest condition. This states that if the month difference of the current date and the initial account creation is greater than 6 then the user can withdraw
            amount = int(input("Enter the amount to be withdrawn"))
            if self.savingsBalance >= amount:  # checks if the amount in the bank is withdrawable
                # deducts the amount  from the balance , to show that it has been withdrawn
                self.savingsBalance -= amount
                print(
                    f"You withdrew ${amount} from your account. Your current balance is ${self.savingsBalance} ")
                self.operation_to_perform()
            # if the money in the bank is to small to be withdrawn it throws this error
            print("Insufficient Funds")
            self.operation_to_perform()
        else:
            # if the month difference is not up to 6 months then it throws this messgae
            print(
                "You can only withdraw after 6 months. Please come back later and try again")
            self.operation_to_perform()

# function to view interest
    def view_Interest(self):
        self.interestCalculation()

# function to transfer money to another client
    def transfer(self):
        account_transfer_no = (
            input("Enter Account no to be transferred to: "))  # collects receiver  account number
        # collects receiver account name
        account_name = input("Enter the name of the account: ")

        # checks to see if the number the user inputs of account number is the same as his own
        if account_transfer_no == card_login:
            print("\nYou can't transfer money to your own account")
            self.transfer()
        for key, value in self.savingsBankdata.items():  # loops through the bankdata dictionary
            # to check if value is of type dict so we can iterate through it
            if isinstance(value, dict):
                for card_no, card_pin in value.items():
                    # checks if the key in the dictionary matches the name input and if the account number matches.
                    if key == account_name and account_transfer_no == card_no:
                        amount = int(input("Enter Amount to be transfered: "))
                        if self.savingsBalance >= amount:  # checks if the balance in the account is transferrable
                            # deducts the money to be transferred from the sender's account
                            self.savingsBalance -= amount
                        #   account_name.balance += amount  #adds the money to be transferred to the receiver account
                            print("\n -----------PROCESSING TRANSFER ------------")
                            time.sleep(2)
                            print(
                                f'Successful Transfer to {account_name}. Remaining Balance ${self.savingsBalance}')
                            self.operation_to_perform()
                        else:  # runs if the money is too small to be transferred
                            print("\nNot enough money to transfer")
                            self.operation_to_perform()
                    # if the card input and card details in the bankdata don't match it throws a message
                    elif account_transfer_no != card_no:
                        print(
                            "Such card doesn't exist. Probably you made a mistake in the card try again")
                        self.operation_to_perform()

    # List of operations to perform in savings account
    def operation_to_perform(self):
        print(
            "\nWhat operation would you like to perform\n1.Deposit \n2.Withdrawl\n3.View Interest\n4.Transfer money\n5.Log Out\n6.Exit")
        user_operation_input = int(input())
        if user_operation_input == 1:
            self.deposit()
        elif user_operation_input == 2:
            self.withdraw()
        elif user_operation_input == 3:
            self.view_Interest()
        elif user_operation_input == 4:
            self.transfer()
        elif user_operation_input == 5:
            self.log_out()
        elif user_operation_input == 6:
            self.exit_bank()


# Child class, The child class currentaccount contains methods that allows the user to create a current account, login into their current account, deposit money, withdraw, and transfer in their current account. It inherits from the Parent class Customer because it also requires some methods in customer
class Currentaccount (Customer):
    # Added new properties balance, and bankdata needed in the current account
    def __init__(self, Fname="Please enter your First name:", Lname="Please enter your Last name:", currentBankdata=collections.defaultdict(dict), currentBalance=0.00):
        super().__init__(Fname, Lname)
        # stores the data of all created accounts and their card details,
        self.currentBankdata = currentBankdata
        self.currentBalance = currentBalance     # stores the user bank balance


# This methods calculates the interest in the current account. After 1 months a customer receives an interest of 1%, this method provides the calculation for that


    def currentInterestCalculation(self):
        if month_difference >= 1 and self.currentBalance > 0:  # this shows that if the month_difference is greater than 1 meaning if the number of months for which the account is greater than one month and the balance in the user account is greater than 0
            # Interest formula = (PRT)/100x12 ; where P stands for the Principal income, R for the interest rate, T for the number of time period
            interest = (self.currentBalance * 1 * month_difference)/(100*12)
            self.currentBalance += interest  # adds intest to the current account balance
            print(
                f"You've earned an interest of {interest} in your account. Your current balance is {self.currentBalance}")
            self.operation_to_perform()
        else:
            print("You don't have any interest because you have no money in your account or you haven't reached the interest time limit")
            self.operation_to_perform()

   # function to create current account
    def create_current_account(self):
        print("\n")
        # we set the input(self.Fname) to firstname because we want it to store the name given and no longer the string
        firstname = input(self.Fname)
        lastname = input(self.Lname)
        # we set account_name to global because we would like to use it throughout the savingsaccount class
        global account_name
        # formats the input into an account name
        account_name = firstname + " " + lastname

        # generates a random series of numbers that can be used as a cardnumber, the first 400000 stands for the bank IIN then the :010 stands for the numbers that would be generated, all together this would generate a unique 16 digit card number
        card_number = f'400000{randrange ( 1e10 ):010}'
        pin_request = input(
            "Would you like the bank to issue your unique PIN or create your PIN yourself (Issue/Create): ")

        if pin_request == "Issue":
            # generates a unique pin number of 4 digits
            pin_number = f'{randbelow ( 10_000 ):04}'
        elif pin_request == "Create":
            pin_number = input("Enter your desired 4 DIGIT PIN: ")
        else:
            print("Invalid Input please try again")
            self.create_current_account()

        print(
            f'\nYour card has been created\n --------CURRENT ACCOUNT------\nAccount Name:\n{account_name} \nYour card number:\n{card_number}\nYour card PIN:\n{pin_number}')  # Displays the current account user card information

        # appends the created card to the savingsbankdata , in a nested dictionary format, for easy viewing
        self.currentBankdata[account_name][card_number] = pin_number
        print(self.currentBankdata)
        print("\nYou can now log in")
        screen()  # redirects the user to the screen option so they can login

    # function to login into current account we want the user card details and login details to match so we've created the method as follows

    def login_current_account(self):
        # since it is a nested dictionary we loop through each key and value, we need the details in the value
        for key, value in self.currentBankdata.items():
            if isinstance(value, dict):  # checks if dictionary is of type dict
                for card_no, card_pin in value.items():  # decomposes the items in values into 2
                    if key == account_name:  # checks if the key is equal to the name
                        global card_login
                        self.getDate()                  # redirects to the getdate function
                        # collecting user login details
                        card_login = input("Enter your card number: ")
                        pin_login = input("Enter your PIN: ")

                        # checks if the user logindetails matches the card details
                        if card_login == card_no and pin_login == card_pin:
                            print(f'\nYou have successfully logged in')
                            # redirects to the list of operations to perform after logging in
                            self.operation_to_perform()
                        else:
                            print("\n Wrong Card or PIN!")
                            time.sleep(2)
                            self.login_current_account()

# function to deposit into current account
    def deposit(self):
        # collects user input of amount to be deposited
        amount = int(input("\nEnter amount to be deposited: "))
        self.currentBalance += amount  # adds the amount to the user current account balance
        print(
            f"You depositied ${amount} into your account. Your current balance is {self.currentBalance} \n ")
        self.operation_to_perform()

# function to withdraw from current account
    def withdraw(self):
        # collects user input of amount to be withdrawn
        amount = int(input("Enter the amount to be withdrawn"))
        if self.currentBalance >= amount:  # checks if the amount in the bank is withdrawable
            self.currentBalance -= amount  # deducts amount from the user balance
            print(
                f"You withdrew ${amount} from your account. Your current balance is {self.currentBalance} ")
            self.operation_to_perform()
        else:
            # if the money in the bank is to small to be withdrawn it throws this error
            print("Insuffucient Funds")
            self.operation_to_perform()

# function to transfer money to user
    def transfer(self):
        # collects receiver account number
        account_transfer_no = (
            input("Enter Account no to be transferred to: "))
        # collects the reciver account name
        account_name = input("Enter the name of the account: ")

        # checks to see if the number the user input of account number is the same as his own
        if account_transfer_no == card_login:
            print("\nYou can't transfer money to your own account")
            self.transfer()
        for key, value in self.currentBankdata.items():  # loops through the bankdata dictionary,
            if isinstance(value, dict):
                for card_no, card_pin in value.items():
                    # checks if the key in the dictionary matches the name input and if the account number matches.
                    if key == account_name and account_transfer_no == card_no:
                        amount = int(input("Enter Amount to be transfered: "))
                        if self.currentBalance >= amount:  # checks if the balance in the account is transferrable
                            # deducts the money to be transferred from the sender's account
                            self.currentBalance -= amount
                        #   account_name.savingsBalance += amount    #adds the money to be transferred to the receiver account
                            print("\n -----------PROCESSING TRANSFER ------------")
                            time.sleep(2)
                            print(
                                f'Successful Transfer to {account_name}. Remaining Balance ${self.currentBalance}')
                            self.operation_to_perform()
                        else:
                            print("\nNot enough money to transfer")
                            self.operation_to_perform()
                    elif account_transfer_no != card_no:
                        # if the card input and card details in the bankdata don't match it throws a message
                        print(
                            "Such card doesn't exist. Probably you made a mistake in the card try again")
                        self.operation_to_perform()
# List of operations to perform in savings account

    def operation_to_perform(self):
        print(
            "\nWhat operation would you like to perform\n1.Deposit \n2.Withdrawl\n3.View Interest\n4.Transfer money\n5.Log Out\n6.Exit")
        user_operation_input = int(input())
        if user_operation_input == 1:
            self.deposit()
        elif user_operation_input == 2:
            self.withdraw()
        elif user_operation_input == 3:
            self.currentInterestCalculation()
        elif user_operation_input == 4:
            self.transfer()
        elif user_operation_input == 5:
            self.log_out()
        elif user_operation_input == 6:
            self.exit_bank()


# calls the function that runs the program
screen()
