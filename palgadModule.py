from curses.ascii import isalpha
from operator import le
import string
import random
import os
import sys

LISA_INIMENE = "Lisa inimene"
KUSTUTA_INIMENE = "Kustuta inimene"
SUURIM_PALK = "Suurim Palk"
VAIKSEM_PALK = "Väiksem Palk"
SORTEERI = "Sorteeri palka järgi"
SARNASED = "Leia sarnased palgad"
MAKSE = "Maksud"
PALGA_OTSING = "Palga otsing"

menu = [
    LISA_INIMENE,
    KUSTUTA_INIMENE,
    SUURIM_PALK,
    VAIKSEM_PALK,
    SORTEERI,
    SARNASED,
    MAKSE,
    PALGA_OTSING
    ]

palgad = [ 1200, 2500, 750, 395, 1200 ]
inimesed = [ "A", "B", "C", "D", "E" ]

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
    """
    Lisa inimesi ja nende palkasid
    :return: None
    """
    count = inputInt("Mitu?", 1, 10)
    for i in range(count):
        name = inputNimi("Nimi:")
        palk = inputInt("Palk:", 0)
        inimesed.append(name)
        palgad.append(palk)

def kustutaInimene()->any:
    """
    Kustuta inimene
    :return: None
    """
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
    """
    Leia suurim palk
    :return: None
    """
    maxPalk = max(palgad)
    count = palgad.count(maxPalk)
    maxIndex = palgad.index(maxPalk)
    print(f"Suurim palk on:\n {inimesed[maxIndex]}: {palgad[maxIndex]}")
    for i in range(count-1):
        maxIndex = palgad.index(maxPalk, maxIndex+1)
        print(f" {inimesed[maxIndex]}: {palgad[maxIndex]}")

def vaiksemPalk()->any:
    """
    Leia väikseim palk
    :return: None
    """
    minPalk = min(palgad)
    count = palgad.count(minPalk)
    minIndex = palgad.index(minPalk)
    print(f"Väikseim palk on:\n {inimesed[minIndex]}: {palgad[minIndex]}")
    for i in range(count-1):
        minIndex = palgad.index(minPalk, minIndex+1)
        print(f" {inimesed[minIndex]}: {palgad[minIndex]}")

def sorteeri()->any:
    """
    Sorteeri inimese nende palka järgi
    :return: None
    """
    print(" 1. Kasvavas")
    print(" 2. Kahanevas")
    order = inputInt("Vali järjestus:", 1, 2)

    if (order == 1):
        for i in range(len(palgad)):
            for j in range(i + 1, len(palgad)):
                if palgad[i] > palgad[j]:
                    palgad[i], palgad[j] = palgad[j], palgad[i]
                    inimesed[i], inimesed[j] = inimesed[j], inimesed[i]
        return

    if (order == 2):
        for i in range(len(palgad)):
            for j in range(i + 1, len(palgad)):
                if palgad[i] < palgad[j]:
                    palgad[i], palgad[j] = palgad[j], palgad[i]
                    inimesed[i], inimesed[j] = inimesed[j], inimesed[i]
        return

def sarnased()->any:
    """
    Leia sarnased palgad
    :return: None
    """
    for i in range(len(palgad)):
        for j in range(len(palgad)):
            if (i != j and palgad[i] == palgad[j]):
                print(f"{inimesed[i]} ja {inimesed[j]} palk on {palgad[i]}")

def calculateTax()->any:
    summa = 0
    for i in range(len(palgad)):
        summa += palgad[i] / 0.67 - palgad[i]
    
    print(f"Sa pead maksma {round(summa, 2)} eurot makse töötajale.")

def palgaOtsing()->any:
    """
    Otsi palka
    :return: None
    """
    palk = inputInt("Palk: ", 0)

    if (palk in palgad):
        index = palgad.index(palk)
        print(f"Leitud inimesed: ")
        print(f" {inimesed[index]}")
        for i in range(palgad.count(palk) - 1):
            index = palgad.index(palk, index + 1)
            print(f" {inimesed[index]}")
    else:
        print("Palk ei leitud")

def aaa():
    # Найти имена начинающиеся на введенную букву и их зарплаты. Отобразить данные в столбик (Имя-зарплата)
    ...

def bbb():
    ...