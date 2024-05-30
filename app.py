import streamlit as st
import requests
import json

# Title of the application
st.title("Prediction for Players Value")

# Sidebar for user inputs
appearance = st.sidebar.slider("Number of Appearances", 0, 96, 10)
minutes_played = st.sidebar.slider("Minutes Played", 0, 8581, 500)
highest_value = st.sidebar.slider("Highest Value (€)", 0, 180000, 500)
award = st.sidebar.slider("Number of Awards", 0, 92, 1)
kmeans_cluster = st.sidebar.slider("KMeans Cluster", 0, 0, 1)

# Preparing input data in JSON format
input_data = {
    "appearance": appearance,
    "minutes_played": minutes_played,
    "highest_value": highest_value,
    "award": award,
    "kmeans": kmeans_cluster
}

# Button to trigger prediction
if st.button('Predict Player Value'):
    try:
        # Ensure the correct endpoint URL
        response = requests.post(
            url="https://use-case-7-hbl3.onrender.com/predict",  # Correct endpoint for POST
            headers={"Content-Type": "application/json"},
            data=json.dumps(input_data)
        )
        response.raise_for_status()  # Raise HTTP errors if any

        # Parsing the prediction result
        prediction = response.json().get('pred')
        st.subheader(f"Predicted Value: €{prediction}")

    except requests.exceptions.RequestException as http_error:
        st.error(f"HTTP Request Error: {http_error}")
    except ValueError as json_error:
        st.error(f"JSON Parsing Error: {json_error}")
