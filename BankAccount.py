#!/usr/bin/python3
#########################################################
# Encapsulates data and methods of a generic bank account
#########################################################

class BankAccount:

    # Note the "self" as the first parameter in all of the
    # methods.  This is a peculiarity of Python.  Just
    # get used to it.  When you call the method the "self"
    # argument is automatically inserted for you.  So to
    # call the "withdraw" function here just do "withdraw(75)"
    # with only a single argument.
    
    # Constructor (automatically called when creating a new object)
    def __init__(self, owner, balance):
        print("Creating BankAccount")
        # Create and initialize two variables named "owner"
        # and "__balance".  Variables with two leading
        # underscores are private.  Variables without two leading
        # underscores are public.
        self.owner = owner
        self.__balance = balance

    # Destructor (automatically called when object goes out of scope,
    # or explicitly called with "del" function)
    def __del__(self):
        # The "self.__class__.__name__" dynamically gets the name
        # of the class at runtime, in this case "BankAccount"
        print("Destroying " + self.__class__.__name__)

    # Deposit money
    def deposit(self, amount):
        # To use instance variables always add "self." in front
        # of the variable name
        self.__balance += amount

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            # Raising an exception for the caller to catch
            # Here we create a new exception object from the built-in
            # Exception class
            raise Exception("Insufficient funds")
        self.__balance -= amount

    # Get balance
    def getBalance(self):
        return self.__balance

    # Get owner
    def getOwner(self):
        return self.owner

    # Set balance
    def setBalance(self, newBalance):
        self.__balance = newBalance

    # Print account
    def toString(self):
        # Notice how "self.__balance" is inside the "str()" function but
        # "self.owner" is not? That's because in Python the type of a variable
        # is determined by its contents.  "self.owner" contains a string so it's
        # type is string and can be readily concatenated with other strings.
        # "self.__balance" contains an integer so it's type is an integer and must
        # be converted to a string using str() function before concatening with
        # other strings.  The plus sign "+" is used to concatenate several strings
        # together
        return "Owner: " + self.owner + ", Balance: " + str(self.__balance)

