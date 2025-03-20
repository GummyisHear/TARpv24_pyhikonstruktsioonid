import string
import random
import os

def randomPassword(length:int = 8)->str:
    chars = string.ascii_letters + string.digits
    l = list(chars)
    random.shuffle(l)
    return ''.join(l[:length])

def clearOneLine():
    print("\033[A" + (" " * os.get_terminal_size().columns) + "\033[A")

def menuChoice()->int:
    os.system("cls")

    print("1. Registreeri")
    print("2. Logi sisse")
    print("3. Unustasid parooli")
    print("4. Muuda parooli")
    print("5. Muuda kasutajanime")
    print("0. Välju")

    print()
    print()
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
    username = input("Kasutajanimi: ")
    if (inputYesNo("Kas soovite genereerida parooli? (y/n): ")):
        password = randomPassword()
        print("Parool: " + password)
    else:
        password = input("Parool: ")

    return (username, password)


def inputYesNo(text:str)->bool:
    while True:
        choice = input(text)
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Vale valik!")