from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}