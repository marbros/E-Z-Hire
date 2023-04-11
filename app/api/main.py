# Importing necessary libraries
import uvicorn
import pickle
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib as joblib
import os

# Initializing the fast API server
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get path absolute of folder "model"
model_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model'))

# Loading up the trained model
model_path = os.path.join(model_dir, 'hireable.pkl')
model = joblib.load(model_path)

# Defining the model input types
class Candidate(BaseModel):
    gender: int
    bsc: float
    workex: int
    etest_p: float
    msc: float

# Setting up the home route
@app.get("/")
def read_root():
    return {"data": "Welcome to online employee hireability prediction model"}

# Setting up the prediction route
@app.post("/prediction/")
async def get_predict(data: Candidate):
    sample = [[
        data.gender,
        data.bsc,
        data.workex,
        data.etest_p,
        data.msc
    ]]

    hired = model.predict(sample).tolist()[0]

    response = {
        "data": {
            'prediction': hired,
            'interpretation': 'Candidate can be hired.' if hired == 1 else 'Candidate can not be hired.'
        }
    }

    return response

# Configuring the server host and port
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')