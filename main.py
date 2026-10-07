from fastapi import FastAPI, HTTPException #importing FastAPI and HTTPException from fastapi module #
app=FastAPI(title="Enterprise AI Assistant") #this creates our application#
@app.get("/health") #get means we are asking the server to give us information about the health of server #
def health_check(): # healtcheck is a function that performs the task #
    return {
        "status":"healthy",
        "service":"Enterprise AI Assistant"
    }
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

