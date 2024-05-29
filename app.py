import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


df = pd.read_csv("Data\Final_data2.csv")
Cdf = pd.read_csv("Data\clustered.csv")

#title and Introduction
st.title("Discover more about the favourite worldwide sport football")

# #Introduction
st.write("have you ever wondered if teams save the players for important matches or keep putting them to the field?")
st.write("well we made this visualization to answer that.")

fig = px.scatter(Cdf, x='minutes played',y='highest_value',title="Football", color="kmeans")

fig.update_layout(
    xaxis_title='minutes played',
    yaxis_title='value',
    title_x=0.5,
) 

st.plotly_chart(fig)

