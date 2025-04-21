import json

with open("andmed.json", "r", encoding="utf-8-sig") as f:
    andmed = json.load(f)
   
sisNimi = input("Sisesta nimi: ")

if (andmed.get("nimi", "Andmed ei ole!")) == sisNimi:
    print(f"\nAutod kasutajal {sisNimi}:")
    for auto in andmed.get("autod", []):
        print(f"- ({auto['muudel']} {auto['varv']} {auto['joud']}hj) #{auto['number']}")

