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
# height	age	appearance	goals	assists	yellow cards	second yellow cards	red cards	goals conceded	clean sheets
# 	minutes played	days_injured	games_injured	award	highest_value	position_encoded	winger
class PlayerFeatures(BaseModel):
    appearance: int
    highest_value: int
    height: int
    age: int
    goals: float
    assists: int
    yellow_cards: int
    second_yellow_cards: int
    red_cards: int
    goals_conceded: float
    clean_sheets: float
    minutes_played: float
    days_injured: int
    games_injured: int
    award: int
    position_encoded: int
    winger: int

def preprocess(features: PlayerFeatures):
    feature_dict = {
        'appearance': features.appearance,
        'highest_value': features.highest_value,
        'height': features.height,
        'age': features.age,
        'goals': features.goals,
        'assists': features.assists,
        'yellow cards': features.yellow_cards,
        'second yellow_cards': features.second_yellow_cards,\
        'red cards': features.red_cards,
        'goals conceded': features.goals_conceded,
        'clean sheets': features.clean_sheets,
        'minutes played': features.minutes_played,
        'days_injured': features.days_injured,
        'games_injured': features.games_injured,
        'award': features.award,
        'position_encoded': features.position_encoded,
        'winger': features.winger,
        
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