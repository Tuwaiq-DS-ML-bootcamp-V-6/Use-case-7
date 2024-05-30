import streamlit as st
import plotly.express as px
import pandas as pd
import json
import requests

X = pd.read_csv('Data/DBSCAN.csv')
st.markdown('# Can we group players based on their some information')
fig = px.scatter(X, x='height', y='goals', color='DBSCAN',
                 title='Scatter plot of height vs. goals',
                 labels={'height': 'Height', 'goals': 'Goals'})

# Display the plot in Streamlit
st.plotly_chart(fig)
st.write('apparently no. Try to plug some values to try the grouping model')


height = st.slider("height",150.0, 220.0, 160.0)
age = st.slider("age",18.0, 40.0, 24.0 )
appearance = st.slider("appearance",0, 5, 2 )
goals = st.slider("goals",0.0, 1.0, 0.3)
appearance = st.slider("appearance",0 , 100, 20 )
assists = st.slider("assists",0.0, 2.0, 1.0 )
goals_conceded = st.slider("goals_conceded", 0.0, 1.0, 0.2)
highest_value = st.slider("highest_value",100000, 10000000, 1200000)
position_encoded = st.slider("position_encoded", 0, 4, 2)
winger = st.slider("winger",0, 1, 0)

inputs = {"height":height,
          "age":age,
          "appearance":appearance,
          "goals":goals,
          "appearance":appearance,
          "assists":assists,
          "goals_conceded":goals_conceded,
          "highest_value":highest_value,
          "position_encoded":position_encoded,
          "winger":winger,
         }

if st.button('Predict'):
    res = requests.post(url = "https://back-end-proj.onrender.com/predict" , data = json.dumps(inputs),headers={"Content-Type": "application/json"})

    if res.status_code == 200:
        result = res.json()
        st.write(f"Based on these information it is in cluster {result['pred']}")
    else:
        st.write("Try Again")
