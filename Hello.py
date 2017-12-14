#!/usr/bin/python

class Hello:
    """Enter name and print greeting"""

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print "Hello " + self.name + ", and good bye."


"Take user input as string"
action = raw_input("Enter name: ")

"Create object for Hello Class"
hello = Hello(action)

hello.display_name()

