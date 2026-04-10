import tkinter as tk

def convertir():
    try:
        celsius = float(entree_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        resultat_label.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        resultat_label.config(text="Entrée invalide")

fenetre = tk.Tk()
fenetre.title("Conversion Température")

label = tk.Label(fenetre, text="Température en Celsius :")
label.pack()

entree_celsius = tk.Entry(fenetre)
entree_celsius.pack()

bouton = tk.Button(fenetre, text="Convertir", command=convertir)
bouton.pack()

resultat_label = tk.Label(fenetre, text="Résultat en Fahrenheit")
resultat_label.pack()

fenetre.mainloop()