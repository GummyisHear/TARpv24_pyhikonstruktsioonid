from calendar import c
from ModuleRegister import *
import os

readFile()

while True:
    print()
    print("1. Registreeri")
    print("2. Logi sisse")
    print("3. Unustasid parooli")
    print("4. Muuda parooli")
    print("5. Muuda kasutajanime")
    print("6. Salvesta fail")
    print("0. Välju")
    print()
    print()

    choice = menuChoice()
    os.system("cls")

    if (choice == 0):
        saveFile()
        print("Goodbye!")
        break

    if (choice == 1):
        register()
        continue

    if (choice == 2):
        login = loginId(input("Kasutajanimi: "), input("Parool: "))
        if (login == ""):
            print("Vale kasutajanimi või parool")
            continue
        loggedIn = login
        print("Sisselogimine õnnestus!")
        continue

    if (choice == 3):
        while True:
            username = input("Kasutajanimi: ")
            if username not in auths:
                print("Kasutaja ei leitud.")
                continue
            break

        print("Check your e-mail.")
        sendMail("artjompoldsaar@gmail.com", "Forgotten Password", f"You requested to see your forgotten password: {auths[username]}")
        continue

    if (choice == 4):
        if (loggedIn == ""):
            print("Palun logi sisse.")
            continue

        auths[loggedIn] = input("Sisesta uus parool: ")
        sendMail("artjompoldsaar@gmail.com", "New Password", f"Your password has been changed.")
        continue

    if (choice == 5):
        if (loggedIn == ""):
            print("Palun logi sisse.")
            continue

        newUser = input("Sisesta uus kasutajanimi: ")
        password = auths.pop(loggedIn)
        auths[newUser] = password
        sendMail("artjompoldsaar@gmail.com", "New Username", f"You have changed your username to {newUser}")
        continue

    if (choice == 6):
        print("Salvestame...")
        saveFile()
        continue
