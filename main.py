from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

model_path = os.path.join(os.path.dirname(__file__), 'ML-Kmeans.joblib')
scaler_path = os.path.join(os.path.dirname(__file__), 'Models', 'scaler.joblib')

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except FileNotFoundError as e:
    print(f"Error: {e}")

class InputFeatures(BaseModel):
    height: float
    age: int
    appearance: int
    goals: int
    assists: int
    minutes_played: int
    days_injured: int
    award: int
    highest_value: float
    position_Attack: int

def preprocessing(input_features: InputFeatures):
    dict_f = {
        'height': input_features.height,
        'age': input_features.age,
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'minutes_played': input_features.minutes_played,
        'days_injured': input_features.days_injured,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
        'position_Attack': input_features.position_Attack
    }
    return dict_f

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.get("/items/")
def create_item(item: dict):
    return {"item": item}

@app.post("/predict")
def predict(input_features: InputFeatures):
    processed_features = preprocessing(input_features)
    features = np.array([list(processed_features.values())])
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    return {"predicted_price": prediction[0]}
# uvicorn main:app --reload
