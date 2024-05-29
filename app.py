import streamlit as st
import requests
import json

st.title("Player Value Prediction App ⚽")

# Taking user inputs
appearance = st.sidebar.slider("Appearance", 0, 96, 10)
minutes_played = st.sidebar.slider("Minutes Played", 0, 8581, 500)
highest_value = st.sidebar.slider("highest_value", 0, 180000, 500)
award = st.sidebar.slider('Award', 0, 92, 1)

# Converting the inputs into a JSON format
inputs = {
    "appearance": appearance,
    "minutes_played": minutes_played,
    "highest_value": highest_value,
    "award": award
}

# When the user clicks on the button, it will fetch the API
if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="http://localhost:8000/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status()  # Check for HTTP request errors
        prediction_result = res.json()
        st.subheader(f"Prediction result 🚀 = {prediction_result}")

    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
    except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")