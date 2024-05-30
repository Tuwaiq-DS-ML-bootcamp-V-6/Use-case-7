import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt


st.title("Football Players Categories Prediction")


feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):

    payload = {
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3,
        
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    prediction = response.json()["category"]
    st.write(f"The predicted category is: {prediction}")


st.title("Clustering Results Visualization")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if 'cluster' in df.columns:
        clusters = df['cluster'].unique()
        fig, ax = plt.subplots()
        for cluster in clusters:
            cluster_data = df[df['cluster'] == cluster]
            ax.scatter(cluster_data['feature1'], cluster_data['feature2'], label=f'Cluster {cluster}')
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("The CSV file does not contain a 'cluster' column.")
