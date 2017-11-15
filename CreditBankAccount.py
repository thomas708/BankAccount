#!/usr/bin/python3
###########################################################
# CreditBankAccount's balance is allowed to go below 0
###########################################################

# Importing the "BankAccount" class
# Format is: from <file name without .py> import <class name>
from BankAccount import BankAccount

# CreditBankAccount inherits from BankAccount
# Put the parent classes inside the parentheses
class CreditBankAccount(BankAccount):

    # Constructor
    def __init__(self, owner, balance):
        print("Creating CreditBankAccount")
        # Invoking the parent's constructor
        # The "super()" finds the correct parent
        # If multiple inheritance put the parent name
        # inside the parentheses of super()
        super().__init__(owner, balance)

    # Destructor
    def __del__(self):
        # The "self.__class__.__name__" dynamically gets the name
        # of the class at runtime, in this case "CreditBankAccount"
        print("Destroying " + self.__class__.__name__)

    # Withdraw money
    # This overrides the "withdraw(self, amount)" method in parent
    def withdraw(self, amount):
        # Note that "__balance" variable in parent is private so
        # cannot manipulate it directly. Must use public get() and
        # set() methods provided by parent
        super().setBalance(super().getBalance() - amount)

    
