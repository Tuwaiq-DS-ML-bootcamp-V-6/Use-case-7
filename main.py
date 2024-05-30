from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import logging

app = FastAPI()

try:
    model = joblib.load('Models/knn_model.joblib')
    scaler = joblib.load('Models/scaler.joblib')
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    raise

@app.get("/")
def home():
    return "Welcome To Tuwaiq Academy"

class PlayerFeatures(BaseModel):
    appearance: int
    minutes_played: int
    highest_value: int
    award: int
    kmeans: int

def preprocess(features: PlayerFeatures):
    feature_dict = {
        'appearance': features.appearance,
        'minutes_played': features.minutes_played,
        'highest_value': features.highest_value,
        'award': features.award,
        'kmeans': features.kmeans
    }
    scaled_data = scaler.transform([list(feature_dict.values())])
    return scaled_data

@app.post("/predict")
async def predict(features: PlayerFeatures):
    try:
        processed_data = preprocess(features)

        prediction = model.predict(processed_data)
        return {"pred": prediction[0]}
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
