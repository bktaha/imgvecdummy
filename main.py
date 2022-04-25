"""
Dummy API

Request : JSON, deep features from 1 image
    'inputdata': List[float], len = 2048

Response : JSON, 5 items
    'itmcode': int
    'itmurl': str, URL of image in catalog

Usage :
    curl -X POST -d @deepfeatures.json -H 'Content-Type: application/json' localhost:8000/

Monday, April 25, 2022

"""
from random import randrange
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DeepFeatures(BaseModel):
    inputdata : List[float]

class Item(BaseModel):
    itmcode : int
    itmurl : str

@app.post("/", response_model=List[Item])
def get_similar(itmvec : DeepFeatures):
    return [Item(itmcode=itmcd, itmurl='https://dummyimage.com/{}'.format(itmsiz))
        for itmcd, itmsiz in zip([randrange(10) for nX in range(5)], [300,600,300,900,600])]
