from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

WIDTH = 400
HEIGHT = 400

def createWindow(title)->Tk:
    aken = Tk()
    aken.title(title)
    aken.geometry(f"{WIDTH}x{HEIGHT}")
    aken.configure(bg="lightblue")
    aken.resizable(False, False)
    aken.iconbitmap("icon.ico")
    return aken

def getInputValue(entry:Entry, default):
    if (entry.get() == ""):
        return default

    return float(entry.get())

def getInputs():
    try:
        a = getInputValue(aInput, 1)
    except ValueError:
        aInput.config(bg="red", fg="white")
        answer.config(text="Viga sisendis!", bg="red", fg="white")
        return
    try:
        b = getInputValue(bInput, 1)
    except ValueError:
        bInput.config(bg="red", fg="white")
        answer.config(text="Viga sisendis!", bg="red", fg="white")
        return

    try:
        c = getInputValue(cInput, 0)
    except ValueError:
        cInput.config(bg="red", fg="white")
        answer.config(text="Viga sisendis!", bg="red", fg="white")
        return

    return a, b, c

def calculate():
    print("Arvutame...")

    aInput.config(bg="white", fg="black")
    bInput.config(bg="white", fg="black")
    cInput.config(bg="white", fg="black")
    answer.config(bg="yellow", fg="green")

    try:
        a, b, c = getInputs()
    except:
        return

    print(f"Arvutame {a}x^2 + {b}x + {c} = 0")

    delta = b**2-4*a*c
    lahendus = ""
    if (delta == 0):
        x1 = -b/(2*a)
        lahendus = f"x = {x1}"
    elif (delta > 0):
        x1 = round((-b + delta**0.5)/(2*a), 3)
        x2 = round((-b - delta**0.5)/(2*a), 3)
        lahendus = f"x1 = {x1}, x2 = {x2}"
    else:
        lahendus = "Lahendusi pole!"


    answer.config(text=f"{a}x^2 + {b}x + {c} = 0\nD = {delta}\n{lahendus}")

def getPorabolaHeight(a, b, c):
    x = -b / (2 * a)
    y = a * x**2 + b * x + c
    return x, y

def graph():
    try:
        a = getInputValue(aInput, 1)
        b = getInputValue(bInput, 1)
        c = getInputValue(cInput, 0)
    except ValueError:
        answer.config(text="Viga sisendis!", bg="red", fg="white")
        return

    if (a != 0):
        centerX, centerY = getPorabolaHeight(a, b, c)
    else:
        centerX, centerY = 0, 0

    x_vals = np.linspace(centerX-10, centerX+10, 400)

    y_vals = a * x_vals**2 + b * x_vals + c

    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Graafik')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.legend()
    
    plt.show()

aken = createWindow("Ruutvõrrandi lahendamine")

header = Label(aken, text="Ruutvõrrandi lahendamine", font=("Arial", 20), bg="blue", fg="green")
header.pack(pady=20)

eqFrame = Frame(aken, bg = "lightblue")
eqFrame.pack()

aInput = Entry(eqFrame, font=("Arial", 16), bg="white", fg="black", width=3)
bInput = Entry(eqFrame, font=("Arial", 16), bg="white", fg="black", width=3)
cInput = Entry(eqFrame, font=("Arial", 16), bg="white", fg="black", width=3)
eq1 = Label(eqFrame, text="x^2 + ", font=("Arial", 16), bg="lightblue", fg="black")
eq2 = Label(eqFrame, text="x + ", font=("Arial", 16), bg="lightblue", fg="black")
eq3 = Label(eqFrame, text="= 0", font=("Arial", 16), bg="lightblue", fg="black")
calcButton = Button(eqFrame, text="Arvuta", font=("Arial", 16), bg="yellow", fg="red", command=calculate)

aInput.pack(side = LEFT)
eq1.pack(side = LEFT)
bInput.pack(side = LEFT)
eq2.pack(side = LEFT)
cInput.pack(side = LEFT)
eq3.pack(side = LEFT)
calcButton.pack(side = LEFT)
answer = Label(aken, text="Lahendus", font=("Arial", 20), bg="yellow", fg="green", width=20, height=3)
answer.pack(side = "bottom", pady = 20)

grafButton = Button(aken, text="Graafik", font=("Arial", 16), bg="yellow", fg="red", command=graph)
grafButton.pack(side = "bottom", pady = 20)

aken.mainloop()