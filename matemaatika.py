import math
import random

while True:
    try:
        raskus = int(input("Valige raskus (1 - Kerge, 2 - Keskmine, 3 - Raske): "))
        kusimused = int(input("Kui palju küsimused tahad: "))
        break
    except:
        print("Sisesta täisarved!")

if (raskus <= 1):
    tehed = ["+", "-"]
elif (raskus == 2):
    tehed = ["+", "-", "*"]
else:
    tehed = ["+", "-", "*", "/"]

oigedVastused = 0
i = 0
for i in range(0, kusimused):
    a = random.randint(5 ** raskus, 10 ** raskus)
    b = random.randint(2 ** raskus, 12 ** raskus)
    tegevus = random.choice(tehed)
    if (tegevus == "+"):
        vastus = a + b
        print(f"{i+1}.   {a} + {b} = ?")
    elif (tegevus == "-"):
        vastus = a - b
        print(f"{i+1}.   {a} - {b} = ?")
    elif (tegevus == "*"):
        vastus = a * b
        print(f"{i+1}.   {a} * {b} = ?")
    else:
        vastus = int(a / b)
        print(f"{i+1}.   {a} / {b} = ? (floor)")

    while True:
        try: 
            kasutajaVastus = int(input("Vasta: "))
            if (kasutajaVastus != vastus):
                print(f"Sinu vastus on vale! Õige vastus oli {vastus}")
            else:
                print("Õige!")
                oigedVastused += 1
            break
        except:
            print("Sisesta täisarved!")

hinne = oigedVastused / float(kusimused)
if (hinne < 0.6):
    print("Hinne 2")
elif (hinne < 0.75):
    print("Hinne 3")
elif (hinne < 0.9):
    print("Hinne 4")
else:
    print("Hinne 5!")
