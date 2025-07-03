from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

class PollutionModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = MultiOutputRegressor(RandomForestRegressor(n_estimators=n_estimators, random_state=random_state))
        self.columns = None

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.columns = X_train.columns.tolist()

    def predict(self, X):
        return self.model.predict(X)

    def save(self, model_path, columns_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.columns, columns_path)

    def load(self, model_path, columns_path):
        self.model = joblib.load(model_path)
        self.columns = joblib.load(columns_path)
