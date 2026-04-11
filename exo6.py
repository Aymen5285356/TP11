import tkinter as tk
from tkinter import messagebox
import openpyxl
import os

# Créer ou charger le fichier Excel
file_name = "stagiaires.xlsx"

if os.path.exists(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
else:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Stagiaires"
    sheet.append(["Nom", "Prénom", "Âge", "Formation"])
    workbook.save(file_name)

# Fonction pour enregistrer les données
def enregistrer():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    age = entry_age.get()
    formation = entry_formation.get()

    if nom == "" or prenom == "" or age == "" or formation == "":
        messagebox.showwarning("Attention", "Tous les champs sont obligatoires !")
        return

    sheet.append([nom, prenom, age, formation])
    workbook.save(file_name)

    messagebox.showinfo("Succès", "Stagiaire enregistré avec succès !")

    # Vider les champs
    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_formation.delete(0, tk.END)

# Interface graphique
root = tk.Tk()
root.title("Enregistrement Stagiaire")
root.geometry("400x300")

# Labels et champs
tk.Label(root, text="Nom").pack()
entry_nom = tk.Entry(root)
entry_nom.pack()

tk.Label(root, text="Prénom").pack()
entry_prenom = tk.Entry(root)
entry_prenom.pack()

tk.Label(root, text="Âge").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Formation").pack()
entry_formation = tk.Entry(root)
entry_formation.pack()

# Bouton
tk.Button(root, text="Enregistrer", command=enregistrer).pack(pady=10)

# Lancer l'application
root.mainloop()