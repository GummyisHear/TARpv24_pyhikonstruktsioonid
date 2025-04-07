from palgadModule import *

while True:
    showData()
    showMenu()
    choice = menuChoice()
    choiceName = menu[choice-1]

    if (choice == 0):
        print("Head aega!")
        break

    if (choiceName == LISA_INIMENE):
        lisaInimesed()
    if (choiceName == KUSTUTA_INIMENE):
        kustutaInimene()
    if (choiceName == SUURIM_PALK):
        suurimPalk()
    if (choiceName == VAIKSEM_PALK):
        vaiksemPalk()

    print()
