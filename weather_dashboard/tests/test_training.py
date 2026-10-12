import unittest
import tempfile
from pathlib import Path
import pandas as pd
import joblib
from train import train

class TrainingSmoke(unittest.TestCase):
    def test_unseen_city_and_saved_model(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "model.joblib"
            train(root / "simulated_weather_data.csv", target)
            model = joblib.load(target)
            result = model.predict(pd.DataFrame([{"location":"Unseen City", "humidity":60, "wind_speed":10}]))
            self.assertEqual(result.shape, (1,))
            self.assertTrue(pd.notna(result[0]))
