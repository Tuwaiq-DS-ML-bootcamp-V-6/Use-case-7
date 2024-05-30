from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

try:
    model = joblib.load('Models/knn_model.joblib')
    scaler = joblib.load('Models/scaler.joblib')
    logging.info("Model and scaler loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    raise

@app.get("/")
def home():
    return "Welcome To Tuwaiq Academy"

# Input data model
class PlayerFeatures(BaseModel):
    appearance: int
    minutes_played: int
    highest_value: int
    award: int
    kmeans: int

# Preprocessing function
def preprocess(features: PlayerFeatures):
    try:
        feature_dict = {
            'appearance': features.appearance,
            'minutes_played': features.minutes_played,
            'highest_value': features.highest_value,
            'award': features.award,
            'kmeans': features.kmeans
        }
        scaled_data = scaler.transform([list(feature_dict.values())])
        return scaled_data
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
        raise HTTPException(status_code=400, detail="Error in preprocessing input data")

# Prediction endpoint
@app.post("/predict")
async def predict(features: PlayerFeatures):
    try:
        # Preprocess the input data
        processed_data = preprocess(features)
        # Make prediction
        prediction = model.predict(processed_data)
        return {"pred": prediction[0]}
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
