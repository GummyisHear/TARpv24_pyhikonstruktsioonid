import random

# Variant 1
#1. Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n елок.
puuosad = [
    "   /v\   ",
    "  / v \  ",
    " / v v \ ",
    "/vv v vv\\"
]

while True:
    try:
        arve = int(input("Kui palju jõulupuud tahad? (1-9) "))
        if (arve > 9 or arve < 1):
            print("Lubatud ainult arved 1-9!")
            continue
        break
    except:
        print("Sisesta täisarved!")

for osa in puuosad:
    for i in range(arve):
        print(osa, end =" ")
    print()

# 2. Перемножить все не чётные значения в диапазоне от 0 до введенного пользователем числа(R);

while True:
    try:
        R = int(input("Sisesta R (0-...): "))
        if (R < 0):
            print("Lubatud ainult positiivsed arved!")
            continue
        break
    except:
        print("Sisesta täisarved!")

kord = 1
for i in range(R):
    if (i % 2 != 0):
        kord *= i

print(f"Korrutis on: {kord}")

# 3. Дано N чисел. Найти количество положительных чисел среди них; N рандомное число

N = random.randint(1, 10)
pos = 0
print(f"Palun sisesta {N} täisarved.")

for i in range(N):
    while True:
        try:
            arv = int(input(f"{i+1}) "))
            if (arv > 0):
                pos += 1
            break
        except:
            print("Sisesta täisarved!")

print(f"Positiivsed arved kokku on {pos}")

# 4. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

while True:
    try:
        Narv = int(input("Sisesta naturaal arv: "))
        if (Narv < 1):
            print("Naturaal arved alustavad 1-st!")
            continue
        break
    except:
        print("Sisesta täisarved!")

paaris = 0
paaritu = 0
for i in range(len(str(Narv))):
    stringArv = str(Narv)
    iArv = int(stringArv[i])
    if iArv % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

print(f"Arves {Narv} on {paaris} paaris arved ja {paaritu} paaritu arved")

# 5. Найти сумму ряда чисел от A до B. Полученный результат вывести на экран;

print("Sisesta A-B arve rida.")
while True:
    try:
        A = int(input("Sisesta A: "))
        B = int(input("Sisesta B: "))
        if (B <= A):
            print("B peaks olema suurem kui A!")
            continue
        break
    except:
        print("Sisesta täisarved!")

summ = 0
for i in range(A, B):
    summ += i
print(f"Summ arvedest {A}-{B} on {summ}")




