from datetime import *
import calendar
import random
import math
import time

tana = date.today()
print(f"Täna on {tana}")

# 27/12/2022
#tana = tana.strftime("%d/%m/%Y")

# December 27, 2022
#tana = tana.strftime("%B %d, %Y")

# 12/27/22
#tana = tana.strftime("%m/%d/%y")

# Dec-27-2022
#tana = tana.strftime("%b-%d-%Y")

aastaLopp = date(tana.year, 12, 31)
print(f"Aasta lõpp on {aastaLopp}")

aastaPaevad = aastaLopp - tana
print(f"Aasta lõppu on jäänud {aastaPaevad.days} päeva")

res = calendar.monthrange(tana.year, tana.month)
paevadKuus = res[1]
print(f"Kuus on {paevadKuus} päeva")

kuuPaevad = paevadKuus - tana.day
print(f"Kuu lõppu on jäänud {kuuPaevad} päeva")

# Ülesanne 2
a = 3 + 8 / (4 - 2) * 4
print("\n3 + 8 / (4 - 2) * 4 = ", a)
print("\n1) 4 - 2 \n2) 8 / 2 \n3) 4 * 4 \n4) 3 + 16")

a = 3 + (8 / 4 - 2) * 4
print("\n3 + (8 / 4 - 2) * 4 = ", a)
print("1) 8 / 4 \n2) 2 - 2 \n3) 0 * 4 \n4) 3 + 0")

a = 3 + 8 / 4 - 2 * 4
print("\n3 + 8 / 4 - 2 * 4 = ", a)
print("1) 8 / 4 \n2) 2 * 4 \n3) 2 - 8 \n4) 3 + -6")

a = 3 + 8 / (4 - 2 * 4)
print("\n3 + 8 / (4 - 2 * 4) = ", a)
print("1) 2 * 4 \n2) 4 - 8 \n3) 8 / -4 \n4) 3 + -2")

# Ülesanne 3
r = random.random() * 20
print(f"\nRingi raadius on {r}")
print(f"Ruudu pindala on {round((2 * r)**2, 2)}")
print(f"Ruudu ümbermõõt on {round(8 * r, 2)}")
print(f"Ringi pindala on {round(math.pi * r**2, 2)}")
print(f"Ringi ümbermõõt on {round(2*math.pi*r, 2)}")

# Ülesanne 4
mundiD = 2.575
maaR = 6378 * 100_000
Pmaa = 2 * math.pi * maaR
kogus = Pmaa / mundiD
print(f"Meil on vaja {int(kogus):,d} mündi.")
print(f"Meil on vaja {int(kogus * 2):,d} euro.")

# Ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

# Ülesanne 6
luuletus = '''Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.'''

for i in luuletus.split(",\n"):
    print(i.capitalize())

# Ülesanne 7
while True:
    try:
        print("\nRistküliku pikkused")
        a = float(input("a: "))
        b = float(input("b: "))
        print("Ümbermõõdu on ", (a + b) * 2)
        print("Pindala on ", (a * b))
        break
    except:
        print("Palun sisenda õiged andmed")

# Ülesanne 8
while True:
    try:
        print("\nKütusekulu arvutamine")
        a = float(input("Tangitud kütuse liitrid: "))
        b = float(input("Läbitud kilomeetrid: "))
        print("Keskmine kütusekulu 100km kohta on", round(a / b * 100, 2), "liitrid")
        break
    except:
        print("Palun sisenda õiged andmed")

# Ülesanne 9
while True:
    try:
        print("\nRulluisutajad")
        kiirus = 29.9
        m = float(input("Minutid: "))
        print("Keskmine rulluisutaja läbib", round(m / 60 * kiirus, 2), "km", m, "minutiga")
        break
    except:
        print("Palun sisenda õiged andmed")


# Ülesanne 10
while True:
    try:
        print("\nAjateisendus")
        m = int(input("Aeg minutites: "))
        tund = int(m/60)
        minutit = m % 60
        print(f"Aeg on {tund}:{minutit}")
        break
    except:
        print("Palun sisenda õiged andmed")