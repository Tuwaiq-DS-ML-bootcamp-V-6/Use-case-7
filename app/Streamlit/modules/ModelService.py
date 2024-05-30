import requests
import json


class ModelService:
    def __init__(self, api_url: str):
        """
        Initialize the ModelService with the FastAPI URL.

        param api_url: str
            URL of the FastAPI prediction endpoint.
        """
        self.api_url: str = api_url

    def predict(self, input_data: dict) -> dict:
        """
        Send a request to the FastAPI server to make a prediction.

        param: input_data: InputFeatures
            The input features provided by the user.
        return: dict
            The prediction result from the API.
        """
        # json_input = json.dumps(.dict())

        response = requests.post(
            self.api_url,
            json=input_data,
            headers={"Content-Type": "application/json"},
        )

        # return response.json()

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error in prediction"}
