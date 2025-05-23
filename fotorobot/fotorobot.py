import random
from turtle import width
import customtkinter as ctk
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import pygame
import glob

#pygame.mixer.init()
#pygame.mixer.music.load("fotorobot/sounds/intro.mp3")
#pygame.mixer.music.set_volume(0.5)
#ctk.set_appearance_mode("Light")

app = ctk.CTk()
app.geometry("800x600")
app.title("Fotorobot")

canvas = Canvas(app, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

FACE = 0
EYES = 1
EYEBROWS = 2
MOUTH = 3
NOSE = 4

faces = {}

eyes = {}

mouths = {}

eyebrows = {}

noses = {}

assets = {}
currentParts = ["", "", "", "", ""]
partDicts = {
    FACE: faces,
    EYEBROWS: eyebrows,
    NOSE: noses,
    EYES: eyes,
    MOUTH: mouths
}

imageRefs = {}

def loadAssets():
    global assets
    for path in glob.glob("fotorobot/parts/faces/*.png"):
        name = path.split("\\")[-1].split(".")[0]
        faces[name] = path

    for path in glob.glob("fotorobot/parts/eyes/*.png"):
        name = path.split("\\")[-1].split(".")[0]
        eyes[name] = path

    for path in glob.glob("fotorobot/parts/eyebrows/*.png"):
        name = path.split("\\")[-1].split(".")[0]
        eyebrows[name] = path
    
    for path in glob.glob("fotorobot/parts/mouths/*.png"):
        name = path.split("\\")[-1].split(".")[0]
        mouths[name] = path

    for path in glob.glob("fotorobot/parts/noses/*.png"):
        name = path.split("\\")[-1].split(".")[0]
        noses[name] = path

    assets = {**faces, **eyebrows, **noses,**eyes, **mouths}

def playMusic():
    pygame.mixer.music.play(loops=-1)

def stopMusic():
    pygame.mixer.music.stop()

def saveFace():
    fileName = simpledialog.askstring("Salvesta Pilt", "Faili nimi:")
    if (not fileName):
        return

    if (fileName.find(".png") == -1):
        fileName = fileName + ".png"

    image = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    for name in currentParts:
        if (name == ""):
            continue
        path = assets[name]
        img = Image.open(path).convert("RGBA").resize((400, 400))
        image.paste(img, (0, 0), img)

    image.save("fotorobot/saved/" + fileName)

def changePart(part, name):
    currentParts[part] = name
    canvas.delete("all")
    for name in currentParts:
        if (name == ""):
            continue
        path = assets[name]
        pil_img = Image.open(path).convert("RGBA").resize((400, 400))
        tk_img = ImageTk.PhotoImage(pil_img)
        imageRefs[name] = tk_img
        x, y = 202, 202
        canvas.create_image(x, y, image=tk_img)

    faceButton.configure(text=currentParts[FACE] or "None")
    eyebrowButton.configure(text=currentParts[EYEBROWS] or "None")
    noseButton.configure(text=currentParts[NOSE] or "None")
    eyesButton.configure(text=currentParts[EYES] or "None")
    mouthButton.configure(text=currentParts[MOUTH] or "None")

def buttonPress(button, part):
    current = currentParts[part]
    parts = partDicts[part]
    names = list(parts.keys())

    currentId = -1 if current == "" else names.index(current)
    nextId = (currentId + 1)
    if (nextId >= len(names)):
        button.configure(text="None")
        changePart(part, "")
        return

    nextName = names[nextId]

    button.configure(text=nextName)
    changePart(part, nextName)

def createButton(root, defText="", partId=FACE)->ctk.CTkButton:
    button = ctk.CTkButton(root, text=defText, **seaded)
    button.configure(width=300)
    button.configure(command=lambda: buttonPress(button, partId))
    return button

def randomFace():
    changePart(FACE, random.choice(list(faces.keys())))
    changePart(EYEBROWS, random.choice(list(eyebrows.keys())))
    changePart(NOSE, random.choice(list(noses.keys())))
    changePart(EYES, random.choice(list(eyes.keys())))
    changePart(MOUTH, random.choice(list(mouths.keys())))

frame = ctk.CTkFrame(app, width=350, height=600)
frame.pack(side="left", padx=10, pady=10)
frame.pack_propagate(False)

seaded = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 32),
    "fg_color": "#4CAF50",
    "text_color": "white",
    "corner_radius": 20
}

ctk.CTkLabel(frame, text="Vali näoosad", **seaded).pack(pady=10)

buttonFrame = ctk.CTkFrame(frame, width=300, height=400)
buttonFrame.pack(pady=10)
buttonFrame.pack_propagate(False)
faceButton = createButton(buttonFrame, "None", FACE)
faceButton.pack(pady=10, padx=10)
eyebrowButton = createButton(buttonFrame, "None", EYEBROWS)
eyebrowButton.pack(pady=10, padx=10)
noseButton = createButton(buttonFrame, "None", NOSE)
noseButton.pack(pady=10, padx=10)
eyesButton = createButton(buttonFrame, "None", EYES)
eyesButton.pack(pady=10, padx=10)
mouthButton = createButton(buttonFrame, "None", MOUTH)
mouthButton.pack(pady=10, padx=10)

bottomFrame = ctk.CTkFrame(frame, width=300)
bottomFrame.pack(pady=10)
bottomFrame.pack_propagate(False)
ctk.CTkButton(bottomFrame, text="Salvesta", command=lambda: saveFace(), **seaded).pack(padx=5, side="left")
ctk.CTkButton(bottomFrame, text="Juhuslik", command=lambda: randomFace(), **seaded).pack(padx=5, side="left")

loadAssets()

app.mainloop()