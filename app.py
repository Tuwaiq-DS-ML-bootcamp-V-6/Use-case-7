import streamlit as st
import requests
import json
st.title('My prediction app ')

height = st.sidebar.slider('Height', 0, 218, 10)
age = st.sidebar.slider('Age', 15, 40, 25)
appearance = st.sidebar.slider('Appearance', 0, 150, 50)
goals = st.sidebar.slider('Goals', 0, 50, 10)
assists = st.sidebar.slider('Assists', 0, 30, 5)
yellow_cards = st.sidebar.slider('Yellow Cards', 0, 20, 2)
red_cards = st.sidebar.slider('Red Cards', 0, 10, 1)
goals_conceded = st.sidebar.slider('Goals Conceded', 0, 50, 10)
clean_sheets = st.sidebar.slider('Clean Sheets', 0, 30, 5)
minutes_played = st.sidebar.slider('Minutes Played', 0, 10000, 2500)
days_injured = st.sidebar.slider('Days Injured', 0, 365, 0)
games_injured = st.sidebar.slider('Games Injured', 0, 50, 0)
award = st.sidebar.slider('Award', 0, 50, 5)
current_value = st.sidebar.slider('Current Value', 0, 200000, 50000)
highest_value = st.sidebar.slider('Highest Value', 0, 500000, 100000)
#player_price_category = st.sidebar.selectbox('Player Price Category', [0, 1, 2])
winger = st.sidebar.slider('Winger (1 for Yes, 0 for No)', 0, 1, 0)
second_yellow_cards = st.sidebar.slider('Second Yellow Cards', 0, 5, 0)

input_features = {
    'height': height,
    'age': age,
    'appearance': appearance,
    'goals': goals,
    'assists': assists,
    'yellow cards': yellow_cards,
    'red cards': red_cards,
    'goals conceded': goals_conceded,
    'clean sheets': clean_sheets,
    'minutes played': minutes_played,
    'days_injured': days_injured,
    'games_injured': games_injured,
    'award': award,
    'current_value': current_value,
    'highest_value': highest_value,
    #'player_price_category': player_price_category,
    'winger': winger,
    'second yellow cards': second_yellow_cards
}


if st.button('Get Prediction'):
     try:
       
        res = requests.post(
           url="https://use-case7api.onrender.com/predict",
           
            headers={"Content-Type": "application/json"},
            data=json.dumps(input_features)
        )
        res.raise_for_status()  # Check for HTTP request errors
        st.subheader(f"Prediction result  = {res.json()}")

     except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
     except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")