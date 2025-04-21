import requests
import json

def work():
    api_voti = "5b77075af00cf7eaba7fad26beb0f447"
    #api_voti = "4160bb7aeefe7aba552ea8aabe0224ed"
    linn = input("Sisesta linna nimi: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_voti}&q={linn}&units=metric&lang=et"
    vastus = requests.get(url)
    jsonData = vastus.json()

    if jsonData["cod"] == 404:
        print("Linna ei leitud. Palun kontrolli nime õigekirja.")
        return

    if "message" in jsonData:
        print("ERROR", jsonData["cod"])
        print(jsonData["message"])
        return
    
    peamine = jsonData["main"]
    temperatuur = peamine["temp"]
    niiskus = peamine["humidity"]
    kirjeldus = jsonData["weather"][0]["description"]
    tuul = jsonData["wind"]["speed"]
    print(f"\nIlm linnas {linn}:")
    print(f"Temperatuur: {temperatuur}°C")
    print(f"Kirjeldus: {kirjeldus.capitalize()}")
    print(f"Niiskus: {niiskus}%")
    print(f"Tuule kiirus: {tuul} m/s")

    with open("weather.json", "w", encoding="utf-8-sig") as f:
        json.dump(jsonData, f, indent=2, ensure_ascii=False)

work()