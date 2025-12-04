# Python Decorators
"""
A decorator is a functional that takes another function
and extends or modifies its behavior without changing the orginal funtions.
"""

def add_security(func):
    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards, License")
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    return wrapper()


def driver_ola_scooter():
    print("I am driving the ola scooter")

def driver_zypp_scooter():
    print("Driving Zypp scooter")

# Decorators with Arguments

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print('Hi')