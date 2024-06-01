from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your model and scaler
model = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')

app = FastAPI()

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    appearance: int
    minutes_played: float
    days_injured: int
    games_injured: int
    award: int
    highest_value: float
    player_level_category_encoded: int

def preprocessing(input_features: InputFeatures):
    # Creating feature list
    features_list = [
        input_features.appearance,
        input_features.minutes_played,
        input_features.days_injured,
        input_features.games_injured,
        input_features.award,
        input_features.highest_value,
        input_features.player_level_category_encoded
    ]
    # Scaling the features
    scaled_features = scaler.transform([features_list])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"prediction": y_pred.tolist()[0]}

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI ML Model"}
