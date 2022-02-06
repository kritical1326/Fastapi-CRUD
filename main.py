from typing import Optional
from decouple import config
from fastapi import FastAPI, Request
from pydantic import BaseModel
import time
from pymongo import MongoClient
    
mongo_url = config('MONGO')
print(mongo_url)

def get_database():
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(mongo_url,tls=True, tlsAllowInvalidCertificates=True)   

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['student']

dbname = get_database()
collection_name= dbname["student"]

app = FastAPI()

starttime = time.time()

class Student(BaseModel):
    name: str
    registration_number: str
    division: str
    fa_name: str

class StudentDelete(BaseModel):
    name: str


@app.get("/")
def healthCheck():
    return {"message": "OK", "uptime": time.time()-starttime}

@app.get("/student")
async def readItem(name: str):
    result = collection_name.find_one({"name": name})
    if result is None:
        return{"result": "failed","status": 404}
    return {"name": result["name"],"registration number": result["registration_number"], "division": result["division"], "FA name": result["fa_name"]}

@app.post("/student")
async def create_item(info : Student):
    contojson = info.json()
    collection_name.insert_one(eval(contojson))
    return {
        "status" : "SUCCESS",
        "data" : info
    }
    
@app.put("/student")
async def updateInformation(info : Student):
    return {
        "status" : "SUCCESS",
        "data" : info
    }

@app.delete("/student")
async def deleteInformation(info : StudentDelete):
    return {
        "status" : "SUCCESS",
        "data" : info
    }

