import pandas as pd

def charger_dataset(dataset):
    try:
        df = pd.read_csv(dataset)
        df = df.drop_duplicates().dropna()
        return df

    except: 
        print("Echec lors du chargement")