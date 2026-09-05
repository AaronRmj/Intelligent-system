import string 


#Mettre en miniscule, enlever ponctuation, enlever espace
def nettoyer(texte):
    if texte is None:
        return
    texte = texte.lower().strip()
    for symbole in string.punctuation:
        texte = texte.replace(symbole, " ")
    texte = " ".join(texte.split())
    return texte


