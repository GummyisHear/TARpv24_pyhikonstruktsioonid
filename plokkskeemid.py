
# v5 3. Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.

from time import sleep


for op in range(20):
    print(f"Sooritab eksamit {op+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

# v4. 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

vastus = 0
P = int(input("Mitu korda kordame? "))     
for i in range(P):
    arv = float(input("Sisesta arv: "))
    if arv<0:
        vastus += arv

print(f"Summ negatiivsete arvude: {vastus}")

def dotSleep(time):
    dots = 3
    for i in range(dots):
        print(".", end="")
        sleep(time/dots)
    print()

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
    dotSleep(aeg)
    print("Praadime teine pool", end="")
    dotSleep(aeg)
    kokku -= praadime
    print()
    if (kokku <= 0):
        break

print("Kotletid on valmis!")