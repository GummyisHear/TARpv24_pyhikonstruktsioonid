
print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = abs(int(input("Sisesta täisarv => "))) # abs() oli kinnitamata
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Pole midagi nulliga teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c = b = a # oli kasutatud operator ==, aga me loome muutujad, peaks olema =
    paaris = 0
    paaritu = 0
    while b > 0: # ; -> :
        if b % 2 == 0: # = -> ==
            paaris =+ 1 # oli liiga palju Tab'e
        else:
            paaritu =+ 1
        b = b // 10 # see oli tehtud ainult kui meil oli paaritu arv, ja programm oli lõpmatult tsüklis kui on paaris arv
    
    print(f"Paaris arved: {paaris}") # võib olla print("..." + str(...)), aga pole print("..."paaris)
    print(f"Paaritu arved: {paaritu}")
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0: # : oli puudu
        number = a % 10
        a = a // 10
        b = b * 10
        b += number # oli üks tühik liiga palju, =+ -> +=
    print("*Ümberpööratud* arv ", b) # lisan üks tühik et arv oleks paremini loetav
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreem")
    print()

    # printid oli siin aga nad peavad olema tsüklis

    while c != 1:
        if c % 2 == 0: # = -> ==
            print(c, " - paaris arv. jagame 2.")
            c = int(c / 2) # oli liiga palju Tab'e, == -> =
        else:
            print(c, " - paaritu arv. korrutame 3, liidame 1 ja jagame 2.")
            c = int((3*c + 1) / 2)
        #print(c) # end=" oli kinnitamata, == -> =, seda printi ei kasuta sest ei ole vaja

    print(c, " - Teoreem on tõestatud") # '' -> ", lisan arv c printimine