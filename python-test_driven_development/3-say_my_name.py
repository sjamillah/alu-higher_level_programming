#!/usr/bin/python3
"""Script that prints a name"""


def say_my_name(first_name, last_name=""):
     '''Function to take in names and prints all name
    Args:
        first_name : this is the first arg in a string format
        last_name : must be a string too

    Returns:
        My name is <first name> <last name>
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
