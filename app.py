import streamlit as st
import requests


#get
url = "http://localhost:8000/predict"
params = {
            "appearance": 104,
            "minutes_played": 9390,
            "highest_value": 70000000
}

response = requests.get(url, params=params)
print(response.json())

#post 
url = "http://localhost:8000/predict"
data = {
            "appearance": 104,
            "minutes_played": 9390,
            "highest_value": 70000000
}
response = requests.post(url, json=data)
print(response.json())