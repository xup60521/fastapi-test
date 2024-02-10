import os
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response, Form
from typing import Union, Annotated
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

import json

load_dotenv()

app = FastAPI()
origins = [
    "https://xup60521.github.io/fastapi-test"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MONGODB_URI = os.getenv("MONGODB_URI")

try:
    mongo_client = MongoClient(MONGODB_URI)
    print("connect to MongoDB")
except:
    print("Cannot connect to MongoDB")
    
db = mongo_client["ToDo"]
collection = db["data"]

class Item(BaseModel):
    str

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/post")
async def newPost(name: Annotated[str, Form()]):
    text = name
    collection.insert_one({"name": text})
    return "ok bye"

@app.get("/post")
async def getPost():
    data = collection.find({})
    jsonString = "["
    for i in data:
        jsonString += f"{i},"
    jsonString = jsonString.rstrip(",")
    jsonString += "]"
    return jsonString

@app.get("/post/{id}")
async def deletePost(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return "ok"