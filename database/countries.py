import sqlite3
from dbModule import *
import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk

def loadTree(tree):
    tree["columns"] = ("name")

    tree.heading("name", text="Riik")

    tree.column("name", width=50)
    
def insertWindow(root, conn)->Toplevel:
    def salvesta():
        c = country.get()
        if c:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO countries (name) VALUES (?)", (c,))
            conn.commit()
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Lisa riik")
    tk.Label(top, text="Riik:").pack(pady=10, padx=10)
    country = tk.Entry(top)
    country.pack(padx=10, pady=10)
    tk.Button(top, text="Salvesta", command=salvesta).pack(padx=10, pady=10)
    return top

def updateWindow(root, itemId)->Toplevel:
    top = tk.Toplevel(root)
    top.title("Muuda riik")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM countries WHERE id=?", (itemId,))
    record = cursor.fetchone()
    conn.close()

    tk.Label(top, text="Riik").grid(row=0, padx=10, pady=10, sticky="w")
    entry = tk.Entry(top, width=50)
    entry.insert(0, record[1])
    entry.grid(row=0, column=1)

    # Salvestamise nupp
    save_button = tk.Button(top, text="Salvesta", command=lambda: updateRecord(itemId, entry.get(), top)).grid(column=0, columnspan=2, pady=10)
    return top

def search(search:str):
    if not search:
        return selectAll("countries", None, None)

    return selectAll("countries", None, f"name LIKE '{search}%'")

def updateRecord(itemId, name, window):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE countries
        SET name=?
        WHERE id=?
    """, (name, itemId))
    conn.commit()
    conn.close()

    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")