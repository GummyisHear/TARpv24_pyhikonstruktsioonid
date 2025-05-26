import sqlite3
from dbModule import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

try:
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    print("Ühendus loodud")
    # Siia päringud
    createMoviesTable(cursor)
    conn.commit()
    print("Tabel loodud")

    selectAll("movies", cursor)

except sqlite3.Error as error:
    print("Tekkis viga andmebaasiga ühendamisel:", error)
finally:
    if conn:
        conn.close()

def validate_data()->bool:
    global entries
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    return True

def insert_data():
    if not validate_data():
        return

    global entries
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entries["Pealkiri"].get(),
        entries["Režissöör"].get(),
        entries["Aasta"].get(),
        entries["Žanr"].get(),
        entries["Kestus"].get(),
        entries["Reiting"].get(),
        entries["Keel"].get(),
        entries["Riik"].get(),
        entries["Kirjeldus"].get()
    ))
        
    conn.commit()
    conn.close()

    messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
    clearEntries()
    updateTree()

def clearEntries():
    global entries
    for entry in entries.values():
        entry.delete(0, tk.END)

entries = {}
def insertWindow():
    root = tk.Tk()
    root.title("Filmi andmete sisestamine")

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    global entries
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(root, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    # Loo nupp andmete sisestamiseks
    submit_button = tk.Button(root, text="Sisesta andmed", command=insert_data)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

    # Näita Tkinteri akent
    root.mainloop()

search = ""
def updateTree():
    global search
    rows = selectAll("movies", None, f"title LIKE '{search}%'")

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])

def onSearch():
    global search
    search = search_entry.get().strip()
    updateTree()

def onDelete():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Hoiatus", "Palun vali kustutatav film.")
        return

    movieId = selected_item[0]
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM movies WHERE id=?", (movieId,))
    conn.commit()
    conn.close()

    updateTree()

def onUpdate():
    selected_item = tree.selection()
    if selected_item:
        itemId = selected_item[0]
        updateWindow(itemId)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

def updateWindow(itemId):
    # Loo uus aken
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    # Loo andmebaasi ühendus ja toomine olemasolevad andmed
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE id=?", (itemId,))
    record = cursor.fetchone()
    conn.close()

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(update_window, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, record[i])
        entries[label] = entry

    # Salvestamise nupp
    save_button = tk.Button(update_window, text="Salvesta", command=lambda: updateRecord(itemId, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

def updateRecord(itemId, entries, window):
    title = entries["Pealkiri"].get()
    director = entries["Režissöör"].get()
    release_year = entries["Aasta"].get()
    genre = entries["Žanr"].get()
    duration = entries["Kestus"].get()
    rating = entries["Reiting"].get()
    language = entries["Keel"].get()
    country = entries["Riik"].get()
    description = entries["Kirjeldus"].get()

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE movies
        SET title=?, director=?, release_year=?, genre=?, duration=?, rating=?, language=?, country=?, description=?
        WHERE id=?
    """, (title, director, release_year, genre, duration, rating, language, country, description, itemId))
    conn.commit()
    conn.close()

    updateTree()
    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")

root = tk.Tk()
root.title("Filmid")
root.geometry("1000x600")

rowFrame = tk.Frame(root)
rowFrame.pack(pady=10, fill=tk.X)

# Nuppude loomine
buttonFrame = tk.Frame(rowFrame)
buttonFrame.pack(pady=10, side=tk.RIGHT, anchor="e")

button = tk.Button(buttonFrame, text="Lisa uus film", command=insertWindow)
button.pack(side="left", padx=10)
button = tk.Button(buttonFrame, text="Kustuta film", command=onDelete)
button.pack(side="left", padx=10)
button = tk.Button(buttonFrame, text="Muuda film", command=onUpdate)
button.pack(side="left", padx=10)

# Lisa otsingukast
search_frame = tk.Frame(rowFrame)
search_frame.pack(pady=10, padx=10, side=tk.LEFT, anchor="w")

search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=onSearch)
search_button.pack(side=tk.LEFT)

# Loome tabel
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

updateTree()

root.mainloop()