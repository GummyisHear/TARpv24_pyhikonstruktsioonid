import os
import random
from pyfiglet import *
from colorama import Fore, Back, Style, init

# Initialize colorama (important for Windows)
init(autoreset=True)


sonad = [ "eesti", "loodus", "õun", "vana", "sõber", "täht" ]
vastus = random.choice(sonad)
arvumused = []
katsed = 6

def inputFixedLengthGuess(length, message):
    while True:
        arvumus = input(message)
        if len(arvumus) != length:
            print(f"Arvamus peab olema {length} tähemärki pikk")
        elif (not arvumus.isalpha()):
            print("Arvumus peab olema ainult tähti")
        else:
            return arvumus

def drawGame():
    os.system("cls")
    print("=== Eesti Wordle!")
    length = len(vastus)
    arr = [ (Fore.CYAN + " - ") * length ]

    for j, sone in enumerate(arvumused):
        if (j >= katsed):
            break
        for i, taht in enumerate(sone):
            if (vastus[i] == taht):
                taht = Back.GREEN + taht
            elif (taht in vastus):
                taht = Back.YELLOW + taht
            else:
                taht = Back.RED + taht

            print(f" {taht} ", end = "")
        print()

    for i in arr:
        print(i)

for i in range(katsed):
    drawGame()
    g = inputFixedLengthGuess(len(vastus), "Sinu arvamus: ")
    arvumused.append(g)

    if g == vastus:
        drawGame()
        print(Fore.GREEN + figlet_format('You win!', font='doom'))
        break
    elif i == katsed -1:
        drawGame()
        print(Back.CYAN + f"Vastus oli: {vastus}")
        print(Fore.RED + figlet_format('You lose!', font='doom'))
        break
