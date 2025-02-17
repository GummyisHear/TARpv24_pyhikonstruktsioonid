import math

print("Tere! olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")

while True:
    try:
        soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah:"))
        if (soov == 1):
            while True:
                try:
                    pikkus = int(input("Kui pikk sa oled: "))
                    break
                except:
                    print("Vale pikkuse formaat!")
            
            while True:
                try:
                    mass = float(input("Kui palju sa kaalub: "))
                    break
                except:
                    print("Vale kaalu formaat!")

            indeks = mass / math.pow(0.01 * pikkus, 2)
            print(f"{nimi}! Sinu keha indeks on: {round(indeks, 1)}")

            if (indeks < 16):
                print("Hinnang: Tervisele ohtlik alakaal")
            elif (indeks < 19):
                print("Hinnang: Alakaal")
            elif (indeks < 25):
                print("Hinnang: Normaalkaal")
            elif (indeks < 30):
                print("Hinnang: Ülekaal")
            elif (indeks < 35):
                print("Hinnang: Rasvumine")
            elif (indeks < 40):
                print("Hinnang: Tugev rasvumine")
            else:
                print("Hinnang: Tervisele ohtlik rasvumine")

        elif (soov == 0):
            print("Kahju! See on väga kasulik info!")
            print()
        else:
            print("Vale soov!")
            continue

        print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
        break
    except:
        print("idioot")
