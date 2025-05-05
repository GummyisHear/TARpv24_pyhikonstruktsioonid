from tkinter import *

k = 0

def createWindow(title, w:int = 400, h:int = 400)->Tk:
    aken = Tk()
    aken.title(title)
    aken.geometry(f"{w}x{h}")
    aken.configure(bg="lightblue")
    aken.resizable(False, False)
    aken.iconbitmap("icon.ico")
    return aken

def vajutatud():
    global k
    k += 1
    pealkiri.config(text=f"Sa vajutasid nuppu {k} korda!", bg="orange", fg="blue")
    print("Nupp vajutatud!")

def vajutatudPK(event:Event):
    global k
    k -= 1
    pealkiri.config(text=f"Sa vajutasid nuppu {k} korda!", bg="blue", fg="orange")
    print("Nupp vajutatud parema hiirega!")

def enter(event:Event):
    global k
    print("Sisenesid sisestusvälja!")
    try:
        click = int(sisestus.get())
        k = click
    except ValueError:
        return
    sisestus.config(bg="lightgreen", fg="black")
    sisestus.delete(0, END)
    pealkiri.config(text=f"Sa vajutasid nuppu {k} korda!", bg="orange", fg="blue")

    # sisestus.unbind("<FocusIn>")
    # sisestus.bind("<FocusOut>", tagasi)

aken = createWindow("Teema 8")
pealkiri = Label(aken, text="Tere tulemast!", font=("Arial", 16), bg="blue", fg="green")
nupp = Button(aken, text="Vajuta mind!", font=("Arial", 12), bg="yellow", fg="red", relief=GROOVE, comma=vajutatud) # flat, groove, raised, ridge, solid or sunken
nupp.bind("<Button-3>", vajutatudPK)
sisestus = Entry(aken, font=("Arial", 12), bg="white", fg="black", width=20)
sisestus.insert(0, "Sisesta midagi siia")
sisestus.bind("<Return>", enter) # Enter vajutamine

pealkiri.pack(pady=20, padx=20)
sisestus.pack(pady=20)
nupp.pack(pady=20)

aken.mainloop()


