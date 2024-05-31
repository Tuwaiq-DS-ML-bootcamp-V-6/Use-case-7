from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

try:
    model = joblib.load('Models/knn_model.joblib')
    scaler = joblib.load('Models/scaler.joblib')
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    raise

@app.get("/")
def root():
    return "Welcome To My Lab"

@app.get("/items/")
def create_item(item: dict):
    return{"item": item}

# model = joblib.load('Models/knn_model.joblib')
# scaler = joblib.load('Models/scaler.joblib')  

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    appearance : int
    minutes_played : int
    highest_value : int

def preprocessing(input_features: InputFeatures):
    dict_f = {
                'appearance': input_features.appearance,
                'minutes_played': input_features.minutes_played,
                'highest_value': input_features.highest_value,
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


# curl -X POST "http://localhost:8000/predict" \
# -H "Content-Type: application/json" \
# -d '{
# "appearance": 104,
# "minutes_played": 9390,
# "highest_value": 70000000
# }'