from email.message import EmailMessage
from random import *
import smtplib
import ssl
from tkinter import filedialog

def saadaKiri():
    saaja = input("Kellele saata? ")
    teema = input("Teema: ")
    sisu = input("Sisu: ")
    server = "smtp.gmail.com"
    port = 587
    sender = "artjompoldsaar@gmail.com"
    password = input("Password: ")
    msg = EmailMessage()
    msg["Subject"] = teema
    msg["From"] = sender
    msg["To"] = saaja
    msg.set_content("""
    <!DOCTYPE html>
    <head>
    </head>
    <body>
    <h1>privet</h1>
    <p>privet,</p>
    <a href="https://artjompoldsaar1.wordpress.com/">here my wordpress</a>
    </body>
    </html>
    """, subtype="html")
    
    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    with open(fail, "rb") as f:
        fail_data = f.read()
        fail_nimi = fail.split("/")[-1]
        msg.add_attachment(fail_data, maintype="application", subtype="octet-stream", filename=fail_nimi)

    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

def loeFail(fail:str)->list:
    jarjend = []
    with open(fail, 'r', encoding="utf-8-sig") as f:
        for line in f:
            jarjend.append(line)
    return jarjend

def kirjutaFail(fail:str, jarjend:list):
    f = open(fail, 'w', encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

def failToDict(f:str): 
    riik_pealinn = {}#sõnastik {"Riik": "Pealinn"} 
    pealinn_riik = {}#sõnastik {"Pealinn": "Riik"}
    file = open(f, 'r', encoding="utf-8-sig") 

    for line in file: 
        k,v = line.strip().split('-') #k-võti, v-väärtus 
        riik_pealinn[k] = v #täidame riik_pealinn 
        pealinn_riik[v] = k #täidame pealinn_riik
    file.close() 
    return riik_pealinn, pealinn_riik 