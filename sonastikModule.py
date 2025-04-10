import random

keel1 = "est"
keel2 = "rus"

sonastik = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]

def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return None

def lisa_sona(sonad):
    print("Lisame uue sõna sõnastikku!")
    uus_est = inputSona("Sisesta sõna eesti keeles: ").strip().lower()
    uus_rus = inputSona("Sisesta sõna vene keeles: ").strip().lower()
    uus_eng = inputSona("Sisesta sõna inglise keeles: ").strip().lower()
    
    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("Uus sõna on lisatud!")

def otsi_indeks(sona:str):
    for i, kirje in enumerate(sonastik):
        if (sona in kirje.values()):
            return i

    return -1

def otsi_sona(sona:str):
    indeks = otsi_indeks(sona)
    if (indeks == -1):
        print("Sõna pole leitud")
        return

    for keel, s in sonastik[indeks].items():
        print(keel, s)

def paranda_sona(sona:str):
    indeks = otsi_indeks(sona)
    if (indeks == -1):
        print("Sõna pole leitud")
        return

    for keel, s in sonastik[indeks].items():
        print(keel, s)
        uus = input("Sisesta parandus (tühi kui ei soovi): ")
        if (len(uus) > 0):
            sonastik[indeks][keel] = uus

def kuva_sonad():
    print("Sõnastik:")
    for i, kirje in enumerate(sonastik):
        string = f"{i+1}: "
        for keel, s in kirje.items():
            string += s.ljust(12)
        print(string)

def vali_keel()->str:
    keeled = ["est", "rus", "eng"]
    while True:
        try:
            i = int(input("Vali keel (0 - eesti, 1 - vene, 2 - inglise): "))
            if (i < 0 or i >= len(keeled)):
                print("Vale valik!")
                continue
            break
        except:
            print("Vale valik!")
            continue

    return keeled[i]

testiTulemused = []

def testi_sonad():
    sonad1 = []
    sonad2 = []
    for kirje in sonastik:
        for keel, s in kirje.items():
            if (keel == keel1):
                sonad1.append(s)
            if (keel == keel2):
                sonad2.append(s)
    
    total = len(sonad1)
    oige = 0
    print(f"Tõlgi [{keel1} -> {keel2}]")
    for i, sona in enumerate(sonad1):
        tolgi = inputSona(sona + " -> ")
        if (tolgi == sonad2[i]):
            print("GG WP!")
            oige += 1
        else:
            print("Boowoomp...")

    testiTulemused.append([oige, total])
    print("Et testi tulemusi näita, valige 7")

def kuva_tulemused():
    print("Tulemused: ")
    for i, test in enumerate(testiTulemused):
        oige = test[0]
        kokku = test[1]
        protsent = round(oige / kokku * 100, 2)
        print(f"Test {i + 1}: {test[0]}/{test[1]} {protsent}%")

def inputSona(tekst:str)->str:
    while True:
        sona = input(tekst)
        sona = sona.strip().lower()
        if (len(sona) > 0):
            return sona

def juhuslik_sona():
    sonad = []
    for kirje in sonastik:
        sonad.append([kirje["est"], kirje["rus"], kirje["eng"]])

    sona = random.choice(sonad)

    print("Juhuslik sõna:")
    for tolgi in sona:
        print(tolgi, end=", ")
    print()

def kuva_menu():
    print("1 - Kuva sõnastik")
    print("2 - Vali Keel")
    print("3 - Lisa sõna")
    print("4 - Otsi sõna")
    print("5 - Paranda sõna")
    print("6 - TEST")
    print("7 - Testi tulemused")
    print("8 - Juhuslik sõna")
    print("0 - Välju")