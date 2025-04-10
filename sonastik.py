
from sonastikModule import *

while True:
    print("Sõnastik!!!")

    kuva_menu()

    sona = input("Sisesta sõna või menüü valik: ").strip().lower()
    valik = -1
    try:
        valik = int(sona)
    except:
        pass

    if (len(sona) == 0):
        print("Tühjad sõnad pole lubatud!")
        continue

    if (valik == -1):
        print(f"[{keel1} -> {keel2}]")
        t = tolkija(sonastik, keel1, keel2, sona)
        if (t is not None):
            print(f"{sona} -> {t}")
        else:
            print("Sõna ei leitud")

    if (valik == 0):
        print("Head aega!")
        break

    if (valik == 1):
        kuva_sonad()

    if (valik == 2):
        print("Vali keel 1: ")
        keel1 = vali_keel()
        print("Vali keel 2: ")
        keel2 = vali_keel()

    if (valik == 3):
        lisa_sona(sonastik)

    if (valik == 4):
        sona = inputSona("Sisesta sõna: ")
        otsi_sona(sona)

    if (valik == 5):
        sona = inputSona("Sisesta sõna: ")
        paranda_sona(sona)

    if (valik == 6):
        testi_sonad()

    if (valik == 7):
        kuva_tulemused()

    if (valik == 8):
        juhuslik_sona()

    print()