import os
import joblib


MODEL_PATH = os.getenv("MODEL_PATH", "app/model.pkl")


class ModelService:
    def __init__(self):
        self.model_data = joblib.load(MODEL_PATH)
        self.model = self.model_data["model"]
        self.target_names = self.model_data["target_names"]

    def predict(self, features: list[float]) -> dict:
        prediction = self.model.predict([features])[0]
        predicted_class = self.target_names[prediction]

        return {
            "prediction": int(prediction),
            "class_name": predicted_class
        }
    
"""
main.py отвечает за API.

predict.py отвечает за работу с моделью.
"""