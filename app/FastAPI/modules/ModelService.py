import joblib
from utils.InputFeatures import InputFeatures
import numpy as np


class ModelService:
    def __init__(self, model_path: str, scaler_path: str):
        """
        Initialize the ModelService with paths to the model and scaler.

        param model_path: str
            Path to the trained model file.
        param scaler_path: str
            Path to the scaler file for preprocessing.
        """
        # load the model and scaler
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def preprocess(self, input_features: InputFeatures) -> np.ndarray:
        """
        preprocess the input features for the model
        param: input_features: InputFeatures
        return: np.ndarray
        """
        # create a dictionary with feature names and values
        dict_f: dict = {
            "height": input_features.height,
            "age": input_features.age,
            "appearance": input_features.appearance,
            "goals": input_features.goals,
            "assists": input_features.assists,
            "yellow_cards": input_features.yellow_cards,
            "goals_conceded": input_features.goals_conceded,
            "clean_sheets": input_features.clean_sheets,
            "minutes_played": input_features.minutes_played,
            "current_value": input_features.current_value,
            "highest_value": input_features.highest_value,
            "winger": input_features.winger,
        }

        # scale the input features
        scaled_features = self.scaler.transform([list(dict_f.values())])

        # return the scaled features
        return scaled_features

    def predict(self, data: np.ndarray) -> list[float]:
        """
        make predictions using the model
        param: data: np.ndarray
        return: List[float]
        """
        # make prediction using the model
        y_pred: np.ndarray = self.model.predict(data)

        # return the prediction
        return y_pred.tolist()

    def get_teams(self) -> list[str]:
        """
        get the list of teams
        return: List[str]
        """
        return [
            "AC Milan",
            "ACF Fiorentina",
            "AFC Bournemouth",
            "AS Monaco",
            "AS Roma",
            "Ajax Amsterdam",
            "Arsenal FC",
            "Aston Villa",
            "Atalanta BC",
            "Athletic Bilbao",
            "Atlético de Madrid",
            "Bayer 04 Leverkusen",
            "Bayern Munich",
            "Borussia Dortmund",
            "Borussia Mönchengladbach",
            "Brentford FC",
            "Brighton & Hove Albion",
            "Chelsea FC",
            "Crystal Palace",
            "Everton FC",
            "FC Barcelona",
            "FC Porto",
            "Fulham FC",
            "Inter Milan",
            "Juventus FC",
            "Leeds United",
            "Leicester City",
            "Liverpool FC",
            "Manchester City",
            "Manchester United",
            "Newcastle United",
            "Nottingham Forest",
            "Olympique Lyon",
            "Olympique Marseille",
            "Paris Saint-Germain",
            "RB Leipzig",
            "Real Sociedad",
            "SL Benfica",
            "SSC Napoli",
            "Southampton FC",
            "Stade Rennais FC",
            "Tottenham Hotspur",
            "Villarreal CF",
            "West Ham United",
            "Wolverhampton Wanderers",
        ]
