import pandas as pd

def charger_dataset(dataset):
    df = pd.read_csv(dataset)
    return df

