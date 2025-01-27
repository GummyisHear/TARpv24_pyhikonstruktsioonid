from datetime import *
import calendar

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