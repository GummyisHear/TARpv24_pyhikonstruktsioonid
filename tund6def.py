from MoodulTund6Def import *

# squaer_list funktsiooni kasutamine
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