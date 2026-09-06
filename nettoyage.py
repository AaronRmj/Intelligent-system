import string 


#Mettre en miniscule, enlever ponctuation, enlever espace
def nettoyer(texte):
    
    if texte is None:
        return ""
    
    synonyme_syllabe = {

        "à": "a",
        "ù": "u",
        "é": "e",
        "è": "e",
        "ê": "e",
        "ç": "c"

    }

    #on retourne cle, valeur avec la clé qui sera remplacé par la valeur
    for syllabe_accentuee, syllabe_normale in synonyme_syllabe.items():
        texte = texte.replace(syllabe_accentuee, syllabe_normale)

    
    texte = texte.lower().strip()
    for symbole in string.punctuation:
        texte = texte.replace(symbole, " ")
    texte = " ".join(texte.split())
    return texte