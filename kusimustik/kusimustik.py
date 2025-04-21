import json
from random import *
from email.message import EmailMessage
import smtplib
import ssl

DIR = "kusimustik/"
kus_vas = {}
oiged = {}
valed = {}
emails = {}

def saadaKiri(saaja:str, teema:str, sisu:str):
    server = "smtp.gmail.com"
    port = 587
    sender = "" # sender email
    password = "" # app password
    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = sender
    msg["To"] = saaja
    msg.set_content(sisu)

    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

def saadaValeKiri(nimi:str, email:str):
    saadaKiri(email, "Küsimustiku tulemus", f"""
    Tere {nimi}!  
    Sinu õigete vastuste arv: {oiged[nimi]}.  
    Kahjuks testi ei sooritatud edukalt.
    """)

def saadaOigeKiri(nimi:str, email:str):
    saadaKiri(email, "Küsimustiku tulemus", f"""
    Tere {nimi}!  
    Sinu õigete vastuste arv: {oiged[nimi]}.  
    Sa sooritasid testi edukalt.
    """)

def dir(directory:str)->str:
    return DIR + directory

def loeJsonFail(nimi:str)->dict:
    with open(dir(nimi), "r", encoding="utf-8-sig") as f:
        andmed = json.load(f)
    return andmed

def salvestaJsonFail(data:dict, nimi:str)->None:
    andmed = {"kusimused": []}
    for k, v in data.items():
        andmed["kusimused"].append({"question": k, "answer": v})

    with open(dir(nimi), "w", encoding="utf-8-sig") as f:
        json.dump(andmed, f, indent=2, ensure_ascii=False)

def getEmail(nimi:str)->str:
    if (nimi in emails):
        return emails[nimi]

    ret = nimi.replace(" ", ".").lower() + "@example.com"
    emails[nimi] = ret
    return ret

def kusimustik(nimi):
    if (nimi in oiged):
        print("Te olete juba vastanud.")
        return

    print("Küsimustik!")
    kusimusteArv = randint(4, len(kus_vas))
    print(f"Küsime sinult {kusimusteArv} küsimused")

    kusimused = list(kus_vas.keys())
    shuffle(kusimused)
    oige = 0
    for i in range(kusimusteArv):
        kusimus = kusimused[i]
        vastus = input(kusimus + " : ")
        if vastus == kus_vas[kusimus]:
            print("Õige!")
            oige += 1
        else:
            print("Vale!")

    print("\nTulemus: ")
    protsent = oige / kusimusteArv
    oiged[nimi] = oige
    if (protsent < 0.5):
        valed[nimi] = oige
        print("Teie tulemus on alla 50%.")
    else:
        print("Te olete tubli!")

def sooritaKusimustik():
    print("Küsime 3 inimest.")
    for i in range(3):
        nimi = input("Sisesta oma nimi: ")
        perenimi = input("Sisesta oma perenimi: ")
        name = nimi + " " + perenimi
        kusimustik(name)

    # Salvestame õiged vastused
    with open(dir("oiged.txt"), "w", encoding="utf-8-sig") as f:
        arr = zip(oiged.values(), oiged.keys())
        s = sorted(arr, reverse=True)
        for punkt, nimi in s:
            if (nimi in valed):
                continue
            f.write(f"{nimi} - {punkt} õigesti\n")

    # Salvestame valed vastused
    with open(dir("valed.txt"), "w", encoding="utf-8-sig") as f:
        arr = valed.keys()
        s = sorted(arr)
        for nimi in s:
            f.write(f"{nimi}\n")

    # Salvestame kõik vastused
    with open(dir("koik.txt"), "w", encoding="utf-8-sig") as f:
        arr = zip(oiged.values(), oiged.keys())
        s = sorted(arr, reverse=True)
        for punkt, nimi in s:
            email = getEmail(nimi)
            f.write(f"{nimi} - {punkt} õigesti - {email}\n")

    # Saada kiri
    for nimi in oiged.keys():
        email = getEmail(nimi)
        print(f"Saadame kiri {email}")
        if (nimi in valed):
            saadaValeKiri(nimi, email)
        else:
            saadaOigeKiri(nimi, email)

    arr = zip(oiged.values(), oiged.keys())
    s = sorted(arr, reverse=True)
    parimPunkt, parimNimi = s[0]

    leaderboard = ""
    for i, (nimi, punkt) in enumerate(oiged.items()):
        email = getEmail(nimi)
        sobib = nimi not in valed
        if sobib:
            leaderboard += f"{i + 1} {nimi} - {punkt} õigesti - {email} - SOBIS\n"
        else:
            leaderboard += f"{i + 1} {nimi} - {punkt} õigesti - {email} - EI SOBINUD\n"

    print("\nSaadame kiri töötajale.")
    email = input("Sisesta töötaja e-mail: ")

    saadaKiri(email, "Tänased küsimustiku tulemused", f"""
    Tere!

    Tänased küsimustiku tulemused: 

    {leaderboard}

    Parim vastaja: {parimNimi} ({parimPunkt} õigesti))

    Lugupidamisega,
    Küsimustiku Automaatprogramm
    """)

andmed = loeJsonFail("kusimused.json")
for kusimus in andmed.get("kusimused", "[]"):
    kus_vas[kusimus["question"]] = kusimus["answer"]

while True:
    print("1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("0. Välju")

    try:
        valik = int(input("Vali tegevus: "))
        if (valik > 2 or valik < 0):
            print("Vale valik!")
            continue
    except:
        print("Vale!")
        continue

    if (valik == 0):
        print("Väljun...")
        break

    if (valik == 1):
        sooritaKusimustik()
        continue

    if (valik == 2):
        k = input("Küsimus: ")
        v = input("Vastus: ")
        kus_vas[k] = v
        salvestaJsonFail(kus_vas, "kusimused.json")
        continue