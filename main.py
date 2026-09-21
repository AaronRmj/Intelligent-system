from charger_dataset import charger_dataset
from nettoyage import nettoyer


df = charger_dataset("dataset.csv")
df["intention_user"] = df["intention_user"].apply(nettoyer)

print(df)
input_user = input("Que voulez vous faire?\n")
input_clean = nettoyer(input_user)
print(input_clean)


