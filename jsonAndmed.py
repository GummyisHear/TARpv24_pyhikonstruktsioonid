from encodings.utf_8_sig import encode
import json

andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

with open("andmed.json", "w") as f:
    json.dump(andmed, f)

with open("andmed.json", "r") as f:
    andmed_failist = json.load(f)
    print(andmed_failist)


klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Jüri", "hinne": 4}
]}

json_string = json.dumps(klass, indent=2, sort_keys=True, ensure_ascii=False)
print(json_string)

with open("klass.json", "w", encoding="utf-8-sig") as f:
    json.dump(klass, f)