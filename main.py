from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel

# Load the model and scaler
model = joblib.load('Models/knn.joblib')
scaler = joblib.load('Models/scaler.joblib')

app = FastAPI()

# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    appearance: int
    minutes_played: int
    highest_value: int
    award: int
    some_feature: int  # Ensure this matches the missing feature

def preprocessing(input_features: InputFeatures, scaler):
    dict_f = {
        'appearance': input_features.appearance,
        'minutes_played': input_features.minutes_played,
        'highest_value': input_features.highest_value,
        'award': input_features.award,
        'some_feature': input_features.some_feature,  # Include all features
    }

    # Scale the input features using the provided scaler
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        # Call preprocessing function with the scaler
        data = preprocessing(input_features, scaler)
        y_pred = model.predict(data)
        return {"pred": y_pred.tolist()[0]}
    except Exception as e:
        # Log the error and raise HTTPException
        raise HTTPException(status_code=500, detail=str(e))

# Run the app using: uvicorn filename:app --reload
