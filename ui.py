import tkinter as tk
import task_manager as tm


def refresh_list():
    listbox.delete(0, tk.END)
    for task in tm.get_tasks():
        listbox.insert(tk.END, task)


def add_task_UI():
    tm.add_task(entry.get())
    entry.delete(0, tk.END)
    refresh_list()


def remove_task_UI():
    selection = listbox.curselection()
    if selection:
        tm.remove_task(selection[0])
        refresh_list()


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