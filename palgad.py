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
    if (choiceName == SORTEERI):
        sorteeri()
    if (choiceName == SARNASED):
        sarnased()
    if (choiceName == MAKSE):
        calculateTax()
    if (choiceName == PALGA_OTSING):
        palgaOtsing()
    if (choiceName == TAHT_OTSING):
        findByLetter()


    print()
