import imghdr
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from turtle import back, color, width
import matplotlib.pyplot as plt
import numpy as np
import os
from email.message import EmailMessage
import smtplib
import ssl
import tkinter as tk
from ttkbootstrap import *

WIDTH = 470
HEIGHT = 470

file_attachments = list()

def createWindow(title)->Window:
    aken = Window(title, size=(WIDTH, HEIGHT))
    aken.style.theme_use('minty')
    aken.title(title)
    aken.geometry(f"{WIDTH}x{HEIGHT}")
    #aken.configure(bg="lightblue")
    #aken.resizable(False, False)
    aken.iconbitmap("icon.ico")
    return aken

def choosePictures():
    files = filedialog.askopenfilenames()
    lisaLabel.configure(text=str(len(file_attachments) + len(files)) + " failid")
    return files

def attachment():
    global file_attachments
    for file in choosePictures():
        file_attachments.append(file)

def sendMail(to:str, subj:str, content:str, files:list, password:str):
    server = "smtp.gmail.com"
    port = 587
    sender = "artjompoldsaar@gmail.com"
    msg = EmailMessage()
    msg["Subject"] = subj
    msg["From"] = sender
    msg["To"] = to
    msg.set_content(content)
    for file in files:
        if (file != "" and file != None and len(file) > 0):
            with open(file, "rb") as fpilt:
                pilt = fpilt.read()
                msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")
        sendBtn.config(bootstyle="danger")
        return
    
    sendBtn.config(bootstyle="success")

def mailButton():
    global file_attachments
    emails = emailEntry.get()
    teema = teemaEntry.get()
    kiri = kiriEntry.get("1.0", "end-1c") 
    password = passEntry.get()
    
    if (emails.find(",") == -1):
        sendMail(emails, teema, kiri, file_attachments, password)
    else:
        for email in emails.split(","):
            sendMail(email.strip(), teema, kiri, file_attachments, password)

def restoreMail():
    email = ""
    teema = ""
    password = ""
    kiri = None
    with open("mail_save.txt", "r") as file:
        for line in file.readlines():
            if (line.startswith("email:")):
                email = line.split(":")[1].strip()
            if (line.startswith("teema:")):
                teema = line.split(":")[1].strip()
            if (line.startswith("pass:")):
                password = line.split(":")[1].strip()
            if (line.startswith("kiri:")):
                kiri = line.split(":")[1]
                continue
            if (kiri != None):
                kiri += line

    emailEntry.insert(0, email)
    teemaEntry.insert(0, teema)
    passEntry.insert(0, password)
    if (kiri != None):
        kiriEntry.insert("1.0", kiri)
    else:
        kiriEntry.insert("1.0", "")

def on_closing():
    with open("mail_save.txt", "w") as file:
        file.write("email:" + emailEntry.get() + "\n")
        file.write("teema:" + teemaEntry.get() + "\n")
        file.write("pass:" + passEntry.get() + "\n")
        file.write("kiri:" + kiriEntry.get("1.0", "end-1c") + "\n")
    aken.destroy()

aken = createWindow("E-kirja saatmine")
aken.protocol("WM_DELETE_WINDOW", on_closing)

style = Style()
current_font = style.lookup("TButton", "font")
style.configure("TButton", font=(current_font, 20))
style.configure("TLabel", font=(current_font, 20))

label = Label(aken, text="EMAIL:", width=8, style="info")
label.grid(row=0, column=0, pady=10, padx=10)
label = Label(aken, text="TEEMA:", width=8, style="info")
label.grid(row=1, column=0, pady=10, padx=10)
label = Label(aken, text="LISA:", width=8, style="info")
label.grid(row=2, column=0, pady=10, padx=10)
label = Label(aken, text="PASS:", width=8, style="info")
label.grid(row=3, column=0, pady=10, padx=10)

label = Label(aken, text="KIRI:", width=8, style="info")
label.grid(row=4, column=0, pady=10, padx=10)

emailEntry = Entry(aken, width=20, style="TEntry", font=("Arial", 20))
emailEntry.grid(row=0, column=1, columnspan=2)
teemaEntry = Entry(aken, width=20, font=("Arial", 20))
teemaEntry.grid(row=1, column=1, columnspan=2)
lisaLabel = Label(aken, font=("Arial", 20), width=20, relief="solid", borderwidth=2, style="secondary")
lisaLabel.grid(row=2, column=1, columnspan=2, ipady=5, ipadx=5)
passEntry = Entry(aken, width=20, font=("Arial", 20))
passEntry.grid(row=3, column=1, columnspan=2)
kiriEntry = ScrolledText(aken,  width=19, height=5, font=("Arial", 20))
kiriEntry.grid(row=4, column=1, columnspan=2, rowspan=1)

btn = Button(aken, text="LISA PILT", command=attachment)
btn.grid(row=5, column=1, padx=10, pady=10)
sendBtn = Button(aken, text="SAADA", command=mailButton)
sendBtn.grid(row=5, column=2, padx=10, pady=10)

restoreMail()

aken.mainloop()