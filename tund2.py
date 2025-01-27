from datetime import *
import calendar
import random
import math

tana = date.today()
print(f"Täna on {tana}")

# 27/12/2022
#tana = tana.strftime("%d/%m/%Y")

# December 27, 2022
#tana = tana.strftime("%B %d, %Y")

# 12/27/22
#tana = tana.strftime("%m/%d/%y")

# Dec-27-2022
#tana = tana.strftime("%b-%d-%Y")

aastaLopp = date(tana.year, 12, 31)
print(f"Aasta lõpp on {aastaLopp}")

aastaPaevad = aastaLopp - tana
print(f"Aasta lõppu on jäänud {aastaPaevad.days} päeva")

res = calendar.monthrange(tana.year, tana.month)
paevadKuus = res[1]
print(f"Kuus on {paevadKuus} päeva")

kuuPaevad = paevadKuus - tana.day
print(f"Kuu lõppu on jäänud {kuuPaevad} päeva")

# Ülesanne 2
a = 3 + 8 / (4 - 2) * 4
print("\n3 + 8 / (4 - 2) * 4 = ", a)
print("\n1) 4 - 2 \n2) 8 / 2 \n3) 4 * 4 \n4) 3 + 16")

a = 3 + (8 / 4 - 2) * 4
print("\n3 + (8 / 4 - 2) * 4 = ", a)
print("1) 8 / 4 \n2) 2 - 2 \n3) 0 * 4 \n4) 3 + 0")

a = 3 + 8 / 4 - 2 * 4
print("\n3 + 8 / 4 - 2 * 4 = ", a)
print("1) 8 / 4 \n2) 2 * 4 \n3) 2 - 8 \n4) 3 + -6")

a = 3 + 8 / (4 - 2 * 4)
print("\n3 + 8 / (4 - 2 * 4) = ", a)
print("1) 2 * 4 \n2) 4 - 8 \n3) 8 / -4 \n4) 3 + -2")

# Ülesanne 3
r = random.random() * 20
print(f"\nRingi raadius on {r}")
print(f"Ruudu pindala on {round((2 * r)**2, 2)}")
print(f"Ruudu ümbermõõt on {round(8 * r, 2)}")
print(f"Ringi pindala on {round(math.pi * r**2, 2)}")
print(f"Ringi ümbermõõt on {round(2*math.pi*r, 2)}")
