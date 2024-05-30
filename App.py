import streamlit as st
import requests
import json

# Manually include the statistics
statistics = {
    "age": {"mean": 26.04, "max": 43},
    "appearance": {"mean": 36.41, "max": 107},
    "minutes_played": {"mean": 2470.79, "max": 9510},
    "days_injured": {"mean": 117.96, "max": 2349},
    "games_injured": {"mean": 15.83, "max": 339},
    "award": {"mean": 1.96, "max": 92},
    "current_value": {"mean": 3622971, "max": 180000000}
}

st.image("pics/pngwing.com.png")
st.title(" KiRBY Predict Everything ")

st.markdown(""" Try anything i should guess them all """)

# Create columns for the input fields
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Age")
    age = st.number_input("Age", min_value=0)

    st.markdown("### Minutes Played")
    minutes_played = st.number_input("Minutes Played", min_value=0)

    st.markdown("### Games Injured")
    games_injured = st.number_input("Games Injured", min_value=0)

    st.markdown("### Current Value")
    current_value = st.number_input("Current Value", min_value=0)

with col2:
    st.markdown("### Appearance")
    appearance = st.number_input("Appearance", min_value=0)

    st.markdown("### Days Injured")
    days_injured = st.number_input("Days Injured", min_value=0)

    st.markdown("### Awards")
    award = st.number_input("Awards", min_value=0)

# Add a button for prediction
if st.button("Predict"):
    # Create input data dictionary
    input_data = {
        "age": age,
        "appearance": appearance,
        "minutes_played": minutes_played,
        "days_injured": days_injured,
        "games_injured": games_injured,
        "award": award,
        "current_value": current_value
    }

    # Make a POST request to the FastAPI endpoint
    url = "https://use-case-7-kf3q.onrender.com/predict"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(input_data), headers=headers)

    # Display the prediction result
    if response.status_code == 200:
        result = response.json()
        # Mapping from prediction to label
        prediction_mapping = {0: 'High', 1: 'Medium', 2: 'Low'}
        pred_label = prediction_mapping.get(result['pred'], "Unknown")
        st.success(f"**Predicted Value**: {pred_label}")
    else:
        st.error("Error in prediction request")

# Footer
st.markdown("---")
st.markdown("Developed by KiRBY")
