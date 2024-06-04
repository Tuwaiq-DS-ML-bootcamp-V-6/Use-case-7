import streamlit as st
import requests

st.set_page_config(page_title="Player Price Prediction", page_icon="⚽")

st.title("Tuwaiq Academy Player Price Prediction App")

st.sidebar.header("Input Features")

appearance = st.sidebar.number_input("Appearance", min_value=0, max_value=100, value=0)
award = st.sidebar.number_input("Award", min_value=0, max_value=10, value=0)
highest_value = st.sidebar.number_input("Highest Value", min_value=0.0, max_value=1e6, value=0.0)
goals = st.sidebar.number_input("Goals", min_value=0, max_value=100, value=0)
assists = st.sidebar.number_input("Assists", min_value=0, max_value=100, value=0)
yellow_cards = st.sidebar.number_input("Yellow Cards", min_value=0, max_value=20, value=0)
kmeans = st.sidebar.number_input("Kmeans", min_value=0.0, max_value=10.0, value=0.0)

if st.sidebar.button("Predict"):
    input_data = {
        "appearance": appearance,
        "award": award,
        "highest_value": highest_value,
        "goals": goals,
        "assists": assists,
        "yellow_cards": yellow_cards,
        "kmeans": kmeans
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
    
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Predicted Player Price: {prediction['predicted_price']}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
