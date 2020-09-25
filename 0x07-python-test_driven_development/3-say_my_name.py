#!/usr/bin/python3
""" This function will print out a message with a name from input """


def say_my_name(first_name, last_name=""):
    """
    say_my_name - a function that will print out a message with user input
    Argument1 - A string, meant to be first name, required
    Argument2 - A string, meant to be last name, defualt is empty
    return - no return, just print to stdout
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
