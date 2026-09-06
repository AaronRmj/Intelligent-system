from charger_dataset import charger_dataset
from nettoyage import nettoyer


dataset = charger_dataset("dataset.csv")
input_user = input("Que voulez vous faire?\n")

clean_dataset = dataset["intention_user"].apply(nettoyer)
clean_input = nettoyer(input_user)

# set elimination doublon
vocabulaire = []
for ligne in clean_dataset:
    ligne = ligne.split()
    for mot in ligne:
        vocabulaire.append(mot)

vocabulaire_globale = sorted(list(set(vocabulaire)))
print(vocabulaire_globale)
# vectoriser le dataset et l input user en 0 et 1, absent ou present

# calculer distance euclidienne entre vecteur user et vecteur dataset