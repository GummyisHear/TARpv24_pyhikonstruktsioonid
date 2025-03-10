
from time import sleep

# v5 3. Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.

for op in range(20):
    print(f"Sooritab eksamit {op+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

# v4. 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

vastus = 0
while True:
    try:
        P = int(input("Mitu korda kordame? "))
        break
    except:
        print("Sisesta täisarv!")  
for i in range(P):
    while True:
        try:
            arv = float(input("Sisesta arv: "))
            break
        except:
            print("Sisesta arv!")
    if arv<0:
        vastus += arv

print(f"Summ negatiivsete arvude: {vastus}")

# v1 4. Koostage plokkskeem kotlette praadiva roboti jaoks.
while True:
    try:
        kokku = int(input("Kokku kotlete: "))
        break
    except:
        print("Sisesta täisarved!")

while True:
    try:
        panni_maht = int(input("Panni maht: "))
        break
    except:
        print("Sisesta täisarved!")

aeg = 1
while True:
    praadime = min(panni_maht, kokku)
    print(f"Praadime {praadime} kotlette")
    print("Praadime esimene pool", end="")
    sleep(aeg)
    print("Praadime teine pool", end="")
    sleep(aeg)
    kokku -= praadime
    print()
    if (kokku <= 0):
        break

print("Kotletid on valmis!")

# v11 2. küsitlege O kasutajaid. Selgitage välja nende kaal ja pikkus ning vanus. Leidke kehamassiindeks ja teatage kasutajale selle indeksi iseloomustus.

while True:
    try:
        o = int(input("Mitu kasutajat on? "))
        break
    except:
        print("Sisesta kaal!")

for i in range(o):
    print(f"{i+1}. Kasutaja")
    while True:
        try:
            kaal = float(input("Sisesta kaal: "))
            break
        except:
            print("Sisesta kaal!")
    while True:
        try:
            pikkus = float(input("Sisesta pikkus: "))
            break
        except:
            print("Sisesta pikkus!")
    while True:
        try:
            vanus = int(input("Sisesta vanus: "))
            break
        except:
            print("Sisesta vanus!")
    bmi = kaal/(pikkus*pikkus)
    if (bmi < 18.5):
        print("Alakaaluline")
    elif (bmi < 25):
        print("Normaalkaal")
    elif (bmi < 30):
        print("Ülekaaluline")
    else:
        print("Rasvunud")

# v10 2. Te lähete kinosse. Kinosaalile lähenedes avastate, et täna on seal kaks filmi: uus "Harry Potteri" sari ja uus põnevusfilm Sylvester Stallone'iga. Kui teil on piletid esimesele, lähete seda vaatama, muidu vaatate põnevusfilmi.

print("Lähme kinno!")
print("Täna on kaks filmi: Harry Potter ja Sylvester Stallone")

while True:
    try:
        harryPilet = input("Kas sul on piletid Harry Potteri filmidele? (jah/ei) ")
        if (harryPilet != "jah" and harryPilet != "ei"):
            print("Sisesta jah või ei!")
            continue
        break
    except:
        print("Sisesta jah või ei!")

if (harryPilet == "jah"):
    print("Lähme Harry Potterit vaatama!")
else:
    print("Lähme Sylvester Stallone filmi vaatama!")