#!/usr/bin/python3
#########################################################
# JointBankAccount has two owners instead of one
#########################################################

# Importing the "BankAccount" class
# Format is: from <file name without .py> import <class name>
from BankAccount import BankAccount

# JointBankAccount inherits from BankAccount
# Put the parent classes inside the parentheses
class JointBankAccount(BankAccount):

    # Constructor
    def __init__(self, owner1, owner2, balance):
        print("Creating JointBankAccount")
        # Invoking the parent's constructor
        # The "super()" finds the correct parent
        # If multiple inheritance put the parent name
        # inside the parentheses of super()
        super().__init__(owner1, balance)
        # Defining variables only in child class
        self.owner2 = owner2

    # Destructor
    def __del__(self):
        # The "self.__class__.__name__" dynamically gets the name
        # of the class at runtime, in this case "JointBankAccount"
        print("Destroying " + self.__class__.__name__)

    # Print account
    # This overrides the "toString(self)" function in parent
    def toString(self):
        # Note: to call parent's method need to add "super()." in
        # front of method's name
        return "Owners: " + self.owner + ", " + self.owner2 + \
               ", Balance: " + str(super().getBalance())
