import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import joblib

# URL for FastAPI
api_url = "http://127.0.0.1:8000/predict"

st.title("Football Players Prediction")

# Load preprocessed dataset for clustering visualization
data = pd.read_csv('final_data.csv')  # Update with your dataset path

# Select only numeric columns for clustering
numeric_data = data.select_dtypes(include=[float, int])


# Interface for predicting player category
st.header("Predict Player Category")
appearance = st.number_input("Appearance", min_value=0)
minutes_played = st.number_input("Minutes Played", min_value=0)
highest_value = st.number_input("Highest Value", min_value=0)

if st.button("Predict"):
    input_data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "highest_value": highest_value
    }
    try:
        response = requests.post(api_url, json=input_data)
        response.raise_for_status()  # Check if the request was successful
        prediction = response.json()
        st.write(f"Predicted Category: {prediction['pred']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: Unable to get a prediction. {e}")

# View clustering results (from preloaded dataset)
st.header("View Clustering Results")
if st.button("Cluster Data"):
    st.write("Displaying clustering results...")
    st.write(data)