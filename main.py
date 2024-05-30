from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

import joblib
model = joblib.load('Models/knn_model.joblib')
scaler = joblib.load('Models/scaler.joblib')


from pydantic import BaseModel
# Define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    goals:int
    highest_value:int 
    age:float
   





def preprocessing(input_features: InputFeatures):
    dict_f = {
    'goals': input_features.goals,
    'highest_value': input_features.highest_value,
    'age': input_features.age,
    
    }
    # Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
    # Scale the input features
    scaled_features = scaler.transform([list(dict_f.values
    ())])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
 data = preprocessing(input_features)
 y_pred = model.predict(data)
 return {"pred": y_pred.tolist()[0]}




 if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



