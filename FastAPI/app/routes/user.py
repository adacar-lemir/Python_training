from fastapi import APIRouter
from app.schemas import User

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

users = []

@router.get('/welcome')
def welcome():
    return("Welcome")

@router.get('/user')
def getUsers():
    return users

@router.post('/user')
def createUser(user:User):
    user = user.dict()
    users.append(user)
    return {"user created succesfully"}

@router.get('/user/{user_id}')
def getUser(user_id:int):
    for user in users:
        if user['id']==user_id:
            return user
    return {"user not found"}

@router.delete('/user/{user_id}')
def deleteUser(user_id:int):
    for index,user in enumerate(users):
        if user['id']==user_id:
            users.pop(index)
            return {"user deleted succesfully"}
    return {"user not found"}

@router.put('/user/{user_id}')
def updateUser(user_id:int, updateUser:User):
    for index,user in enumerate(users):
        if user['id']==user_id:
            users[index] = updateUser
            return {"user updated succesfully"}
    return {"user not found"}
