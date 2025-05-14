import os
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox

BACKGROUND = "#100f27"
GREY = "#4b4a5e"
GREY_RGB = (75, 74, 94)
YELLOW = "#c69000"
GREEN = "#2f9800"
RED = "#c4121b"

sonad = [ "eesti", "sõber" ]
gameNumber = 0
answer = ""
katsed = 6
tiles = []
currentKey = 0
currentRow = 0

def readFile():
    global sonad
    global gameNumber
    sonad = []
    try:
        with open("wordleGui/sonad.txt", "r") as file:
            for i, line in enumerate(file):
                if (i == 0):
                    try:
                        n = int(line)
                        gameNumber = n
                        updateGameNumber()
                        continue
                    except:
                        ...
                sonad.append(line.strip())
    except FileNotFoundError:
        print("Sõnade faili ei leitud.")
        exit(1)

def saveFile():
    global sonad
    global gameNumber
    try:
        with open("wordleGui/sonad.txt", "w") as file:
            file.write(str(gameNumber) + "\n")
            for word in sonad:
                file.write(word + "\n")
    except Exception as e:
        print(f"Viga faili kirjutamisel: {e}")

def startGame(root):
    global answer
    global currentKey
    global currentRow
    global gameNumber

    for tile in tiles:
        resetTile(tile)

    gameNumber += 1
    updateGameNumber()
    answer = random.choice(sonad)
    currentKey = 0
    currentRow = 0

    root.unbind("<Key>")
    root.bind("<Key>", onKey)

def createWindow(title, w:int = 600, h:int = 600)->Tk:
    aken = Tk()
    aken.title(title)
    aken.geometry(f"{w}x{h}")
    aken.configure(bg=BACKGROUND)
    aken.resizable(False, False)
    aken.iconbitmap("icon.ico")
    return aken

def initTiles(root):
    global tiles
    for y in range(katsed):
        for x in range(5):
            tile = createTile(root, 20, 20, 16)
            tiles.append(tile)
            tile.grid(row=y+1, column=x, padx=5, pady=5)

def createTile(root, width, height, fontSize)->Label:
    label = Label(root, text="", width=2, height=1, font=("Arial", fontSize, "bold"), anchor="center")
    label.config(bg=BACKGROUND, fg="white", highlightbackground=GREY, highlightthickness=2)
    return label

def resetTile(tile:Label):
    tile.config(bg=BACKGROUND, fg="white", highlightbackground=GREY, highlightthickness=2)
    tile.config(text="")

def colorTile(tile:Label, color:str):
    tile.config(bg=color, highlightbackground=color)

def closeWindow(window):
    window.destroy()
    startGame(root)

