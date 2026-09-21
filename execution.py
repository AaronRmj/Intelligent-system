import numpy as np
import webbrowser
from classifier import dataset, index_min, score, clean_input
import urllib.parse


seuil = 1.4
commande_a_executer = dataset['commande_a_executer'][index_min]


def execution(commande, phrase_user):

    if score < seuil:
        if commande == "ouvrir_chrome":
            print("je lance le navigateur")
            webbrowser.open("www.google.com")

        elif commande == "jouer_chanson": 

            
            verbes_musique = ["jouer","lancer", "chanson", "morceau", "playlist", "musique", "lancer","mettre","mets","diffuser","ecouter"]

            #on va recherche sur youtube les mots en dehors de verbes_musique
            recherche = [mot for mot in phrase_user if mot not in verbes_musique]

            # rattacher les mots
            requete = " ".join(recherche)

            if requete:
                query = urllib.parse.quote(requete)
                webbrowser.open(f"https://www.google.com/search?q={query}+youtube&btnI")

            print("Playlist en cours de lecture")

        elif commande == "deviner_chanson":
            print("Je suis en train de chercher le titre de votre chanson")    

    else: 
        print("Je ne comprends pas votre commande, ressayer svp!")

execution(commande_a_executer, clean_input)