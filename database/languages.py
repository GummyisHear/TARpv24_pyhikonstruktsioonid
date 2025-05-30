import sqlite3
from dbModule import *
import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk

def loadTree(tree):
    tree["columns"] = ("name")

    tree.heading("name", text="Keel")

    tree.column("name", width=50)

def insertWindow(root, conn)->Toplevel:
    def salvesta():
        keel = entry_keel.get()
        if keel:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO languages (name) VALUES (?)", (keel,))
            conn.commit()
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Lisa keel")
    tk.Label(top, text="Keel:").pack(pady=10, padx=10)
    entry_keel = tk.Entry(top)
    entry_keel.pack(pady=5)
    tk.Button(top, text="Salvesta", command=salvesta).pack(pady=10)
    return top

def updateWindow(root, itemId)->Toplevel:
    top = tk.Toplevel(root)
    top.title("Muuda keel")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM languages WHERE id=?", (itemId,))
    record = cursor.fetchone()
    conn.close()

    tk.Label(top, text="Keel").grid(row=0, padx=10, pady=10, sticky="w")
    lang = tk.Entry(top, width=50)
    lang.insert(0, record[1])
    lang.grid(row=0, column=1)

    # Salvestamise nupp
    save_button = tk.Button(top, text="Salvesta", command=lambda: updateRecord(itemId, lang.get(), top)).grid(column=0, columnspan=2, pady=10)
    return top

def search(search:str):
    if not search:
        return selectAll("languages", None, None)

    return selectAll("languages", None, f"name LIKE '{search}%'")

def updateRecord(itemId, lang, window):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE languages
        SET name=?
        WHERE id=?
    """, (lang, itemId))
    conn.commit()
    conn.close()

    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")