from math import pi, sqrt

# Harjutus 1
print("Tere, maailm!")
nimi = input("Mis on sinu nimi?\n")
print("Tere, maailm! Tervitan sind", nimi, "!")
vanus = input("Kui vana sa oled?\n")
print("Tere, maailm! Tervitan sind", nimi, "! Sa oled", vanus, "aastat vana.")
print("\n")

# Harjutus 2
vanus = 18 # int
eesnimi = "Jaak" # string
pikkus = 16.5 # float
kas_kaib_koolis = True # Boolean, võib olla ka False

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_kaib_koolis))
print("\n")

# Harjutus 3
kommid = 10
print("Lauas on", kommid, "kommid")
vota = int(input("Kui palju kommid sa tahad ära võtta?\n"))
kommid -= vota
print("Lauas on nüüd", kommid, "kommid")
print("\n")

# Harjutus 4
C = float(input("Mis on puude ümbermõõt?\n"))
d = C / pi
print("Puu diameter on:", d)
print("\n")

# Harjutus 5
print("Sisestage ristkülike mõõtmed")
n = float(input("N: "))
m = float(input("M: "))
c = sqrt(n**2 + m**2)
print("Diagonaal on", c)
print("\n")

# Harjutus 7
summ = 0
for i in range(5):
    summ += int(input(f"Sisesta number {i+1}: "))

print("Aritmeetiline Keskmine on ", summ / 5)
print("\n")

# Harjutus 8
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print(" ^^ \"\" ^^  ")


