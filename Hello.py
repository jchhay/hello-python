#!/usr/bin/python
"""Hello.py: Enter name and print greeting"""

__author__ = "Jeffrey Chhay"
__copyright__ = "Copyright 2017, Hello Test"
__credits__ = ["Jeffrey Chhay"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Jeffrey Chhay"
__email__ = "n/a"
__status__ = "Prototype"  # Prototype/Development/Production


class Hello:

    def __init__(self, name):
        """Sets user's name"""
        self.name = name

    def display_name(self):
        """Prints greeting with user's name"""
        print("Hello " + self.name + ", and good bye.")


# Take user input as string
action = input("Enter name: ")

# Create object for Hello Class
hello = Hello(action)

hello.display_name()

