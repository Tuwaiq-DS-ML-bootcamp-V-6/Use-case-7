import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import json
import requests

Cdf = pd.read_csv("Data\clustered.csv")

#title and Introduction
st.title('Discover more about the favorite worldwide sport "Football".')

# #Introduction
st.write("have you ever wondered if teams save their important players for important matches or do they keep placing them in every possible match?")
st.write("well we made this visualization to answer that.")

fig = px.scatter(Cdf, x='minutes_played',y='highest_value',title="Football", color="kmeans")

fig.update_layout(
    xaxis_title='minutes played',
    yaxis_title='value',
    title_x=0.5,
) 

st.plotly_chart(fig)
st.write("")
st.write("Want to see which cluster your player places in?")
st.write("Please Input the values of the player you want to predict")
goals = st.slider("goals",0, 20, 13)
assists = st.slider("assists",0, 11, 4 )
award = st.slider("award",0, 10, 6 )
highest_value = st.slider("highest_value",0, 130000000, 1500000)
appearance = st.slider("appearance",0 , 100, 20 )
minutes_played = st.slider("minutes_played",0, 8000, 3000 )
yellow_cards = st.slider("yellow_cards", 0, 20, 5)
games_injured = st.slider("games_injured",0, 70, 30)

inputs = {"appearance":appearance, "minutes_played":minutes_played, "games_injured":games_injured, "award":award, "highest_value":highest_value, "goals":goals, "assists":assists, "yellow_cards":yellow_cards}

if st.button('Predict'):
    res = requests.post(url = "http://127.0.0.1:8000/predict" , data = json.dumps(inputs),headers={"Content-Type": "application/json"})

    if res.status_code == 200:
        result = res.json()
        st.write(f"The player is predicted in cluster {result['pred']}")
    else:
        st.write("Error in prediction request")