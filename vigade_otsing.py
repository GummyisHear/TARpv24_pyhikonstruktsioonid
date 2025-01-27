# vahetasin "import * from math" väärtuseks "import math", sest kasutame nii "math.sqrt"
import math
print("Ruudu karakteristikud")
while True:
    a=input('Sisesta ruudu külje pikkus => ')
    try:
        a = float(a)
        if (a <= 0):
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")

S=a**2
print("Ruudu pindala", S)
P=4*a
# muutusin '' väärtuseks "
print("Ruudu ümbermõõt", P)
# viga funktsiooni nimega, muudisin "sqr" väärtuseks "sqrt"
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
# eemaldasin lisa ")"
print("Ristküliku karakteristikud")
while True:
    b=input("Sisesta ristküliku 1. külje pikkus => ")
    c=input("Sisesta ristküliku 2. külje pikkus => ")
    try:
        b = float(b)
        c = float(c)
        if (b <= 0 or c <= 0):
            print("Pikkus peab olema suurem kui 0")
            continue
        break
    except:
        print("Palun sisesta õige number")

S=b*c
# algusesse lisatud '
print('Ristküliku pindala', S)
# lisan * korrustamiseks
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
# muutusin kõik * väärtuseks **, sest kasutame Pifagoori teoreem
di=math.sqrt(b**2+c**2)
# lisan ")" lõpuni, lisan 1 koht pärast koma
print("Ristküliku diagonaal", round(di, 1))
print()
print("Ringi karakteristikud")
# muutusin kõik '' väärtuseks " ja eemaldasin lisa ")"
while True:
    r=input("Sisesta ringi raadiusi pikkus => ")
    try:
        if (r <= 0):
            print("Raadius peab olema suurem kui 0")
            continue
        r = float(r)
        break
    except:
        print("Palun sisesta õige number")

# lisasin * korrustamiseks
d=2*r
# lisasin ,
print("Ringi läbimõõt", d)
# muutusin pi() väärtuseks math.pi, sest pi ei ole funktsioon
# muutusin r*2 väärtuseks r**2, sest ringi pindala formula kasutab seda
S=math.pi*r**2
#lisan 2 kohte pärast koma
print("Ringi pindala", round(S, 2))
# lisasin * korrustamiseks, muutusin pi() väärtuseks math.pi, sest pi ei ole funktsioon
C=2 * math.pi * r
# lisasin ")" lõpuni, lisan 2 kohte pärast koma
print("Ringjoone pikkus", round(C, 2))
