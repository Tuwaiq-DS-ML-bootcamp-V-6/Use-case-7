from pydantic import BaseModel


# define a Pydantic model for input data validation
class InputFeatures(BaseModel):
    """
    Data model for input features.

    Attributes:
    height: float - The height of the player.
    age: float - The age of the player.
    appearance: int - The number of appearances.
    goals: float - The number of goals.
    assists: float - The number of assists.
    yellow_cards: float - The number of yellow cards.
    goals_conceded: float - The number of goals conceded.
    clean_sheets: float - The number of clean sheets.
    minutes_played: int - The number of minutes played.
    current_value: int - The current market value of the player.
    highest_value: int - The highest market value of the player.
    winger: int - Whether the player is a winger.
    """

    height: float
    age: float
    appearance: int
    goals: float
    assists: float
    yellow_cards: float
    goals_conceded: float
    clean_sheets: float
    minutes_played: int
    current_value: int
    highest_value: int
    winger: int
