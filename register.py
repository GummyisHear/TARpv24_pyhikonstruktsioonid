from ModuleRegister import *

usernames = [ "artjomProGamer" ]
passwords = [ "1234" ]

while True:
    choice = menuChoice()

    if (choice == 0):
        print("Goodbye!")
        break

    if (choice == 1):
        username, password = register()