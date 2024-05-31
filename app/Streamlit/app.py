import streamlit as st
import pandas as pd
from modules import ModelService as md
import plotly.express as px
from sklearn.decomposition import PCA

# instantiate the model service
model_service: md.ModelService = md.ModelService(
    "https://use-case-7-0dl2.onrender.com/predict"
)


df = pd.read_csv("cleaned/clean_data.csv")
st.write(df)
X = df[
    [
        "height",
        "age",
        "appearance",
        "goals",
        "assists",
        "yellow cards",
        "goals conceded",
        "clean sheets",
        "minutes played",
        "current_value",
        "highest_value",
        "position_encoded",
        "winger",
        "kmeans",
    ]
]

kvalues = X["kmeans"]
pca_components = PCA(3).fit_transform(X.drop("kmeans", axis=1))
pca_df = pd.DataFrame(data={f"PCA{i+1}": c for i, c in enumerate(pca_components.T)})
pca_df["kmeans"] = kvalues
px.scatter_3d(pca_df.head(500), x="PCA1", y="PCA2", z="PCA3", color="kmeans")


def create_sidebar() -> dict:
    """
    Create the sidebar with input fields for the model features.

    return: tuple[InputFeatures, str]
        The input features provided by the user.
    """
    st.sidebar.header("Prediction Features")

    height: float = st.sidebar.number_input(
        "Height", min_value=0.0, format="%f", key="height"
    )
    age: float = st.sidebar.number_input("Age", min_value=0, format="%d", key="age")
    appearance: int = st.sidebar.number_input(
        "Appearance", min_value=0, format="%d", key="appearance"
    )
    goals: float = st.sidebar.number_input(
        "Goals", min_value=0.0, format="%f", key="goals"
    )
    assists: float = st.sidebar.number_input(
        "Assists", min_value=0.0, format="%f", key="assists"
    )
    yellow_cards: float = st.sidebar.number_input(
        "Yellow Cards", min_value=0.0, format="%f", key="yellow_cards"
    )
    goals_conceded: float = st.sidebar.number_input(
        "Goals Conceded", min_value=0.0, format="%f", key="goals_conceded"
    )
    clean_sheets: float = st.sidebar.number_input(
        "Clean Sheets", min_value=0.0, format="%f", key="clean_sheets"
    )
    minutes_played: int = st.sidebar.number_input(
        "Minutes Played", min_value=0, format="%d", key="minutes_played"
    )
    current_value: int = st.sidebar.number_input(
        "Current Value", min_value=0, format="%d", key="current_value"
    )
    highest_value: int = st.sidebar.number_input(
        "Highest Value", min_value=0, format="%d", key="highest_value"
    )
    winger: int = st.sidebar.selectbox("Winger", options=[0, 1], key="winger")

    input_data = {
        "height": height,
        "age": age,
        "appearance": int(appearance),
        "goals": goals,
        "assists": assists,
        "yellow_cards": yellow_cards,
        "goals_conceded": goals_conceded,
        "clean_sheets": clean_sheets,
        "minutes_played": int(minutes_played),
        "current_value": int(current_value),
        "highest_value": int(highest_value),
        "winger": int(winger),
    }
    return input_data


st.write(df)
st.title("Football Player Prediction")
st.markdown("""
            Please use the Sidebar to predict the player current value.
            """)

input_data = create_sidebar()


if st.sidebar.button("Predict"):
    with st.spinner("Making prediction..."):
        result = model_service.predict(input_data)

        if "pred" in result:
            prediction = result["pred"]
            # pred_list.append(
            #     {"Player": player_name, "Current Value Prediction": prediction[0]}
            # )
            st.write(f"Resualt is {prediction[0]}")
        else:
            st.error(result["error"])
