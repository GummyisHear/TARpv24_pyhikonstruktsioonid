import sqlite3
from dbModule import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import movies
import languages

currentTable = "movies"

try:
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    initDb()
except sqlite3.Error as error:
    print("Tekkis viga andmebaasiga ühendamisel:", error)

def onInsert():
    if (currentTable == "languages"):
        languages.insertWindow(root, conn)
    if (currentTable == "movies"):
        movies.insertWindow()
    # code does not stop in toplevel windows, need to listen for event close
    updateTree()

def onSearch():
    global search
    search = search_entry.get().strip()
    updateTree()

def onDelete():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Hoiatus", "Palun vali kustutatav rida.")
        return

    movieId = selected_item[0]
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {currentTable} WHERE id=?", (movieId,))
    conn.commit()
    conn.close()

    updateTree()

def onUpdate():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
        return

    itemId = selected_item[0]
    if (currentTable == "movies"):
        movies.updateWindow(root, itemId)
    if (currentTable == "languages"):
        languages.updateWindow(root, itemId)
    updateTree()

def lisa_Keel():
    def salvesta():
        keel = entry_keel.get()
        if keel:
            cursor.execute("INSERT OR IGNORE INTO languages (name) VALUES (?)", (keel,))
            conn.commit()
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Lisa keel")
    tk.Label(top, text="Keel:").pack(pady=5)
    entry_keel = tk.Entry(top)
    entry_keel.pack(pady=5)
    tk.Button(top, text="Salvesta", command=salvesta).pack(pady=10)

search = ""
def updateTree():
    global search
    if (currentTable == "movies"):
        rows = movies.search(search)
    elif (currentTable == "languages"):
        rows = languages.search(search)

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])

def switchTable(tableName:str):
    global currentTable
    tree["columns"] = []
    for item in tree.get_children():
        tree.delete(item)

    if (tableName == "languages"):
        currentTable = "languages"
        languages.loadTree(tree)

    if (tableName == "movies"):
        currentTable = "movies"
        movies.loadTree(tree)

    updateTree()

root = tk.Tk()
root.title("Filmid")
root.geometry("1000x600")

rowFrame = tk.Frame(root)
rowFrame.pack(pady=10, fill=tk.X)

# Nuppude loomine
buttonFrame = tk.Frame(rowFrame)
buttonFrame.pack(pady=10, side=tk.RIGHT, anchor="e")

button = tk.Button(buttonFrame, text="Lisa uus film", command=onInsert)
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

# Tabeli valiminine nupud
flame = tk.Frame(root)
flame.pack(pady=10, padx=10, anchor="w")
tk.Label(flame, text="Vali tabel:").pack(side=tk.LEFT)
tk.Button(flame, text="Filmid", command=lambda: switchTable("movies")).pack(padx=10, side=tk.LEFT)
tk.Button(flame, text="Keeled", command=lambda: switchTable("languages")).pack(padx=10, side=tk.LEFT)
tk.Button(flame, text="Riigid", command=lambda: switchTable("countries")).pack(padx=10, side=tk.LEFT)
tk.Button(flame, text="Žanrid", command=lambda: switchTable("genres")).pack(padx=10, side=tk.LEFT)
tk.Button(flame, text="Režissöörid", command=lambda: switchTable("directors")).pack(padx=10, side=tk.LEFT)

# Loome tabel
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

switchTable("movies")

root.mainloop()