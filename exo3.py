import tkinter as tk
from tkinter import messagebox

def calculer_carre():
    try:
        nombre = float(entry_nombre.get())
        resultat = nombre ** 2
        label_resultat.config(text=f"Résultat : {resultat}")
    except ValueError:
        messagebox.showerror("Erreur", "Nombre invalide")

fenetre = tk.Tk()
fenetre.title("Calcul du Carré")

tk.Label(fenetre, text="Nombre :").pack()
entry_nombre = tk.Entry(fenetre)
entry_nombre.pack()

tk.Button(fenetre, text="Calculer", command=calculer_carre).pack()
label_resultat = tk.Label(fenetre, text="")
label_resultat.pack()

fenetre.mainloop()