from curses.ascii import isalpha
import string
import random
import os
import sys

LISA_INIMENE = "Lisa inimene"
KUSTUTA_INIMENE = "Kustuta inimene"
SUURIM_PALK = "Suurim Palk"
VAIKSEM_PALK = "Väiksem Palk"

menu = [
    LISA_INIMENE,
    KUSTUTA_INIMENE,
    SUURIM_PALK,
    VAIKSEM_PALK
    ]

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

def showData():
    print("Palgad: " + str(palgad))
    print("Inimesed: " + str(inimesed))
    print()

def showMenu():
    print("Vali tegevus:")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")
    print("0. Välju")
    print()

def clearConsole():
    os.system("cls")

def clearOneLine():
    #print("\033[A" + (" " * os.get_terminal_size().columns) + "\033[A")
    ...

def menuChoice()->int:
    while True:
        try:
            choice = int(input("Valik: "))
            if choice >= 0 and choice <= len(menu):
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

def inputYesNo(text:str)->bool:
    while True:
        choice = input(text)
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Vale valik!")

def inputInt(text:str, min:int = -1, max:int = -1)->int:
    if (min != -1 or max != -1):
        maxStr = "+" if max == -1 else f"-{max}"
        text += f"({min}{maxStr})"
    while True:
        try:
            choice = int(input(text))
            if (min == -1 or choice >= min) and (max == -1 or choice <= max):
                return choice
            else:
                clearOneLine()
                clearOneLine()
                print("Vale valik!")
        except:
            clearOneLine()
            clearOneLine()
            print("Vale valik!")

def inputNimi(text:str)->str:
    while True:
        name = input(text)
        if len(name) > 0 and name.isalpha():
            return name
        else:
            clearOneLine()
            clearOneLine()
            print("Vale nimi!")

def lisaInimesed()->any:
    count = inputInt("Mitu?", 1, 10)
    for i in range(count):
        name = inputNimi("Nimi:")
        palk = inputInt("Palk:", 0)
        inimesed.append(name)
        palgad.append(palk)

def kustutaInimene()->any:
    while True:
        name = inputNimi("Nimi:")
        if (name not in inimesed):
            print("Nimi ei leitud")
            continue
        index = inimesed.index(name)
        palgad.pop(index)
        inimesed.pop(index)
        break

def suurimPalk()->any:
    maxPalk = max(palgad)
    count = palgad.count(maxPalk)
    maxIndex = palgad.index(maxPalk)
    print(f"Suurim palk on:\n {inimesed[maxIndex]}: {palgad[maxIndex]}")
    for i in range(count-1):
        maxIndex = palgad.index(maxPalk, maxIndex+1)
        print(f" {inimesed[maxIndex]}: {palgad[maxIndex]}")

def vaiksemPalk()->any:
    minPalk = min(palgad)
    count = palgad.count(minPalk)
    minIndex = palgad.index(minPalk)
    print(f"Väikseim palk on:\n {inimesed[minIndex]}: {palgad[minIndex]}")
    for i in range(count-1):
        minIndex = palgad.index(minPalk, minIndex+1)
        print(f" {inimesed[minIndex]}: {palgad[minIndex]}")