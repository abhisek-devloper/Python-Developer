from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# FastAPI app
app = FastAPI(title="Income Prediction API")

# Request body structure
class InputData(BaseModel):
    age: int
    experience: int

# Prediction route
@app.post("/predict")
def predict(data: InputData):
    input_data = [[data.age, data.experience]]
    prediction = model.predict(input_data)[0]
    result = "Income > 50K" if prediction == 1 else "Income ≤ 50K"
    return {"prediction": result}
