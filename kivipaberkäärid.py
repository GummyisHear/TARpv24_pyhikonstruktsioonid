import random

kasutajaNimi = input("Sisesta oma nimi: ")
arvutiNimi = "Arvuti"
valikuid = ["kivi", "paber", "käärid"]

tulemused = {
    kasutajaNimi: 0,
    arvutiNimi: 0
    }

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

    kasutajaValik = kasutajaValik - 1

    if (random.random() < 0.8):
        arvutiValik = random.randint(0, 2)
    else:
        arvutiValik = (kasutajaValik + 1) % 3

    print(f"{kasutajaNimi} valis: {valikuid[kasutajaValik]}")
    print(f"Arvuti valis: {valikuid[arvutiValik]}")

    if kasutajaValik == arvutiValik:
        print("Viik!")
        tulemused[kasutajaNimi] += 1
        tulemused[arvutiNimi] += 1
    elif (kasutajaValik == (arvutiValik - 1) % 3):
        print("Kaotasid!")
        tulemused[arvutiNimi] += 1
    else:
        print("Võitsid!")
        tulemused[kasutajaNimi] += 1
    print()

print("\n=== Mäng läbi!!! ===")
print("Tulemused:")
for nimi, tulemus in tulemused.items():
    print(f"{nimi}: {tulemus}")