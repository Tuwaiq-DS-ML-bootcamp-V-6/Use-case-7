import streamlit as st
import plotly.express as px
import pandas as pd
X = pd.read_csv('Data/DBSCAN.csv')
fig = px.scatter(X, x='assists', y='position_encoded', color='DBSCAN',
                 title='Scatter plot of Assists vs. Position Encoded',
                 labels={'assists': 'Assists', 'position_encoded': 'Position Encoded'})

# Display the plot in Streamlit
st.plotly_chart(fig)
