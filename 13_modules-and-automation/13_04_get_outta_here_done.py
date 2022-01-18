# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys


x=1

while x==1:
    string = input("Enter quit to exit: ")
    if string=="quit":
        quit()