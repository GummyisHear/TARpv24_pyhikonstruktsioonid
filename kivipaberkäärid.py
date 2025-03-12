import random

kasutajaNimi = input("Sisesta oma nimi: ")
arvutiNimi = "Arvuti"
valikuid = ["kivi", "paber", "käärid"]

kasutajaTulemus = 0
arvutiTulemus = 0

print("Mängime Kivi-Paber-Käärid 5 korda!")

for i in range(5):
    while True:
        try:
            kasutajaValik = int(input("Sisesta 1 - kivi, 2 - paber või 3 - käärid: "))
            if (kasutajaValik not in (1, 2, 3)):
                print("Vali number 1, 2 või 3!")
                continue
            break
        except:
            print("Vali number 1, 2 või 3!")

    # Kasutaja valik muutub indeksiks
    kasutajaValik = kasutajaValik - 1

    # 80% tõenäosusega arvuti valib juhuslikult
    if (random.random() < 0.8):
        arvutiValik = random.randint(0, 2)
    else:
        # Valime et võidab arvuti. Järgmine valik järjes alati võidab eelmist
        arvutiValik = (kasutajaValik + 1) % 3

    print(f"{kasutajaNimi} valis: {valikuid[kasutajaValik]}")
    print(f"Arvuti valis: {valikuid[arvutiValik]}")

    if kasutajaValik == arvutiValik:
        print("Viik!")
        kasutajaTulemus += 1
        arvutiTulemus += 1
    elif (kasutajaValik == (arvutiValik - 1) % 3):
        print("Kaotasid!")
        arvutiTulemus += 1
    else:
        print("Võitsid!")
        kasutajaTulemus += 1
    print()

print("\n=== Mäng läbi!!! ===")
print("Tulemused:")
print(f"{kasutajaNimi}: {kasutajaTulemus} võitu")
print(f"{arvutiNimi}: {arvutiTulemus} võitu")

if (kasutajaTulemus > arvutiTulemus):
    print("SINA VÕITSID!!!")
else:
    print("Sina kaotasid...")