import random
import math

# 1.
print("Ülesanne 1.")
tais = 0
print("Sisesta 15 arved!")
for i in range(0,15):
    while True:
        try:
            arv = float(input(f"{i+1} => "))
            break
        except:
            print("Sisesta reaal arv!")
            continue
    try:
        a = int(arv)
        tais += 1
    except:
        continue

print(f"{tais} täisarved")
print()

# 2.
print("Ülesanne 2.")
while True:
    try:
        a = int(input("Sisesta täisarv A: "))
        break
    except:
        print("Sisesta täisarv!")
summ = 0
for i in range(0, a):
    summ += i

print(f"Summ numbridest 0-{a} on: {summ}")
print()

# 3.
print("Ülesanne 3.")
print("Sisesta 8 arved!")
kord = 1
for i in range(1, 9):
    while True:
        try:
            arv = float(input("=> "))
            break
        except:
            print("Sisesta reaal arv!")
            continue
    if (arv > 0):
        kord *= arv

print("Kõikide arvude korrutis: " + str(kord))
print()

# 4.
print("Ülesanne 4.")
print("Numbrite ruudud 10 kuni 20...")
for i in range(10, 21):
    print(f"{i} ** 2 = {i ** 2}")
print()

# 5.
print("Ülesanne 5.")
print("Summ negatiivse arvedest")
while True:
    try:
        N = int(input("Kui palju arved tahad sisestada: "))
        break
    except:
        print("Sisesta täis arv!")
summ = 0

for i in range(N):
    while True:
        try:
            arv = float(input(f"Sisesta arv: "))
            break
        except:
            print("Sisesta reaal arv!")
            continue
    if arv < 0:
        summ += arv

print(f"Summ on: {summ}")
print()

# 6.
print("Ülesanne 6.")
while True:
    try:
        N = int(input("Kui palju arved tahad sisestada: "))
        break
    except:
        print("Sisesta täis arv!")
neg = 0
pos = 0
nul = 0

for i in range(N):
    while True:
        try:
            arv = int(input("Sisesta arv: "))
            break
        except:
            print("Sisesta täis arv!")
            continue
    if arv < 0:
        neg += 1
    elif arv > 0:
        pos += 1
    else:
        nul += 1

print(f"On sisestatud {neg} negatiivsed arved, {pos} positiivsed arved, {nul} null arved")
print()

# 7.
print("Ülesanne 7.")
while True:
    try:
        A = int(input("Sisesta vahemiku algus A: "))
        break
    except:
        print("Sisesta täis arv!")
while True:
    try:
        B = int(input("Sisesta vahemiku lõpp B: "))
        break
    except:
        print("Sisesta täis arv!")
while True:
    try:
        K = int(input("Sisesta arv K: "))
        break
    except:
        print("Sisesta täis arv!")

print(f"Arved, mis on jagatavad {K} vahemikus:")
for num in range(A, B + 1):
    if num % K == 0:
        print(num)
print()

# 8.
print("Ülesanne 8.")
print("Tabel tollist sentimeetrini")
for i in range(1, 21):
    print(f"{i} tollid = {i * 2.5} cm")

print()

# 9.
print("Ülesanne 9.")
print("Pank")
s = random.randint(1000, 10000)
n = random.randint(3, 10)
print(f"Panime {n} aastaks {s} eurot panka, 3% protsendi aastal")
print(f"Lõpp summa on {round(s * math.pow(1.03, n), 2)} euro")
print()

# 10.
print("Ülesanne 10.")
for i in range(10):
    while True:
        try:
            a = int(input("Sisesta esimene arv: "))
            break
        except:
            print("Sisesta täis arv!")
    while True:
        try:
            b = int(input("Sisesta teine arv: "))
            break
        except:
            print("Sisesta täis arv!")
    if (a > b): print(f"{a} on suurem kui {b}")
    elif (a < b): print(f"{b} on suurem kui {a}")
    else: print(f"Numbrid on võrdsed")
print()

# 14.
print("Ülesanne 14.")
print("Arvude 1-N korrutis")
n = random.randint(5,20)
print(f"N = {n}")
korrutis = 1
for i in range(1,n+1):
    korrutis *= i
print(f"Korrutis on {korrutis}")
print()

# 15.
print("Ülesanne 15.")
for i in range(10):
    for n in range(10):
        print(n, end=" ")
    print()
print()

# 16.
print("Ülesanne 16.")
for y in range(9): 
    for x in range(9):
        if (x == y):
            print(x+1, end=" ")
        else:
            print("0", end=" ")
    print()

# 17.
print("Ülesanne 17.")
print("Korrutamise tabel")
arv = random.randint(1, 9)
for i in range(1, 10):
    print(f"{arv}*{i}={arv*i}")
print()

# 18.
print("Ülesanne 18.")
print("täisarved 20-50")
for i in range(20, 51):
    if (i % 3 == 0 and i % 5 != 0):
        print(f"{i} jagub 3-ga ja ei jaga 5-ga")
print()

# 23.
print("Ülesanne 23.")
r = random.randint(8, 16)
rS = r ** 2
a = random.randint(-10, 10)
b = random.randint(-10, 10)
print(f"Ring raadiusega {r}, koordinaatides ({a},{b})")
while True:
    try:
        n = int(input("Kui palju puktid tahad sisestada: "))
        break
    except:
        print("Sisesta täis arv!")
c = 0
for i in range(n):
    while True:
        try:
            x = int(input("Sisesta x: "))
            break
        except:
            print("Sisesta täis arv!")
    while True:
        try:
            y = int(input("Sisesta y: "))
            break
        except:
            print("Sisesta täis arv!")
    dx = x - a
    dy = y - b
    if (dx ** 2 + dy ** 2 <= rS):
        print("Punkt jääb ringi sisse!")
        c += 1
    else:
        print("Punkt ei jää ringi sisse.")

print(f"Kokku on {c} punktid mis jäävad ringi sisse.")
print()

# 28.
print("Ülesanne 28.")
print("Loterei")
arv = random.randint(1, 10)
katsed = 0
print("Arvake arv vahemikus 1-10")
while True:
    while True:
        try:
            a = int(input("Arvake: "))
            break
        except:
            print("Sisesta täis arv!")
            continue
    if (a == arv): break
    katsed += 1

print(f"Sa võidsid! Arv oli {arv}. Sinu katsed: {katsed}")
print()

# 29.
print("Ülesanne 29.")
for y in range(9): 
    for x in range(9):
        if (x == 0 or x == y):
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()
print()

# 30.
print("Ülesanne 30.")
n = random.randint(1, 10)
m = random.randint(20, 30)
print(f"N = {n}, M = {m}")
print("N kuni M:")
for i in range(n, m+1):
    print(i, end=" ")

print()
print("M kuni N:")
for i in range(m, n-1, -1):
    print(i, end=" ")
print()

# 31.
print("Ülesanne 31.")
print("Spongebob praeb kotlette.")
k = random.randint(15, 50)
m = random.randint(4,8)
print(f"Tal on {k} kotlette ja pannile mahub {m} kotlette")
print(f"On vaja praeda {k // m} täis pannid, ja {k % m} kotletid jäävad ära")
print()
