from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import joblib

# Load your trained model
model = joblib.load("lda_model.pkl")  # Ensure you save your model with joblib

app = FastAPI()

class AdmissionData(BaseModel):
    gre: int
    gpa: float
    rank: int

@app.post("/predict/")
def predict(data: AdmissionData):
    # Convert input data to numpy array and reshape for model input
    data_input = np.array([[data.gre, data.gpa, data.rank]])
    
    # Perform the prediction
    prediction = model.predict(data_input)
    
    # Return the prediction result
    status = "Accepted" if prediction[0] == 1 else "Rejected"
    return {"prediction": status}
