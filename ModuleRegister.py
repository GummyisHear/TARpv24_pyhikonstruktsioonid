import string
import random
import os
from email.message import EmailMessage
import smtplib
import ssl
from tkinter import filedialog

usernames = [ "artjomProGamer" ]
passwords = [ "1234" ]
loggedIn = -1

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

    usernames.append(username)
    passwords.append(password)
    sendMail("artjompoldsaar@gmail.com", "Registered", f"Welcome {username}! Thanks for registering.")

def loginId(user:str, password:str)->int:
    for i in range(len(usernames)):
        if usernames[i] == user and passwords[i] == password:
            return i

    return -1

def inputNewUsername(text:str)->str:
    while True:
        username = input(text)
        if username in usernames:
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