import streamlit as st
import requests
import json


st.title("Prediction for Players Value")


appearance = st.sidebar.slider("Number of Appearances", 0, 96, 10)
minutes_played = st.sidebar.slider("Minutes Played", 0, 8581, 500)
highest_value = st.sidebar.slider("Highest Value (€)", 0, 180000, 500)
height = st.sidebar.slider("Height (cm)", 150, 210, 180)
age = st.sidebar.slider("Age", 16, 45, 25)
goals = st.sidebar.slider("Goals", 0, 100, 5)
assists = st.sidebar.slider("Assists", 0, 100, 5)
yellow_cards = st.sidebar.slider("Yellow Cards", 0, 50, 0)
second_yellow_cards = st.sidebar.slider("Second Yellow Cards", 0, 10, 0)
red_cards = st.sidebar.slider("Red Cards", 0, 10, 0)
goals_conceded = st.sidebar.slider("Goals Conceded", 0, 100, 0)
clean_sheets = st.sidebar.slider("Clean Sheets", 0, 50, 0)
days_injured = st.sidebar.slider("Days Injured", 0, 365, 0)
games_injured = st.sidebar.slider("Games Injured", 0, 50, 0)
award = st.sidebar.slider("Number of Awards", 0, 92, 1)
position_encoded = st.sidebar.slider("Position Encoded", 0, 10, 0)
winger = st.sidebar.slider("Winger", 0, 1, 0)


input_data = {
    'appearance': appearance,
    'highest_value': highest_value,
    'height': height,
    'age': age,
    'goals': goals,
    'assists': assists,
    'yellow_cards': yellow_cards,
    'second_yellow_cards': second_yellow_cards,
    'red_cards': red_cards,
    'goals_conceded': goals_conceded,
    'clean_sheets': clean_sheets,
    'minutes_played': minutes_played,
    'days_injured': days_injured,
    'games_injured': games_injured,
    'award': award,
    'position_encoded': position_encoded,
    'winger': winger
}


if st.button('Predict Player Value'):
    try:

        response = requests.post(
            url="https://use-case-7-hbl3.onrender.com/predict",  
            headers={"Content-Type": "application/json"},
            data=json.dumps(input_data)
        )
        response.raise_for_status()  

        prediction = response.json().get('pred')
        st.subheader(f"Predicted Value: €{prediction}")

    except requests.exceptions.RequestException as http_error:
        st.error(f"HTTP Request Error: {http_error}")
    except ValueError as json_error:
        st.error(f"JSON Parsing Error: {json_error}")
