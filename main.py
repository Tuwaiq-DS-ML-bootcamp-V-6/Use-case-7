from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# تحديد المسارات المطلقة للملفات
model_path = os.path.join(os.path.dirname(__file__), 'ML-Kmeans.joblib')
scaler_path = os.path.join(os.path.dirname(__file__), 'Models', 'scaler.joblib')

# تحميل النموذج والمقياس
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except FileNotFoundError as e:
    print(f"Error: {e}")

class InputFeatures(BaseModel):
    appearance: int
    award: int
    highest_value: float
    goals: int
    assists: int
    yellow_cards: int
    kmeans: float

def preprocessing(input_features: InputFeatures):
    dict_f = {
        'appearance': input_features.appearance,
        'award': input_features.award,
        'highest_value': input_features.highest_value,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'yellow_cards': input_features.yellow_cards,
        'kmeans': input_features.kmeans
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
