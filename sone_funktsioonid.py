from pyfiglet import figlet_format

def inputInt(message):
    while True:
        try:
            return int(input(message))
        except:
            print("Palun sisesta täisarv!")

def inputInt2(message, predicate):
    while True:
        try:
            number = int(input(message))
            if predicate(number):
                return number
            else:
                print("Arv ei vasta tingimustele")
        except:
            print("Palun sisesta täisarv!")

def inputChar(message):
    while True:
        try:
            number = input(message)
            if (len(number) == 1):
                return number
            else:
                print("Peaks olema ainult 1 täht!")
        except:
            print("Palun sisesta üks täht!")

fonts = [
    "big",
    "doom",
    "drpepper",
    "isometric1",
    "jazmine",
    "ogre",
    "puffy",
    "rectangles",
    "roman",
    "slant",
    "speed"
]

functions = [
    "tekst[a:b]",
    "find()",
    "replace()",
    "split()",
    "ord()",
    "chr()",
    "join()",
    "center()",
    "partition()",
    "zfill()",
    "tekst[::-1]",
    "sort()",
    "ASCII tekst"
]

while True:
    for i in range(len(functions)):
        print(f"{i}. ".ljust(5) + functions[i])
    print("0. Kinnita programm")
    funkstioon = input("Sinu valik: ")

    if funkstioon == "1":
        sone = input("Sisesta üks sõne: ")
        start = inputInt2("Sisesta alusindeks: ", lambda i : i >= 0 and i < len(sone))
        end = inputInt2("Sisesta lõppindeks: ", lambda i : i >= 0 and i < len(sone))
        print(sone[start:end])

    elif funkstioon == "2":
        sone = input("Sisesta üks sõne: ")
        otsing = input("Sisesta otsitav sõne: ")
        print("Leitud indeks: ", sone.find(otsing))

    elif funkstioon == "3":
        sone = input("Sisesta üks sõne: ")
        muuda = input("Sisesta sõne mida muutme: ")
        uus = input("Sisesta uus sõne: ")
        print("Muutud sõne: ", sone.replace(muuda, uus))

    elif funkstioon == "4":
        sone = input("Sisesta üks sõne: ")
        sep = input("Sisesta eraldaja: ")
        print(sone.split(sep))

    elif funkstioon == "5":
        taht = inputChar("Sisesta üks täht: ")
        print("ASCII kood on", ord(taht))

    elif funkstioon == "6":
        kood = inputInt("Sisesta ASCII kood: ")
        print("ASCII koodi täht on: ", chr(kood))
    elif funkstioon == "7":
        arr = []
        print("Sisesta 3 sõned.")
        for i in range(3):
            arr.append(input("Sisesta üks sõne: "))
        sep = input("Sisesta eraldaja: ")
        print(sep.join(arr))

    elif funkstioon == "8":
        sone = input("Sisesta üks sõne: ")
        width = inputInt("Sisesta laius: ")
        fill = inputChar("Sisesta täidis (üks täht): ")
        print(sone.center(width, fill))

    elif funkstioon == "9":
        sone = input("Sisesta väike lause: ")
        otsi = input("Sisesta otsimis sõna: ")
        part = sone.partition(otsi)
        print("Esimene osa:", part[0])
        print("Teine osa:", part[1])
        print("Kolmas osa:", part[2])

    elif funkstioon == "10":
        sone = input("Sisesta üks sõne: ")
        nullid = inputInt("Kui palju nullid tahad: ")
        print(sone.zfill(nullid))

    elif funkstioon == "11":
        sone = input("Sisesta üks sõne: ")
        
        print(sone[::-1])

    elif funkstioon == "12":
        sone = input("Sisesta üks sõne: ")
        print("Vali mis fonti soovid kasutada. ")
        for i, f in enumerate(fonts):
            print(f"{i}.".ljust(5) + f)

        valik = inputInt2("Valik: ", lambda i : i >= -1 and i < len(fonts))

        print(figlet_format(sone, fonts[valik]))
    elif funkstioon == "0":
        break
    else:
        print("Vale valik!")

    print()