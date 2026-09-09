from charger_dataset import charger_dataset
from nettoyage import nettoyer
import numpy as np
import math

dataset = charger_dataset("dataset.csv")
input_user = input("Que voulez vous faire?\n")


# il prend ligne par ligne 
clean_dataset = dataset["intention_user"].apply(nettoyer)

clean_input = nettoyer(input_user)

# creer une liste de vocabulaire unique 
vocabulaire = []
for ligne in clean_dataset:
    ligne = ligne.split()
    for mot in ligne:
        vocabulaire.append(mot)
vocabulaire_globale = sorted(set(vocabulaire))
print(vocabulaire_globale)


# vectoriser le dataset

def vectoriser(phrase_user, vocabulaire):
    vecteur_init = np.zeros(len(vocabulaire), dtype=int)
    mots = phrase_user.split()
    for mot in mots: 
        if mot in vocabulaire:
            index = vocabulaire.index(mot)
            vecteur_init[index] = 1

    print(vecteur_init)
    return vecteur_init

vecteur_user = vectoriser(clean_input, vocabulaire_globale)



# vectoriser dataset
matrice_dataset = []
for ligne in clean_dataset:
    v_ligne = vectoriser(ligne, vocabulaire_globale)
    matrice_dataset.append(v_ligne)

#avadika array en np
matrice_dataset = np.array(matrice_dataset)

#how similar are vecteur_user sy vecteur_matrice
def distance_euclidienne(v_user, v_matrice):
    distances = []

    #isaky ny ligne no calculena ny distance
    for v_ligne in v_matrice:
        difference = v_user - v_ligne
        somme_carre = np.sum(difference ** 2)
        distance = math.sqrt(somme_carre)
        distances.append(distance)
    return distances

distances = distance_euclidienne(vecteur_user, matrice_dataset)

#recherche le min
index_min = np.argmin(distances)
print(f"phrase plus proche de l'intention user: {index_min}")
score = distances[index_min]
print(f"score: {score}") 