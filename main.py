from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to my API!"}


model = joblib.load('Models/DBSCAN.joblib')
scaler = joblib.load('Models/scaler.joblib')


class InputFeatures(BaseModel):
    height: int
    age: int
    appearance: int
    goals: float
    assists: float
    yellow_cards: float
    red_cards: float
    goals_conceded: float
    clean_sheets: float
    minutes_played: int
    days_injured: int
    games_injured: int
    award: int
    current_value: int
    second_yellow_cards: int
    highest_value: int 
    winger: int 

def preprocessing(input_features: InputFeatures):
    dict_f = {
        'height': input_features.height,
        'age': input_features.age,
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'yellow cards': input_features.yellow_cards,
        'red cards': input_features.red_cards,
        'goals conceded': input_features.goals_conceded,
        'clean sheets': input_features.clean_sheets,
        'minutes played': input_features.minutes_played,
        'days_injured': input_features.days_injured,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'current_value': input_features.current_value,
        'highest_value': input_features.highest_value,
        'winger': input_features.winger,
        'second yellow cards': input_features.second_yellow_cards,
    }
    return dict_f

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    scaled_features = scaler.transform([list(data.values())])
    y_pred = model.predict(scaled_features)
    return {"pred": y_pred.tolist()[0]}
