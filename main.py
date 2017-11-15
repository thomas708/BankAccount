#!/usr/bin/python3
#########################################################
# Test driver for BankAccount, JointBankAccount, and
# CreditBankAccount classes
#########################################################

# Importing the classes we will use
# Format is: from <file name without .py> import <class name>
from BankAccount import BankAccount
from JointBankAccount import JointBankAccount
from CreditBankAccount import CreditBankAccount


# Create a BankAccount object and do a few transactions
# Notice "try/except" statement to handle exceptions raised
basicAccount = BankAccount("Sam Smith", 0)
print("At creation      : " + basicAccount.toString())

basicAccount.deposit(100)
print("After deposit 100: " + basicAccount.toString())

basicAccount.withdraw(50)
print("After withdraw 50: " + basicAccount.toString())

try:
    basicAccount.withdraw(75)
    print("After withdraw 75: " + basicAccount.toString())
except Exception as ex:
    print("Failed to withdraw 75: " + str(ex))


# Create a JointBankAccount account and do a few transactions
# Notice the "deposit()" and "withdraw()" calls are on JointBankAccount's
# parent class (since they are not defined in JointBankAccount) but the
# "toString()" function calls are from JointBankAccount (since it overrides
# the one in JointBankAccount's parent)
jointAccount = JointBankAccount("John Smith", "Sue Smith", 105)
print("At creation       : " + jointAccount.toString())

jointAccount.deposit(100)
print("After deposit 100 : " + jointAccount.toString())

jointAccount.withdraw(150)
print("After withdraw 150: " + jointAccount.toString())

try:
    jointAccount.withdraw(75)
    print("After withdraw 75: " + jointAccount.toString())
except Exception as ex:
    print("Failed to withdraw 75: " + str(ex))


# Example of polymorphism in Python
# The following "makeWithdrawal()" function takes an account object
# and calls the correct "withdraw()" and "toString()" methods on that
# object, regardless of whether it is a base class object or child
# class object.  Remember that in Python the account object has a
# type, but it's not explicitly declared.  Rather the type is
# determined dynamically at runtime.
def makeWithdrawal(account, amount):
    try:
        account.withdraw(amount)
        print("Success")
    except Exception as ex:
        print("Failed: " + str(ex))
    finally:
        print(account.toString())


# Create an account of type CreditBankAccount
creditAccount = CreditBankAccount("Bob Smith", 50)

# Call the makeWithdrawal function with 3 different types of oject
# Notice the behavior is appropriate to each object type as expected
print("About to withdraw 75 from BankAccount")
makeWithdrawal(basicAccount, 75)
print("About to withdraw 75 from JointBankAccount")
makeWithdrawal(jointAccount, 75)
print("About to withdraw 75 from CreditBankAccount")
makeWithdrawal(creditAccount, 75)

# After this point the 3 objects (basicAccount, jointAccount, creditAccount)
# go out of scope and will be deleted.  Notice the destructor messages for
# the objects are printed out.
# Note: Need to run on command line, not IDLE, to see the destructor messages.
