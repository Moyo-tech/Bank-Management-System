from random import randrange
from secrets import randbelow
import collections
import time

 #Parent class, the parent class contains instance variables Fname, Lname, balance, bankdata we set them to be equal to a string because we want to be able to ask for that input and store it, without having to give a positional argument. It also exit_bank method which ends the program, and the screen which provides a list of options to create an account 
class Customer:
  def __init__(self, Fname="Please enter your First name:", Lname="Please enter your Last name:", balance = 0.00, bankdata=collections.defaultdict(dict)):
      self.Fname = Fname
      self.Lname = Lname
      self.balance = balance
      self.bankdata = bankdata

#list of operations for the user to create an account, or login
  def screen(self):
      print("-----------------------------------------------")
      print("Welcome to Dangote's Wellings Bank")
      print("-----------------------------------------------")
      print("1.Create an account \n2.Log in to your acccount \n3.Exit")
      menu_option = int(input())
      if menu_option == 1:
          Accounts.create_account(self)  #a way of calling the accounts class method, if the user input is  1
      if menu_option == 2: 
          Accounts.log_in(self)        #calls the account login mehtod if the user input is 2 
      if menu_option == 3:
          self.exit_bank()
      else:
          print("Please enter the right input value")
          self.screen()

  def exit_bank(self):
      print("Thanks for banking with us, we hope to see you next time. Bye!")
      exit()


#Child class, The child class Account contains methods that allows the user to create an account, login into their account, and log out It inherits from the Parent class Customer because it also requires some methods in parent class and some properties 

class Accounts(Customer):
  def __init__(self, Fname, Lname):
      super().__init__(Fname, Lname)  #inheritance 

  def create_account(self):
      print("\n")
      firstname = input(self.Fname) #we set the input(self.Fname) to firstname because we want it to store the name given and no longer the string 
      lastname = input(self.Lname) 
      global account_name     #we set account_name to global because we would like to use it throughout the program
      account_name = firstname + " " + lastname #formats the input into an account name 

      card_number = f'400000{randrange(1e10):010}'#generates a random series of numbers that can be used as a cardnumber, the first 400000 stands for the bank IIN then the :010 stands for the numbers that would be generated, all together this would generate a unique 16 digit card number 
      pin_request = input(
          "Would you like the bank to issue your unique PIN or create your PIN yourself (Issue/Create): ")

      if pin_request == "Issue":
          pin_number = f'{randbelow(10_000):04}'   #generates a unique pin number of 4 digits
      elif pin_request == "Create":
          pin_number = input("Enter your desired 4 DIGIT PIN: ")
      else:
          print("Invalid Input please try again")
          self.create_account()

      print(
          f'\nYour card has been created\nAccount Name:\n{account_name} \nYour card number:\n{card_number}\nYour card PIN:\n{pin_number}') #Displays the  user card information 

      self.bankdata[account_name][card_number] = pin_number #appends the created card to the savingsbankdata , in a nested dictionary format, for easy viewing, this way the user data is stored 
      print(self.bankdata)
      print("\nYou can now log in")
      self.screen()  #redirects the user to the screen method so they can login 


# function to login into the account we want the user card details and login details to match so we've created the method as follow
  def log_in(self):
      for key, value in self.bankdata.items(): #since it is a nested dictionary we loop through each key and value, we need the details in the value 
          if isinstance(value, dict):    #checks if dictionary is of type dict 
              for card_no, card_pin in value.items(): #decomposes the items in values into 2
                  if key == account_name:                #checks if the key is equal to the name 
                      global card_login
                      card_login = input("Enter your card number: ")    #collecting user input
                      pin_login = input("Enter your PIN: ")

                      if card_login == card_no and pin_login == card_pin: #checks if the user logindetails matches the card details 
                          print(f'\nYou have successfully logged in')
                          Bankingsystem.operation_to_perform(self)  #redirects to the list of operations to perform after logging in
                      else:
                          print("\n Wrong Card or PIN!")
                          time.sleep(2)      #waits for a little while before recalling the screen method
                          self.screen()

