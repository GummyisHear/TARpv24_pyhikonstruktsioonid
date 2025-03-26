# B-5 Inimesed 

nimed = []
kasv = []

def intInput(text:str)->int:
    """Küsib kasutajat sisestama täisarvu
    :param str text: Tekst mis väljastatakse kasutajale
    :rtype: Sisestatud kasutajalt täisarv
    """
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Sisesta täisarv!")

def nimiInput(text:str):
    """Küsib kasutajat sisestama kasutaja nimi
    :param str text: Tekst mis väljastatakse kasutajale
    :rtype: Sisestatud nimi, mis on olemas nimede listis
    """
    while True:
        nimi = input(text)
        if nimi in nimed:
            return nimi
        else:
            print("Inimene ei leitud!")

def inimesed()->any:
    """Küsib kasutajat sisestama mitu uued kasutajat ja lisab nad nimede listi
    """
    arv = intInput("Mitu inimesed tahad lisada: ")
    for i in range(arv):
        nimed.append(input("Sisesta inimese nimi: "))
        kasv.append(intInput("Sisesta inimese kasv: "))

inimesed()
print()

while True:
    print()
    print("1. Kustuta")
    print("2. Näita tähestiku järjel")
    print("3. Kõige pikem ja kõige lühem inimesed")
    print("4. Keskmine pikkus")
    print("5. Muuda pikkus")
    print("0. Välju")
    print()
    
    valik = intInput("Valik: ")

    if (valik == 0):
        break

    if (valik == 1):
        nimi = nimiInput("Sisesta nimi: ")
        while (nimi in nimed):
            index = nimed.index(nimi)
            nimed.pop(index)
            kasv.pop(index)
        print("Inimesed kustutatud!")
        continue

    if (valik == 2):
        alphabet = sorted(nimed)
        for i in range(len(alphabet)):
            index = nimed.index(alphabet[i])
            print(nimed[index] + " - " + str(kasv[index]))

        continue

    if (valik == 3):
        pikkIndeks = -1
        luheIndeks = -1
        
        for i in range(len(nimed)):
            if (pikkIndeks == -1 or kasv[i] > kasv[pikkIndeks]):
                pikkIndeks = i
            if (luheIndeks == -1 or kasv[i] < kasv[luheIndeks]):
                luheIndeks = i

        print("Kõige pikem inimene: " + nimed[pikkIndeks] + " - " + str(kasv[pikkIndeks]))
        print("Kõige lühem inimene: " + nimed[luheIndeks] + " - " + str(kasv[luheIndeks]))
        continue

    if (valik == 4):
        print("Sisesta inimese nimed! Ei sisesta midagi kui tahad lõpetada!")
        sum = 0
        arv = 0
        while True:
            nimi = ""

            while True:
                nimi = input("Sisesta nimi: ")
                if nimi in nimed or nimi == "":
                    break
                else:
                    print("Inimene ei leitud!")

            if (nimi == ""):
                break

            sum += kasv[nimed.index(nimi)]
            arv += 1
        
        print(f"Keskmine kasv on: {sum / arv}")
        continue

    if (valik == 5):
        nimi = nimiInput("Sisesta nimi: ")
        index = nimed.index(nimi)
        kasv[index] = intInput("Sisesta uus pikkus: ")
        print("Pikkus muudetud!")
        continue


