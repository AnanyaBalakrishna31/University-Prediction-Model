
# University Admission Prediction Web Application

This repository contains a web application for predicting university admissions based on GRE scores, GPA, and the ranking of the undergraduate institution. The application is built using Streamlit for the frontend and FastAPI for the backend, with a machine learning model trained using Linear Discriminant Analysis (LDA).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model](#model)
- [Contributing](#contributing)

## Introduction
This project aims to help students predict their chances of getting admitted to a university by entering their GRE score, GPA, and the ranking of their undergraduate institution. The prediction is based on a trained LDA model

## Features
**User-friendly Interface**: Built with Streamlit to provide an intuitive and interactive user experience.

**Backend API**: Developed using FastAPI to handle predictions efficiently.

**Machine Learning**: Uses Linear Discriminant Analysis (LDA) for predicting university admissions


## Installation

### Clone the repository:
git clone https://github.com/yourusername/university-admission-prediction.git
cd university-admission-prediction


### Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate` 


### Install the dependencies

```bash 
pip install -r requirements.txt
```
## Running the Application
#Start the FastAPI backend:



uvicorn app:app --reload
The API will be available at http://127.0.0.1:8000.

#Start the Streamlit frontend:

streamlit run app.py
The web app will be accessible at http://localhost:8501.

## Making Predictions
Enter the GRE score, GPA, and rank in the Streamlit app.

The app will send a request to the FastAPI backend, which will return the admission prediction.

## Files

app.py: Streamlit frontend that interacts with the FastAPI backend.

train_lda_model.py: Script used to preprocess the data, train the LDA model, and save it as lda_model.pkl.

lda_model.pkl: The pre-trained LDA model used by the backend for predictions.

requirements.txt: List of Python dependencies required to run the application.

Model Training
If you want to retrain the model or use your own dataset:

## Prepare your dataset with columns: admit, gre, gpa, and rank.

Run the training script:

python train_lda_model.py
This will generate a new lda_model.pkl file.

API Documentation
The FastAPI backend provides the following endpoint:

Endpoint: /predict

#Method: POST

Request Body:
{
  "gre": 320,
  "gpa": 3.5,
  "rank": 1
}

Response:
{
  "prediction": 1
}

License

This project is licensed under the MIT License. See the LICENSE file for more details.






