import numpy as np
import os
from classifier import dataset, index_min, score

seuil = 1.4
commande_a_executer = dataset['commande_a_executer'][index_min]


def execution(commande):
    
    if score < seuil:
        if commande == "ouvrir_chrome":
            print("je lance le navigateur")

        elif commande == "jouer_chanson":  
            print("Playlist en cours de lecture")

    else: 
        print("Je ne comprends pas votre commande, ressayer svp!")

execution(commande_a_executer)