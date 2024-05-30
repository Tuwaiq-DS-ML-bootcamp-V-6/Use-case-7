import streamlit as st
import plotly.express as px
import pandas as pd
X = pd.read_csv('Data/DBSCAN.csv')
fig = px.scatter(X, x='height', y='goals', color='DBSCAN',
                 title='Scatter plot of height vs. goals',
                 labels={'height': 'Height', 'goals': 'Goals'})

# Display the plot in Streamlit
st.plotly_chart(fig)
