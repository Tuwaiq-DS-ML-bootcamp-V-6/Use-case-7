import streamlit as st
import requests
import json

st.title("Player Value Prediction App :soccer:")


# Taking user inputs
appearance = st.sidebar.slider("Appearance", 0, 96, 10)
minutes_played = st.sidebar.slider("Minutes Played", 0, 8581, 500)
current_value = st.sidebar.slider("Current Value (in thousands)", 0, 180000, 500)
award = st.sidebar.slider('Award', 0, 92, 1)

appearance=int(appearance)
minutes_played=int(minutes_played)
current_value=int(current_value)
award=int(award)


# Converting the inputs into a JSON format

inputs = {
    "appearance": appearance,
    "minutes_played": minutes_played,
    "current_value": current_value,
    "award": award
}



# When the user clicks on the button, it will fetch the API
if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="https://football-player-price-predict.onrender.com/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status() 
        st.write(f" cluster name as {res.json().get('pred')}")

    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
    except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")        
