import sqlite3
from dbModule import *
import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk

entries = {}
def clearEntries():
    global entries
    for entry in entries.values():
        entry.delete(0, tk.END)

def validateData()->bool:
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

def insertData(window):
    if not validateData():
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
    window.destroy()

def search(search:str)->list:
    if not search:
        return selectAll("movies", None, None)

    return selectAll("movies", None, f"title LIKE '{search}%'")

def loadTree(tree:ttk.Treeview):
    tree["columns"] = ("title", "director", "year", "genre", "duration", "rating", "language", "country", "description")
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

def updateWindow(root, itemId)->Toplevel:
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE id=?", (itemId,))
    record = cursor.fetchone()
    conn.close()

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

        if label in ["Režissöör", "Žanr", "Keel", "Riik"]:
            table_map = {
                "Režissöör": "directors",
                "Žanr": "genres",
                "Keel": "languages",
                "Riik": "countries"
            }
            values = fetchValuesFromTable(table_map[label])
            combo = ttk.Combobox(update_window, values=values, width=47)
            combo.grid(row=i, column=1, padx=10, pady=5)
            combo.set(record[i])  # pre-fill with current value
            entries[label] = combo
        else:
            entry = tk.Entry(update_window, width=50)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, record[i])
            entries[label] = entry

    save_button = tk.Button(update_window, text="Salvesta", command=lambda: updateRecord(itemId, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
    return update_window

def insertWindow()->Toplevel:
    root = tk.Toplevel()
    root.title("Filmi andmete sisestamine")

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    global entries
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)

        if label in ["Režissöör", "Žanr", "Keel", "Riik"]:
            table_map = {
                "Režissöör": "directors",
                "Žanr": "genres",
                "Keel": "languages",
                "Riik": "countries"
            }
            values = fetchValuesFromTable(table_map[label])
            combo = ttk.Combobox(root, values=values, width=37)
            combo.grid(row=i, column=1, padx=10, pady=5)
            entries[label] = combo
        else:
            entry = tk.Entry(root, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[label] = entry

    submit_button = tk.Button(root, text="Sisesta andmed", command=lambda: insertData(root))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)
    return root

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

    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")

def fetchValuesFromTable(table: str) -> list:
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM {table}")
    values = [row[0] for row in cursor.fetchall()]
    conn.close()
    return values