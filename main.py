import os
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from typing import Annotated
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import json

load_dotenv()

app = FastAPI()
origins = [
    "*"
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

@app.get("/")
def root(): #隨意名稱都行
    return {"hello": "world"}

@app.post("/post")
async def newPost(name: Annotated[str, Form()]):
    text = name
    collection.insert_one({"name": text})
    return "ok"
        
@app.get("/post")
def getPosts():
    data = collection.find({})
    list = []
    for x in data:
        list.append({
            "_id": str(x["_id"]),
            "name": x["name"]
        })
    return list

@app.get("/post/{id}")
async def deletePost(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return "ok"