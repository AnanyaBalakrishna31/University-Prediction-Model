import streamlit as st
import requests

st.title("Admission Prediction App")

# Input fields for the user
gre = st.number_input("GRE Score", min_value=0, max_value=800, value=300)
gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=2.5)
rank = st.selectbox("Rank", options=[1, 2, 3, 4])

# Function to get prediction from FastAPI
def get_prediction(gre, gpa, rank):
    url = "http://localhost:8000/predict/"
    data = {"gre": gre, "gpa": gpa, "rank": rank}
    response = requests.post(url, json=data)
    return response.json()

# Predict button
if st.button("Predict"):
    result = get_prediction(gre, gpa, rank)
    st.write(f"Prediction: {result['prediction']}")