from fastapi import FastAPI
import joblib
from pydantic import BaseModel


model = joblib.load('Model/dbscan_model.joblib')
scaler = joblib.load('Model/dbscan_scaler.joblib')
nn = joblib.load('Model/nearest_neighbors.joblib')



app = FastAPI()

@app.get("/")
def root():
    return "Welcome To Tuwaiq Academy"

items = {}


# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}


# get request
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


# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    height: float
    age: float
    appearance: int
    goals: float
    assists: float
    goals_conceded: float
    highest_value: int
    position_encoded: int
    winger: int
    


def preprocessing(input_features: InputFeatures):
    dict_f = {
    'height': input_features.height,
    'age': input_features.age,
    'appearance': input_features.appearance,
    'goals': input_features.goals,
    'assists': input_features.assists,
    'goals conceded': input_features.goals_conceded,
    'highest_value': input_features.highest_value,
    'position_encoded': input_features.position_encoded,
    'winger': input_features.winger,
    }
    
    # return dict_f
    
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
    # Scale the input features
    scaled_features = scaler.transform([list(dict_f.values())])
    
    return scaled_features


@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)

    _, indices = nn.kneighbors(data)
    nearest_core_sample = indices[0][0]

    # Predict the cluster label of the nearest core
    y_pred = model.labels_[model.core_sample_indices_[nearest_core_sample]]
    return {"pred": int(y_pred)}
