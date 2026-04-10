import tkinter as tk
from tkinter import messagebox


def calculer(operation):
    try:

        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "addition":
            resultat = a + b
        elif operation == "soustraction":
            resultat = a - b
        elif operation == "multiplication":
            resultat = a * b
        elif operation == "division":
            if b == 0:
                messagebox.showerror("Erreur", "Division par zéro impossible")
                return
            resultat = a / b
        else:
            resultat = "Opération inconnue"

        label_resultat.config(text=f"Résultat : {resultat}")

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

fenetre = tk.Tk()
fenetre.title("Calculatrice Tkinter")

tk.Label(fenetre, text="Nombre 1 :").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(fenetre)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(fenetre, text="Nombre 2 :").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(fenetre)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Button(fenetre, text="Addition", command=lambda: calculer("addition")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(fenetre, text="Soustraction", command=lambda: calculer("soustraction")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(fenetre, text="Multiplication", command=lambda: calculer("multiplication")).grid(row=3, column=0, padx=5,
                                                                                           pady=5)
tk.Button(fenetre, text="Division", command=lambda: calculer("division")).grid(row=3, column=1, padx=5, pady=5)

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.grid(row=4, column=0, columnspan=2, pady=10)

fenetre.mainloop()