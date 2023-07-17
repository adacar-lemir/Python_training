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
users = []

@app.get('/welcome')
def welcome():
    return("Welcome")

@app.get('/user')
def getUsers():
    return users

@app.post('/user')
def createUser(user:User):
    user = user.dict()
    users.append(user)
    return {"user created succesfully"}

@app.get('/user/{user_id}')
def getUser(user_id:int):
    for user in users:
        if user['id']==user_id:
            return user
    return {"user not found"}

@app.delete('/user/{user_id}')
def deleteUser(user_id:int):
    for index,user in enumerate(users):
        if user['id']==user_id:
            users.pop(index)
            return {"user deleted succesfully"}
    return {"user not found"}

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
