from sairus.functions.clearPage import *
from sairus.functions.printb import printb

from sairus.config.config import ownerName

printb(f"Welcome {ownerName}!")

while True:
    user = input("Message: ")

    if user == "hello!":
        printb(f"Hello {ownerName}!")
    elif user == "bye bye":
        printb(f"Bye Bye {ownerName}!")
        exit(0)