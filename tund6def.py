from MoodulTund6Def import *

# xorCipher funktsiooni kasutamine
s = input("Sisesta sõna: ")
k = input("Sisesta võti: ")
v = xorCipher(s, k)
print(v)

v = xorCipher(v, k)
print(v)

# date funktsiooni kasutamine
d = int(input("Sisesta päev: "))
m = int(input("Sisesta kuu: "))
a = int(input("Sisesta aasta: "))
v = date(d, m, a)
print("Kuupäev on õige!" if v == True else "Kuupäev on vale!")

# is_prime funktsiooni kasutamine

a = int(input("Sisesta arv: "))
v = is_prime(a)
if (v == True):
    print(f"{a} Arv on algarv!")
else:
    pass
    #print(f"{i} Arv ei ole algarv!")

# bank funktsiooni kasutamine
a = float(input("Sisesta summa: "))
aastad = int(input("Sisesta aastate arv: "))
summa = bank(a, aastad)
print(summa)

# season funktsiooni kasutamine
k = int(input("Sisesta kuu number: "))
v = season(k)
print(v)

# square_list funktsiooni kasutamine
sList = square_list(float(input("Sisesta ruudu külg: ")))
for x in sList:
    print(x)

# square funktsiooni kasutamine
S,P,d = square(float(input("Sisesta ruudu külg: ")))
print(S)
print(P)
print(d)

#is_year_leap funktsiooni kasutamine
aasta = int(input("Mis aasta tahad kontrollida? "))
v = is_year_leap(aasta)
if (v == True):
    print("Aasta on liigaasta!")
else:
    print("Aasta ei ole liigasta.")

# arithmetic funktsiooni kasutamine
a = float(input("Sisesta arv 1: "))
b = float(input("Sisesta arv 2: "))
t = input("Tehe: ")
v = arithmetic(a, b, t)
print(v)