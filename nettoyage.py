import string 


#Mettre en miniscule, enlever ponctuation, enlever espace
def nettoyer():
    sentence = input("Que souhaitez vous faire?\n")
    sentence = sentence.lower().strip()
    for ponctuation in string.punctuation:
            sentence = sentence.replace(ponctuation, " ")

    # enleve les espaces de trop        
    sentence = " ".join(sentence.split())
    print(sentence)
    
nettoyer()