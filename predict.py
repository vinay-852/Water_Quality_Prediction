import pandas as pd
from model import PollutionModel

def prepare_input(station_id, year, columns):
    input_data = pd.DataFrame({'year': [year], 'id': [station_id]})
    input_encoded = pd.get_dummies(input_data, columns=['id'])
    missing_cols = set(columns) - set(input_encoded.columns)
    for col in missing_cols:
        input_encoded[col] = 0
    input_encoded = input_encoded[columns]
    return input_encoded

def predict_pollutants(model_path, columns_path, station_id, year, pollutants):
    model = PollutionModel()
    model.load(model_path, columns_path)
    input_encoded = prepare_input(station_id, year, model.columns)
    predicted = model.predict(input_encoded)[0]
    return dict(zip(pollutants, predicted))