#function to logout of the account
  def log_out(self):
      print("You have successfully logged out")
      self.screen()   #goes back to the screen function which allows the user to create an account or log in again 


#Child class, The child class Bankingsystem contains methods that allows the user to deposit money, withdraw, transfer and view balance.  It inherits from the Parent class Customer because it also requires some methods in customer 
class Bankingsystem(Customer):
  def __init__(self, Fname, Lname, email, balance, bankdata):
      super().__init__(Fname, Lname, email, balance, bankdata)  #properties of the child class

#operations available to perform in the program 
  def operation_to_perform(self):
      print("\nWhat operation would you like to perform\n1.Deposit \n2.Withdrawl\n3.View balance\n4.Transfer money\n5.Log Out\n6.Exit")
      user_operation_input = int(input())
      if user_operation_input == 1:
          Bankingsystem.deposit(self)
      elif user_operation_input == 2:
          Bankingsystem.withdraw(self)
      elif user_operation_input == 3:
          Bankingsystem.balance_details(self)
      elif user_operation_input == 4:
          Bankingsystem.transfer(self)
      elif user_operation_input == 5:
          Accounts.log_out(self)
      elif user_operation_input == 6:
          self.exit_bank()

#function to deposit 
  def deposit(self):
      amount = int(input("\nEnter amount to be deposited: ")) #collects user input of amount to be deposited 
      self.balance += amount #adds the amount to the user current account balance 
      print(
          f"You depositied ${amount} into your account. Your current balance is ${self.balance} \n ")
      Bankingsystem.operation_to_perform(self)

  def withdraw(self):
      amount = int(input("Enter the amount to be withdrawn")) #collects user input of amount to be withdrawn
      if self.balance >= amount: #checks if the amount in the bank is withdrawable
          self.balance -= amount  #deducts amount from the user balance 
          print(f"You withdrew ${amount} from your account. Your current balance is ${self.balance} ")
          Bankingsystem.operation_to_perform(self)
      else:
          print("Insufficient Funds")    #if the money in the bank is to small to be withdrawn it throws this error 
          Bankingsystem.operation_to_perform(self)
      
#function to show balance details 
  def balance_details(self):
      print(f"Balance in the account is ${self.balance}")
      
      Bankingsystem.operation_to_perform(self)

#function to transfer money amongst other clients 
  def transfer(self):
      account_transfer_no = (
          input("Enter Account no to be transferred to: "))     #collects user account number 
      account_name = input("Enter the name of the account: ")   #collects the reciver account name

      if account_transfer_no == card_login:                     #checks to see if the number the user input of account number is the same as his own 
          print("\nYou can't transfer money to your own account")
          Bankingsystem.transfer(self)
      for key, value in self.bankdata.items():                      #loops through the bankdata dictionary
          if isinstance(value, dict):                              #to check if value is of type dict so we can iterate through it
              for card_no, card_pin in value.items():
                  if key == account_name and account_transfer_no == card_no:  #checks if the key in the dictionary matches the name input and if the account number matches.
                      amount = int(input("Enter Amount to be transfered: "))
                      if self.balance >= amount:                        #checks if the balance in the account is transferrable 
                          self.balance -= amount               #deducts the money to be transferred from the sender's account
                        #   account_name.balance += amount     #adds the money to be transferred to the receiver account 
                          print("\n -----------PROCESSING TRANSFER ------------")
                          time.sleep(2)
                          print(f'Successful Transfer to {account_name}. Remaining Balance ${self.balance}')
                          Bankingsystem.operation_to_perform(self)
                      else:       #runs if the money is too small to be transferred
                          print("\nNot enough money to transfer")
                          self.operation_to_perform()
                  elif account_transfer_no != card_no:  #if the card input and card details in the bankdata don't match it throws a message
                      print(
                          "Such card doesn't exist. Probably you made a mistake in the card try again")
                      Bankingsystem.operation_to_perform(self)


#object of the class customer 
C1 = Customer()
C1.screen()    #calling the method screen

