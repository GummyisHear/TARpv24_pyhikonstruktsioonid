import os
import random
from tkinter import *

BACKGROUND = "#100f27"
GREY = "#4b4a5e"
YELLOW = "#c69000"
GREEN = "#2f9800"
RED = "#c4121b"

sonad = [ "eesti", "sõber" ]
answer = ""
katsed = 6
tiles = []
currentKey = 0
currentRow = 0

def readFile():
    global sonad
    sonad = []
    try:
        with open("wordleGui/sonad.txt", "r") as file:
            for line in file:
                sonad.append(line.strip())
    except FileNotFoundError:
        print("Sõnade faili ei leitud.")
        exit(1)

def startGame(root):
    global answer
    global currentKey
    global currentRow

    for tile in tiles:
        resetTile(tile)

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

root = createWindow("WORDLE")
pealkiri = Label(root, text="Eesti Wordle!", font=("Arial", 16, "bold"), bg=BACKGROUND, fg="white")

pealkiri.pack(pady=20, padx=20, anchor="center")

tileFrame = Frame(root, bg=BACKGROUND)
initTiles(tileFrame)
tileFrame.pack(pady=20, padx=20, anchor="center")

readFile()
startGame(root)

root.mainloop()