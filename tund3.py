from datetime import date
from random import *

#Näidis 1
# arv = randint(0,10)
# print(arv)

# if (arv > 5):
#     print("***********************")
#     print(f"Arv {arv} suurem kui 5")
#     print("***********************")

# if (arv > 5):
#     print(f"Arv {arv} suurem kui 5")

# # Näidis 2
# arv = randint(-10, 10)

# if (arv > 0):
#     print(f"Arv {arv} on positiivne")
# else:
#     print(f"Arv {arv} on negatiivne") #viga!

# if (arv > 0):
#     print(f"Arv {arv} on positiivne")
# elif (arv == 0):
#     print("0")
# else:
#      print(f"Arv {arv} on negatiivne")

# Ülesanne 1 Juku
print("\nÜlesanne 1")

nimi = input("MIS ON SINU NIMI? ")
if (nimi.isupper() and nimi.lower() == "juku"):
    print("Lähme kinno")
    try:
        vanus = int(input("Kui vana sa oled? "))
        if vanus < 0:
            pilet = "!!!"
        elif vanus < 6:
            pilet="Tasuta"
        elif vanus <= 14:
            pilet = "Lastepilet"
        elif vanus <= 65:
            pilet = "Täospilet"
        elif vanus <= 100:
            pilet = "Sooduspilet"
        print("Sinu pilet on " + pilet)
    except:
        print("bug!")
else:
    print("Ma olen hõivatud")

# Ülesanne 2 Pinginaabrid
print("\nÜlesanne 2")

nimi1 = input("Mis on sinu nimi: ")
nimi2 = input("Sisesta teine nimi: ")
if (nimi1.isalpha() and nimi2.isalpha() and ("artjom" and "nikita" in [nimi1.lower(), nimi2.lower()])):
    print("Olete pinginaabrid!")
else:
    print("Ei ole pinginaabrid!")

# Ülesanne 3 Remont
print("\nÜlesanne 3")

a = float(input("Sisesta toa pikkus a: "))
b = float(input("Sisesta toa pikkus b: "))
S = a * b
print(f"Sinu toa pindala on {S} ruutmeetrit")
remont = input("Kas teeme remonti? (y/n) ")
if (remont.lower() == "y"):
    kulu = float(input("Kui palju maksab 1 ruutmeeter? "))
    print(f"Remondi kulu on {S * kulu} eurot")

# Ülesanne 4 Allahindus
print("\nÜlesanne 4")

hind = int(input("Sisesta toote hind: "))
if (hind > 700):
    hind = hind * 0.7
    print ("Sa saad 30% allahindlust! Uus hind on: " + str(hind))
else:
    print("Sa ei saa allahindlust!")

# Ülesanne 5 Temperatuur
print("\nÜlesanne 5")

temp = int(input("Sisesta temperatuur: "))
if (temp > 18):
    print("On soovitav toasoojus talvel")
else:
    print("Ei ole soovitav")

# Ülesanne 6 Pikkus
print("\nÜlesanne 6")

pikkus = int(input("Sisesta oma pikkus: "))
if (pikkus > 180):
    print("Sa oled pikk")
elif (pikkus > 160):
    print("Sa oled keskmise pikkusega")
else:
    print("Sa ei ole pikk")

# Ülesanne 7 Pikkus ja sugu
print("\nÜlesanne 7")
pikkus = int(input("Sisesta oma pikkus: "))
sugu = input("Sisesta oma sugu (mees/naine): ")
if (sugu.lower() == "mees"):
    print(f"Sa oled {'suur' if pikkus > 180 else 'keskmise pikkusega' if pikkus > 160 else 'väike'} mees")
elif (sugu.lower() == "naine"):
    print(f"Sa oled {'suur' if pikkus > 170 else 'keskmise pikkusega' if pikkus > 150 else 'väike'} naine")

# Ülesanne 8 Poes
print("\nÜlesanne 8")

tsekk = 0
if (input("Soovid piima osta? (y/n) ") == "y"):
    tsekk += 0.6 * int(input("Kui palju: "))
if (input("Soovid saia osta? (y/n) ") == "y"):
    tsekk += 0.8 * int(input("Kui palju: "))
if (input("Soovid leiva osta? (y/n) ") == "y"):
    tsekk += 0.6 * int(input("Kui palju: "))

# print("Sinu tšekk on " + str(tsekk) + " eurot")

# Ülesanne 9 Ruut
print("\nÜlesanne 9")

a = int(input("Sisesta ruudu esimene külg: "))
b = int(input("Sisesta ruudu teine külg: "))
c = int(input("Sisesta ruudu kolmas külg: "))
d = int(input("Sisesta ruudu neljas külg: "))
if (a == b == c == d):
    print("On õige ruut")
else:
    print("Ei ole ruut")

# Ülesanne 10 Matemaatika
print("\nÜlesanne 10")

a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))
op = input("Mis operatsioon soovid teha (+, -, *, /): ")
if (op == "+"):
    print(f"Vastus on {a + b}")
elif (op == "-"):
    print(f"Vastus on {a - b}")
elif (op == "*"):
    print(f"Vastus on {a * b}")
elif (op == "/"):
    print(f"Vastus on {a / b}")

# 11. Juubel
print("\n11. Sisesta oma sünnipaev")
d = int(input("Päev: "))
m = int(input("Kuu: "))
y = int(input("Aasta: "))
if ((date.today().year - y) % 10 == 0):
    print("Sul on juubel!")
else:
    print("Sul ei ole juubel.")

# 12. Müük
print("\n12. Müük")
p = float(input("Siesta toode hind: "))
if (p < 10):
    print("Saad 10% allahindlus!")
    print(f"Lõpp hind: {p * 0.9}")
else:
    print("Saad 20% allahindlus!")
    print(f"Lõpp hind: {p * 0.8}")

# 13. Jalgpalli meeskond
print ("\n13. jalgpalli meeskond")
sugu = input("sisesta oma sugu (m/n): ")
if (sugu.lower() == "m"):
    vanus = int(input("kui vana sa oled: "))
    if (vanus >= 16 and vanus <= 18):
        print("sina sobib!")
    else:
        print("sina ei sobi.")
elif (sugu.lower() == "n"):
    print("sina sobib!")
else:
    print("vale sugu.")

# 14. Busside logistika
print("\n14. Busside logistika")
i = int(input("Kui palju inimesed on: "))
b = int(input("Kui palju inimesed mahub bussile: "))
print(f"Et transportida kõik inimesed meil on vaja {i // b} täis bussid, ja 1 buss kus on {i % b} inimesed.")

