from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome To Tuwaiq Academy!"}

@app.get("/items/")
def create_item(item: dict):
    return{"item": item}

import joblib
model = joblib.load('Models/knn_model (2).joblib')
scaler = joblib.load('Models/scaler (1).joblib')


class InputFeatures(BaseModel):
    age: float
    appearance: int  
    minutes_played: int  
    highest_value: int
    
    
def preprocessing(input_features: InputFeatures):
    dict_f = {
            'age': input_features.age,
            'appearance': input_features.appearance, 
            'minutes_played': input_features.minutes_played, 
            'highest_value': input_features.highest_value ,
            }
     # Scale the input features
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features

# @app.get("/predict")
# def predict(input_features: InputFeatures):
#     return preprocessing(input_features)

@app.post("/predict")
async def predict(input_features: InputFeatures):
    dict_f = preprocessing(input_features)
    y_pred = model.predict(dict_f)
    return {"pred": y_pred.tolist()[0]}


  