from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
import time

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
    return {"name": name}

@app.post("/student")
async def create_item(info : Student):
    # req_info = await info.json()
    # print(req_info["name"])
    return {
        "status" : "SUCCESS",
        "data" : info
    }
    
@app.put("/student")
async def updateInformation(info : Student):
    # req_info = await info.json()
    # print(req_info["name"])
    return {
        "status" : "SUCCESS",
        "data" : info
    }

@app.delete("/student")
async def updateInformation(info : StudentDelete):
    # req_info = await info.json()
    # print(req_info["name"])
    return {
        "status" : "SUCCESS",
        "data" : info
    }
