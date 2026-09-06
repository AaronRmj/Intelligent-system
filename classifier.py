from charger_dataset import charger_dataset
from nettoyage import nettoyer
import numpy as np

dataset = charger_dataset("dataset.csv")
input_user = input("Que voulez vous faire?\n")

clean_dataset = dataset["intention_user"].apply(nettoyer)
clean_input = nettoyer(input_user)

#creer un dictionnaire de mot unique qui contient tous les mots du dataset
vocabulaire = []
for ligne in clean_dataset:
    ligne = ligne.split()
    for mot in ligne:
        vocabulaire.append(mot)

vocabulaire_globale = sorted(list(set(vocabulaire)))

print(vocabulaire_globale)
print(input_user)


# vectoriser le dataset et l input user en 0 et 1, absent ou present

def vectoriser(phrase_user, vocabulaire):
    vecteur_init = np.zeros(len(vocabulaire), dtype=int) 

    # on decoupe la phrase en mot avant de vectoriser
    mots = phrase_user.split()
    for mot in mots:
        if mot in vocabulaire:
            index = vocabulaire.index(mot)
            vecteur_init[index] = 1
    print(vecteur_init)
    return vecteur_init
        

vectoriser(clean_input, vocabulaire_globale)









# calculer distance euclidienne entre vecteur user et vecteur dataset