def onVictory():
    global answer
    root.unbind("<Key>")

    WIDTH = 240
    HEIGHT = 160

    x = root.winfo_x() + (600 // 2) - (WIDTH // 2)
    y = root.winfo_y() + (600 // 2) - (HEIGHT // 2)

    window = Toplevel(root, bg=GREEN)
    window.overrideredirect(True)
    window.pack_propagate(False)
    window.title("Võit!")
    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    frame = Frame(window, bg=BACKGROUND, width=WIDTH-10, height=HEIGHT-10)
    frame.pack_propagate(False)
    frame.pack(padx=5, pady=5)

    label = Label(frame, text="Sa võitsid!", font=("Arial", 24, "bold"), bg=BACKGROUND, fg=GREEN)
    label.pack(pady=(20, 0), anchor="center")
    
    label = Label(frame, text=f"Sõna oli: {answer}", font=("Arial", 16), bg=BACKGROUND, fg="white")
    label.pack(anchor="center")

    button = Button(frame, text="Mängi uuesti", bg=GREY, fg="white", relief="solid", width=16)
    button.config(activebackground=GREEN, activeforeground="white", border=0)
    button.config(command=lambda: closeWindow(window))
    button.pack(anchor="center", side="bottom", pady=20)

    root.bind("<Key>", lambda e: closeWindow(window) if e.keysym == "Return" else ...)

def onDefeat():
    global answer
    root.unbind("<Key>")

    WIDTH = 240
    HEIGHT = 160

    x = root.winfo_x() + (600 // 2) - (WIDTH // 2)
    y = root.winfo_y() + (600 // 2) - (HEIGHT // 2)

    window = Toplevel(root, bg=RED)
    window.overrideredirect(True)
    window.pack_propagate(False)
    window.title("Võit!")
    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    frame = Frame(window, bg=BACKGROUND, width=WIDTH-10, height=HEIGHT-10)
    frame.pack_propagate(False)
    frame.pack(padx=5, pady=5)

    label = Label(frame, text="Sa kaotasid...", font=("Arial", 24, "bold"), bg=BACKGROUND, fg=RED)
    label.pack(pady=(20, 0), anchor="center")
    
    label = Label(frame, text=f"Sõna oli: {answer}", font=("Arial", 16), bg=BACKGROUND, fg="white")
    label.pack(anchor="center")

    button = Button(frame, text="Mängi uuesti", bg=GREY, fg="white", relief="solid", width=16)
    button.config(activebackground=RED, activeforeground="white", border=0)
    button.config(command=lambda: closeWindow(window))
    button.pack(anchor="center", side="bottom", pady=20)

    root.bind("<Key>", lambda e: closeWindow(window) if e.keysym == "Return" else ...)

def onKey(event:Event):
    global currentKey
    global tiles
    global currentRow
    global answer
    global katsed
    global gameNumber

    sym = event.keysym
    char = event.char
    if (sym == "Return"):
        if (currentKey != 5):
            return

        guess = ""
        tempAnswer = answer
        for i in range(5):
            tile:Label = tiles[currentRow * 5 + i]
            char = tile.cget("text")
            if (char == answer[i]):
                colorTile(tile, GREEN)
            elif (char in tempAnswer):
                colorTile(tile, YELLOW)
            else:
                colorTile(tile, GREY)
            tempAnswer = tempAnswer.replace(char, "", 1)
            guess += char

        if (guess == answer):
            onVictory()
            return

        if (currentRow == katsed - 1):
            onDefeat()
            return

        currentRow += 1
        currentKey = 0
        return
    
    if (sym == "BackSpace"):
        if (currentKey == 0):
            return
        currentKey -= 1
        tileId = currentRow * 5 + currentKey
        tile:Label = tiles[tileId]
        tile.config(text="")
        return

    if (not char.isalpha()):
        return

    if (currentKey == 5):
        return

    tileId = currentRow * 5 + currentKey
    tile:Label = tiles[tileId]
    tile.config(text=char)
    currentKey += 1

def openSettings():
    global sonad
    WIDTH = 400
    HEIGHT = 500

    x = root.winfo_x() + (600 // 2) - (WIDTH // 2)
    y = root.winfo_y() + (600 // 2) - (HEIGHT // 2)

    window = Toplevel(root, bg=BACKGROUND)
    window.title("Sättid")
    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
    window.lift()

    window.grid_columnconfigure(0, weight=1)

    label = Label(window, text="Muuda Sõnad", font=("Arial", 16, "bold"), bg=BACKGROUND, fg="white")
    label.grid(row=0, column=0, pady=(20, 0), columnspan=2)

    listbox = Listbox(window, width=30, height=8, selectmode=SINGLE, bg=BACKGROUND, fg="white", font=("Arial", 12))
    listbox.config(relief="solid", highlightbackground=YELLOW, highlightcolor=YELLOW, selectbackground=YELLOW)
    listbox.grid(row=1, column=0, columnspan=2)

    def updateListbox():
        listbox.delete(0, END)
        for word in sonad:
            listbox.insert(END, word)

    updateListbox()

    def add_word():
        word = simpledialog.askstring("Lisa Sõna", "Sisesta uus sõna:", parent=window)

        if word:
            word = word.strip().lower()
            if word and len(word) == 5:
                sonad.append(word)
                updateListbox()
            else:
                messagebox.showerror("Error", "Sõna peaks olema 5 tähed!")
                window.lift()
        saveFile()

    def remove_word():
        selected_word = listbox.curselection()
        if selected_word:
            selected_index = selected_word[0]
            word_to_remove = listbox.get(selected_word)
            sonad.remove(word_to_remove)
            updateListbox()
            if len(listbox.get(0, END)) > 0:
                next_index = selected_index if selected_index < len(listbox.get(0, END)) else selected_index - 1
                listbox.select_set(next_index)
            else:
                listbox.select_clear()
        saveFile()

    buttonFrame = Frame(window, bg=BACKGROUND)

    button = Button(buttonFrame, text="Add Word", command=add_word)
    button.config(relief="solid", width=16)
    button.config(bg=GREY, fg="white", activebackground=GREEN, activeforeground="white", border=0)
    button.grid(row=0, column=0, pady=10, padx=10)

    button = Button(buttonFrame, text="Remove Word", command=remove_word)
    button.config(relief="solid", width=16)
    button.config(bg=GREY, fg="white", activebackground=RED, activeforeground="white", border=0)
    button.grid(row=0, column=1, pady=10, padx=10)

    buttonFrame.grid(row=2, column=0, columnspan=2)

def updateGameNumber():
    global gameNumber
    num.config(text=f"#{gameNumber}")

root = createWindow("WORDLE")
pealkiri = Label(root, text="Eesti Wordle!", font=("Arial", 16, "bold"), bg=BACKGROUND, fg="white")
pealkiri.pack(pady=(20, 0), padx=20, anchor="center")

num = Label(root, text=f"#{gameNumber}", font=("Arial", 20, "bold"), bg=BACKGROUND, fg="white")
num.pack(pady=(5, 20), padx=20, anchor="center")

icon = PhotoImage(file="wordleGui\settings.png")
button = Button(root, image=icon, bg=BACKGROUND, border=0, highlightthickness=0, command=openSettings)
button.config(activebackground=BACKGROUND, overrelief="groove")
button.place(x=10, y=10)

tileFrame = Frame(root, bg=BACKGROUND)
initTiles(tileFrame)
tileFrame.pack(pady=20, padx=20, anchor="center")

readFile()
startGame(root)

root.mainloop()
saveFile()