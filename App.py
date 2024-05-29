import streamlit as st

# Title of the app
st.title("Hello, Streamlit!")

# Text input for the user's name
name = st.text_input("Enter your name:")

# Display a greeting message
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")
else:
    st.write("Please enter your name above.")

