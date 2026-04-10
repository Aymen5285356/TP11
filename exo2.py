import tkinter as tk

compteur = 0

def incrementer():
    global compteur
    compteur += 1
    label_compteur.config(text=str(compteur))

def decrementer():
    global compteur
    if compteur > 0:
        compteur -= 1
        label_compteur.config(text=str(compteur))

fenetre = tk.Tk()
fenetre.title("Compteur")

label_compteur = tk.Label(fenetre, text="0", font=("Arial", 24))
label_compteur.pack()

btn_increment = tk.Button(fenetre, text="Incrémenter", command=incrementer)
btn_increment.pack()

btn_decrement = tk.Button(fenetre, text="Décrémenter", command=decrementer)
btn_decrement.pack()

fenetre.mainloop()