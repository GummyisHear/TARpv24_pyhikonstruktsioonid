import string
import random
import os
from email.message import EmailMessage
import smtplib
import ssl
from tkinter import filedialog

auths = {
    "artjom": "1234"    
}
loggedIn = ""

def randomPassword(length:int = 8)->str:
    chars = string.ascii_letters + string.digits
    l = list(chars)
    random.shuffle(l)
    return ''.join(l[:length])

def clearOneLine():
    print("\033[A" + (" " * os.get_terminal_size().columns) + "\033[A")

def menuChoice()->int:
    while True:
        try:
            choice = int(input("Valik: "))
            if choice >= 0 and choice <= 5:
                break
            else:
                clearOneLine()
                clearOneLine()
                print("Vale valik!")
        except:
            clearOneLine()
            clearOneLine()
            print("Vale valik!")

    return choice

def register()->any:
    username = inputNewUsername("Kasutajanimi: ")
    if (inputYesNo("Kas soovite genereerida parooli? (y/n): ")):
        password = randomPassword(3)
        print("Parool: " + password)
    else:
        password = input("Parool: ")

    auths[username] = password
    sendMail("artjompoldsaar@gmail.com", "Registered", f"Welcome {username}! Thanks for registering.")

def loginId(user:str, password:str)->str:
    if (user in auths and auths[user] == password):
        return user
       
    return ""

def inputNewUsername(text:str)->str:
    while True:
        username = input(text)
        if username in auths:
            print("See kasutajanimi on juba kasutatud.")
        else:
            return username

def inputYesNo(text:str)->bool:
    while True:
        choice = input(text)
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Vale valik!")

def sendMail(to:str, subj:str, content:str):
    server = "smtp.gmail.com"
    port = 587
    sender = "artjompoldsaar@gmail.com"
    password = ""
    msg = EmailMessage()
    msg["Subject"] = subj
    msg["From"] = sender
    msg["To"] = to
    msg.set_content(content)
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

def readFile():
    with open("auths.txt", 'r', encoding="utf-8-sig") as f:
        for line in f:
            user, password = line.split(":")
            auths[user] = password.strip()
    print("Fail loetud.")

def saveFile():
    with open("auths.txt", 'w', encoding="utf-8-sig") as f:
        for user, password in auths.items():
            f.write(f"{user}:{password}" + "\n")

    print("Fail salvestatud.")
