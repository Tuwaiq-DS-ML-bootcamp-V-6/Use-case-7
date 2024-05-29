from fastapi import FastAPI
import joblib
from pydantic import BaseModel


model = joblib.load('Models/k_means_model.joblib')
scaler = joblib.load('Models/scaler.joblib')


app = FastAPI()

@app.get("/")
def root():
    return "Welcome To Tuwaiqsss Academy"

items = {}


#GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}


#get request
@app.get("/items")
def create_item(item: str):
    print(item)
    items[item] = 0
    return items


@app.get("/update")
def update_item(item: str, value: int):
    if items.get(item, None) == None:
        return "error: item not found"

    items[item] = value
    return items[item]


@app.get("/all")
def get_items_item():
    return items

#Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    appearance: int
    minutes_played: int
    games_injured: int
    award: int
    highest_value: int
    goals: int
    assists: int
    yellow_cards: int

def preprocessing(input_features: InputFeatures):
    dict_f = {
    'appearance': input_features.appearance,
    'minutes_played': input_features.minutes_played,
    'games_injured': input_features.games_injured,
    'award': input_features.award,
    'highest_value': input_features.highest_value,
    'goals': input_features.goals,
    'assists': input_features.assists,
    'yellow_cards': input_features.yellow_cards
    }

    #return dict_f
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
    # Scale the input features 
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}