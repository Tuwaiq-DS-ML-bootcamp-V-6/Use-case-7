from fastapi import FastAPI
import json
from modules.ModelService import ModelService
from utils.InputFeatures import InputFeatures

# instantiate the model service
model_service: ModelService = ModelService(
    "model/best_model.joblib", "model/best_model_scaler.joblib"
)


app: FastAPI = FastAPI()


# GET request
@app.get("/")
def read_root() -> dict:
    """
    Handle the root endpoint.
    return: dict
    """
    # return welcome message
    return {"message": "Welcome to UseCase 7.2"}


@app.post("/predict")
async def predict(input_features: InputFeatures) -> dict:
    """
    Handle predict endpoint.

    param: input_features: InputFeatures
    return: dict
    """
    # preprocess the input features
    data = model_service.preprocess(input_features)
    # make prediction
    y_pred = model_service.predict(data)

    # return the prediction
    return {"pred": y_pred}
