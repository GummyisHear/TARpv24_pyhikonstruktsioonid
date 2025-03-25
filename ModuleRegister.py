import string
import random
import os

usernames = [ "artjomProGamer" ]
passwords = [ "1234" ]
loggedIn = -1

def randomPassword(length:int = 8)->str:
    chars = string.ascii_letters + string.digits
    l = list(chars)
    random.shuffle(l)
    return ''.join(l[:length])

def clearOneLine():
    print("\033[A" + (" " * os.get_terminal_size().columns) + "\033[A")

def menuChoice()->int:
    while True:
        try:
            choice = int(input("Valik: "))
            if choice >= 0 and choice <= 5:
                break
            else:
                clearOneLine()
                clearOneLine()
                print("Vale valik!")
        except:
            clearOneLine()
            clearOneLine()
            print("Vale valik!")

    return choice

def register()->any:
    username = inputNewUsername("Kasutajanimi: ")
    if (inputYesNo("Kas soovite genereerida parooli? (y/n): ")):
        password = randomPassword(3)
        print("Parool: " + password)
    else:
        password = input("Parool: ")

    usernames.append(username)
    passwords.append(password)

def loginId(user:str, password:str)->int:
    for i in range(len(usernames)):
        if usernames[i] == user and passwords[i] == password:
            return i

    return -1


def inputNewUsername(text:str)->str:
    while True:
        username = input(text)
        if username in usernames:
            print("See kasutajanimi on juba kasutatud.")
        else:
            return username

def inputYesNo(text:str)->bool:
    while True:
        choice = input(text)
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Vale valik!")