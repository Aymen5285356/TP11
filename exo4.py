import tkinter as tk

def ajouter():
    tache = entry_tache.get()
    if tache:
        listbox.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)

def marquer(event):
    selection = listbox.curselection()
    if selection:
        listbox.itemconfig(selection[0], fg="gray", bg="#f0f0f0")

def supprimer():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])

root = tk.Tk()
root.title("To-Do List")

entry_tache = tk.Entry(root)
entry_tache.pack()

tk.Button(root, text="Ajouter", command=ajouter).pack()

listbox = tk.Listbox(root)
listbox.pack()
listbox.bind('<ButtonRelease-1>', marquer)

tk.Button(root, text="Supprimer", command=supprimer).pack()

root.mainloop()