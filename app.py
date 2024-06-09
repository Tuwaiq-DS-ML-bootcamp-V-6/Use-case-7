import streamlit as st
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8000/predict"

st.title("Player Performance Predictor")

# Input fields for user to enter data
height = st.number_input('Height (cm)', min_value=0)
age = st.number_input('Age', min_value=0)
appearance = st.number_input('Appearances', min_value=0)
goals = st.number_input('Goals', min_value=0)
assists = st.number_input('Assists', min_value=0)
minutes_played = st.number_input('Minutes Played', min_value=0)
days_injured = st.number_input('Days Injured', min_value=0)
award = st.number_input('Awards', min_value=0)
highest_value = st.number_input('Highest Value ($)', min_value=0.0)
position_Attack = st.number_input('Position Attack', min_value=0)

if st.button('Predict'):
    # Create a dictionary to hold the input data
    input_data = {
        'height': height,
        'age': age,
        'appearance': appearance,
        'goals': goals,
        'assists': assists,
        'minutes_played': minutes_played,
        'days_injured': days_injured,
        'award': award,
        'highest_value': highest_value,
        'position_Attack': position_Attack
    }

    # Send a request to the FastAPI endpoint
    response = requests.post(FASTAPI_URL, json=input_data)
    
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Predicted Price: {prediction['predicted_price']}")
    else:
        st.error("Error in prediction. Please try again.")
# streamlit run app.py
