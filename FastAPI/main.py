from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Model
class User(BaseModel):
    id:int
    name:str
    lastname:str
    address:Optional[str]
    phone:int
    createdDate:datetime = datetime.now()

app = FastAPI()

@app.get("/welcome")
def welcome():
    return("Welcome")

@app.post("/withParam")
def withParam(user:User):
    user = user.dict()
    print(user)
    return True

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
