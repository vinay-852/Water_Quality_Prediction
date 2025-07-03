import pandas as pd

def select_features(df, pollutants):
    X = df[['id', 'year']]
    y = df[pollutants]
    X_encoded = pd.get_dummies(X, columns=['id'], drop_first=True)
    return X_encoded, y
