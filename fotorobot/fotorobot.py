
from turtle import width
import customtkinter as ctk
from tkinter import simpledialog, Canvas
from PIL import Image, ImageTk
import pygame

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

faces = {
    "klouni_nägu": "fotorobot/parts/face_1.png",
    "kollane_nägu": "fotorobot/parts/face_2.png",
    "imp_nägu": "fotorobot/parts/face_3.png",
    "kaka_nägu": "fotorobot/parts/face_4.png",
    "robot_nägu": "fotorobot/parts/face_5.png",
    "kolju_nägu": "fotorobot/parts/face_6.png",
    "ogre_nägu": "fotorobot/parts/face_7.png",
}

eyes = {
    "klouni_silmad": "fotorobot/parts/eyes_1.png",
    "punastunud_silmad": "fotorobot/parts/eyes_2.png",
    "imp_silmad": "fotorobot/parts/eyes_3.png",
    "geeniuse_silmad": "fotorobot/parts/eyes_4.png",
    "raha_silmad": "fotorobot/parts/eyes_5.png",
    "kaka_silmad": "fotorobot/parts/eyes_6.png",
    "robot_silmad": "fotorobot/parts/eyes_7.png",
    "kolju_silmad": "fotorobot/parts/eyes_8.png",
    "nutvad_silmad": "fotorobot/parts/eyes_9.png",
    "oksendavad_silmad": "fotorobot/parts/eyes_10.png",
    "ogre_silmad": "fotorobot/parts/eyes_11.png",
}

mouths = {
    "klouni_suu": "fotorobot/parts/mouth_1.png",
    "punastunud_suu": "fotorobot/parts/mouth_2.png",
    "imp_suu": "fotorobot/parts/mouth_3.png",
    "geeniuse_suu": "fotorobot/parts/mouth_4.png",
    "raha_suu": "fotorobot/parts/mouth_5.png",
    "kaka_suu": "fotorobot/parts/mouth_6.png",
    "robot_suu": "fotorobot/parts/mouth_7.png",
    "nutvad_suu": "fotorobot/parts/mouth_8.png",
    "oksendavad_suu": "fotorobot/parts/mouth_9.png",
    "ogre_suu": "fotorobot/parts/mouth_10.png",
}

eyebrows = {
    "punastunud_kulmud": "fotorobot/parts/eyebrow_1.png",
    "nutvad_kulmud": "fotorobot/parts/eyebrow_2.png"
}

noses = {
    "klouni_nina": "fotorobot/parts/nose_1.png",
    "kolju_nina": "fotorobot/parts/nose_2.png",
    "ogre_nina": "fotorobot/parts/nose_3.png",
}

assets = {**faces, **eyebrows, **noses,**eyes, **mouths}
currentParts = ["", "", "", "", ""]
partDicts = {
    FACE: faces,
    EYEBROWS: eyebrows,
    NOSE: noses,
    EYES: eyes,
    MOUTH: mouths
}

imageRefs = {}

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

    image.save(fileName)

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
createButton(buttonFrame, "None", FACE).pack(pady=10, padx=10)
createButton(buttonFrame, "None", EYEBROWS).pack(pady=10, padx=10)
createButton(buttonFrame, "None", NOSE).pack(pady=10, padx=10)
createButton(buttonFrame, "None", EYES).pack(pady=10, padx=10)
createButton(buttonFrame, "None", MOUTH).pack(pady=10, padx=10)

ctk.CTkButton(frame, text="Salvesta Pilt", command=lambda: saveFace(), **seaded).pack(pady=10)

changePart(FACE, "klouni_nägu")

app.mainloop()