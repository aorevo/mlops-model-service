import os
import joblib

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


MODEL_PATH = "app/model.pkl"

def train_model():
    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    os.makedirs("app", exist_ok=True)

    model_data = {
        "model": model,
        "target_names": iris.target_names.tolist(),
        "feature_names": iris.feature_names
    }

    joblib.dump(model_data, MODEL_PATH)

    print(f"Model has been trained and saved to {MODEL_PATH}")
    print(f"Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    train_model()