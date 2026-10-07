from fastapi import FastAPI, HTTPException #importing FastAPI and HTTPException from fastapi module #
from pydantic import BaseModel #importing BaseModel from pydantic module #
app=FastAPI(title="Enterprise AI Assistant") #this creates our application#
@app.get("/health") #get means we are asking the server to give us information about the health of server #
def health_check(): # healtcheck is a function that performs the task #
    return {
        "status":"healthy",
        "service":"Enterprise AI Assistant"
    }
class User(BaseModel):
    name:str
    age:int
    is_learning_ai:bool

users =[
    {
        "name":"Sai",
        "age":28,
        "is_learning_ai":True
    },
    {
        "name":"Gayathri",
        "age":23,
        "is_learning_ai":False
    }
]

@app.get("/users") #get means we are asking the server to give us information about the health of server #

def get_users(): # healtcheck is a function that performs the task #
    return users

@app.get("/users/{name}") #get means we are asking the server to give us information about a specific user #
def get_user(name: str): # name is a path parameter #
    for user in users:
        if user["name"].lower() == name.lower() :
            return user
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.post("/users", status_code=201) #post means we are asking the server to create a new user #
def create_user(user: User):
    for existing_user in users:
        if existing_user["name"].lower() == user.name.lower():
            raise HTTPException(
                status_code=409,
                detail="User already exists"
            )
    users.append(user.model_dump())
    return user
