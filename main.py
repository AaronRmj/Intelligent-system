from charger_dataset import charger_dataset
from nettoyage import nettoyer


df = charger_dataset("dataset.csv")

df["intention_user"] = df["intention_user"].apply(nettoyer)
print(df)