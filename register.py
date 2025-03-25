from calendar import c
from ModuleRegister import *
import os

while True:
    print()
    print("1. Registreeri")
    print("2. Logi sisse")
    print("3. Unustasid parooli")
    print("4. Muuda parooli")
    print("5. Muuda kasutajanime")
    print("0. Välju")
    print()
    print()

    choice = menuChoice()
    os.system("cls")

    if (choice == 0):
        print("Goodbye!")
        break

    if (choice == 1):
        register()
        continue

    if (choice == 2):
        id = loginId(input("Kasutajanimi: "), input("Parool: "))
        if (id == -1):
            print("Vale kasutajanimi või parool")
            continue
        loggedIn = id
        print("Sisselogimine õnnestus!")
        continue

    if (choice == 3):
        while True:
            username = input("Kasutajanimi: ")
            if username not in usernames:
                print("Kasutaja ei leitud.")
                continue
            break

        id = usernames.index(username)
        print("Parool: " + passwords[id])
        continue

    if (choice == 4):
        if (loggedIn == -1):
            print("Palun logi sisse.")
            continue

        passwords[loggedIn] = input("Sisesta uus parool: ")
        continue

    if (choice == 5):
        if (loggedIn == -1):
            print("Palun logi sisse.")
            continue

        usernames[loggedIn] = input("Sisesta uus kasutajanimi: ")
        continue
