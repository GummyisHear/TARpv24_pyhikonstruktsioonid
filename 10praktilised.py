import random
import math

# 1.
#tais = 0
# print("Sisesta 15 arved!")
# for i in range(0,15):
#     arv = input("=> ")
#     try:
#         a = int(arv)
#         tais += 1
#     except:
#         continue

# print(f"{tais} täisarved")
# print()

# 2.
# a = int(input("Sisesta A: "))
# summ = 0
# for i in range(0, a):
#     summ += i

# print(f"Summ numbridest 0-{a} on: {summ}")
# print()

# 3.
# print("Sisesta 8 arved!")
# kord = 1
# for i in range(1, 9):
#     arv = float(input("=> "))
#     if (arv > 0):
#         kord *= arv

# print("Kõikide arvude korrutis: " + str(kord))

# 4.
# print("Numbrite ruudud 10 kuni 20...")
# for i in range(10, 21):
#     print(f"{i} ** 2 = {i ** 2}")
#print()

# 5.
# print("Summ negatiivse arvedest")
# N = int(input("Sisesta N: "))
# summ = 0

# for i in range(N):
#     arv = float(input(f"Sisesta arv: "))
#     if arv < 0:
#         summ += arv

# print(f"Summ on: {summ}")
# print()

# 6.
# N = int(input("Sisesta N: "))
# neg = 0
# pos = 0
# nul = 0

# for i in range(N):
#     arv = int(input(f"Sisesta arv: "))
#     if arv < 0:
#         neg += 1
#     elif arv > 0:
#         pos += 1
#     else:
#         nul += 1

# print(f"On sisestatud {neg} negatiivsed arved, {pos} positiivsed arved, {nul} null arved")

# 7.
# A = int(input("Sisesta vahemiku algus A: "))
# B = int(input("Sisesta vahemiku lõpp B: "))
# K = int(input("Sisesta arv K: "))

# print(f"Arved, mis on jagatavad {K} vahemikus:")
# for num in range(A, B + 1):
#     if num % K == 0:
#         print(num)
# print()

# 8.
# print("Tabel tollist sentimeetrini")
# for i in range(1, 21):
#     print(f"{i} tollid = {i * 2.5} cm")

# print()

# 9.
# print("Pank")
# s = random.randint(1000, 10000)
# n = random.randint(3, 10)
# print(f"Panime {n} aastaks {s} eurot panka, 3% protsendi aastal")
# print(f"Lõpp summa on {round(s * math.pow(1.03, n), 2)} euro")

# 10.



# 14.
# print("Arvude 1-N korrutis")
# n = random.randint(5,20)
# print(f"N = {n}")
# korrutis = 1
# for i in range(1,n+1):
#     korrutis *= i
# print(f"Korrutis on {korrutis}")

# 15.
# for i in range(10):
#     for n in range(10):
#         print(n, end=" ")
#     print()

# 16.
# for y in range(9): 
#     for x in range(9):
#         if (x == y):
#             print(x+1, end=" ")
#         else:
#             print("0", end=" ")
#     print()

# 17.
# print("Korrutamise tabel")
# arv = random.randint(1, 9)
# for i in range(1, 10):
#     print(f"{arv}*{i}={arv*i}")

# 28.
# print("Loterei")
# arv = random.randint(1, 10)
# katsed = 0
# print("Arvake arv vahemikus 1-10")
# while True:
#     a = int(input("Arvake: "))
#     if (a == arv): break
#     katsed += 1

# print(f"Sa võidsid! Arv oli {arv}. Sinu katsed: {katsed}")

# 29.
# for y in range(9): 
#     for x in range(9):
#         if (x == 0 or x == y):
#             print("x", end=" ")
#         else:
#             print("0", end=" ")
#     print()




