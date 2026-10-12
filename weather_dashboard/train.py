from pathlib import Path
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

def train(csv_path, output_path):
    data = pd.read_csv(csv_path)
    features = ["location", "humidity", "wind_speed"]
    preprocess = ColumnTransformer([("city", OneHotEncoder(handle_unknown="ignore"), ["location"])], remainder="passthrough")
    model = make_pipeline(preprocess, LinearRegression())
    model.fit(data[features], data["temperature"])
    joblib.dump(model, output_path)
    return model

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    train(root / "simulated_weather_data.csv", root / "model.joblib")
    print("Trained model on illustrative simulated data; no forecast accuracy claim.")
