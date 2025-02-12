from random import *

#Näidis 1
arv = randint(0,10)
print(arv)

if (arv > 5):
    print("***********************")
    print(f"Arv {arv} suurem kui 5")
    print("***********************")

if (arv > 5):
    print(f"Arv {arv} suurem kui 5")

# Näidis 2
arv = randint(-10, 10)

if (arv > 0):
    print(f"Arv {arv} on positiivne")
else:
    print(f"Arv {arv} on negatiivne") #viga!

if (arv > 0):
    print(f"Arv {arv} on positiivne")
elif (arv == 0):
    print("0")
else:
     print(f"Arv {arv} on negatiivne")

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