import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    try:
        data = pd.read_csv("data.txt", names=["date", "task", "minutes", "distractions"])

        X = data[["minutes", "distractions"]]
        y = data["minutes"] / (data["distractions"] + 1)  # productivity formula

        model = LinearRegression()
        model.fit(X, y)

        return model

    except:
        return None


def predict_productivity(model, minutes, distractions):
    if model is None:
        return "Not enough data"

    prediction = model.predict([[minutes, distractions]])
    return round(prediction[0], 2)
