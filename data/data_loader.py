import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, sep=';')
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
    df = df.sort_values(by=['id', 'date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    return df

def clean_data(df, pollutants):
    df = df.dropna(subset=pollutants)
    return df
