from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "Welcome to my API!"}


# Load your model and scaler
model = joblib.load('DBSCAN.joblib')
scaler = joblib.load('scaler.joblib')

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    height: float
    age: float
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
  
def preprocessing(input_features: InputFeatures):
    dict_f = {
        'height': input_features.height,
        'age': input_features.age,
        'appearance': input_features.appearance,
        'goals': input_features.goals,
        'assists': input_features.assists,
        'yellow_cards': input_features.yellow_cards,
        'red_cards': input_features.red_cards,
        'goals_conceded': input_features.goals_conceded,
        'clean_sheets': input_features.clean_sheets,
        'minutes_played': input_features.minutes_played,
        'days_injured': input_features.days_injured,
        'games_injured': input_features.games_injured,
        'award': input_features.award,
        'current_value': input_features.current_value,
        'highest_value': input_features.highest_value,
       
    }
    return dict_f

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    scaled_features = scaler.transform([list(data.values())])
    y_pred = model.predict(scaled_features)
    return {"pred": y_pred.tolist()[0]}
