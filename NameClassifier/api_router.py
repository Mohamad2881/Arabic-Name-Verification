from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


from NameClassifier.get_predictions import Model

app = FastAPI()
model = Model()

class QueryName(BaseModel):
    Name: str

class QueryNameList(BaseModel):
    name_list: List[str]

class PredictionObject(BaseModel):
    Name: str
    result: str
    score: float

class PredictionsList(BaseModel):
    predictions: List[PredictionObject]

@app.get("/")
def read_root():
    return {"Server is up"}    

@app.post("/predict", summary="Predict single input")
def predict(query_text: QueryName):
    
    prediction = model.classify([query_text.Name])[0]
    return PredictionObject(**prediction)


@app.post("/predict-batch", summary="predict a batch of sentences")
def predict_batch(query_text_list:QueryNameList):
    predictions = model.classify(query_text_list.name_list)
    return PredictionsList(predictions=predictions)