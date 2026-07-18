import tkinter as tk
from tkinter import messagebox

import task_manager as tm


def refresh_list():
    listbox.delete(0, tk.END)
    try:
        tm.load_tasks()
        for task in tm.get_tasks():
            listbox.insert(tk.END, task)
    except Exception as error:
        messagebox.showerror("Erreur de configuration", str(error))


def add_task_UI():
    try:
        tm.add_task(entry.get())
        entry.delete(0, tk.END)
        refresh_list()
    except Exception as error:
        messagebox.showerror("Impossible d'ajouter", str(error))


def remove_task_UI():
    selection = listbox.curselection()
    if not selection:
        return

    try:
        tm.remove_task(selection[0])
        refresh_list()
    except Exception as error:
        messagebox.showerror("Impossible de supprimer", str(error))


root = tk.Tk()
root.title("Mes tâches")

width = 300
height = 500

screen_width = root.winfo_screenwidth()
x = screen_width - width - 20
y = 20

root.geometry(f"{width}x{height}+{x}+{y}")
root.attributes("-topmost", True)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

entry = tk.Entry(frame)
entry.pack(fill="x")

add_button = tk.Button(frame, text="Ajouter", command=add_task_UI)
add_button.pack(fill="x", pady=5)

listbox = tk.Listbox(frame)
listbox.pack(fill="both", expand=True)

delete_button = tk.Button(frame, text="Supprimer", command=remove_task_UI)
delete_button.pack(fill="x", pady=5)

refresh_list()

root.mainloop()