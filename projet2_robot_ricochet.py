################################################

# Groupe 1 BI TD1
# Princesse MOMO 
# Alexandra SCHMIDT
# Malak LALAMI
# Nolwenn CORIC
# Lilian JOANNET
# Tristan TOLENTINO
# https://github.com/uvsq22009244/projet2_robot_ricochet

################################################
# import des modules

import tkinter as tk
import random 

################################################
# constantes

HAUTEUR = 490
LARGEUR = 490
COULEUR_FOND = "grey50"
COTE = 30
COULEUR_QUADR = "grey60"
################################################
# variables globales


################################################
# fonctions

def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1

# programme principale

racine = tk.Tk()
racine.title("Robot ricochet")

# création des widgets

canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)
#canvas.create_oval(racine, )
cercle = canvas.create_oval((10, 10), (30, 30), fill="red", width=5, outline="red")

quadrillage()

#placement des widgets
canvas.grid()

racine.mainloop()