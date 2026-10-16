import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(title='Placement Analytics', version='1.0',
              description='Lightgbm model is used for prediction')

# Initialize model artifacte files. This will be loaded at the start of FastAPI model server.
le  = joblib.load('../model/label_encoder.joblib')
clf = joblib.load('../model/lgb_model.joblib')
features = joblib.load('../model/features.joblib')
categorical_features = joblib.load('../model/categorical_features.joblib')

class Data(BaseModel):
    sl_no: int
    ssc_p: float
    hsc_p: float
    degree_p: float
    etest_p: float
    mba_p: float
    gender: str
    ssc_b: str
    hsc_b: str
    hsc_s: str
    degree_t: str
    workex: str
    specialisation: str

# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'Welcome to this Application'}

# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict(data: Data):
    # Extract data in correct order
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    # Select features required for making prediction
    data_df = data_df[features]
    # Perform label encoding for categorical features
    data_df[categorical_features] = le.transform(data_df[categorical_features])
    # Create prediction
    prediction = clf.predict(data_df)
    # Map prediction to appropriate label
    prediction_label = ['Placed' if label == 0 else 'Not Placed' for label in prediction ]
    # Return response back to client
    return {"prediction": prediction_label}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)
    