import sqlite3 #importing sqlite3 module to connect to the database #

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

class UserUpdate(BaseModel):
    name:str|None=None
    age:int|None=None
    is_learning_ai:bool|None=None



@app.get("/users")
def get_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, age, is_learning_ai
        FROM users
    """)

    rows = cursor.fetchall()

    connection.close()

    users_from_db = []

    for row in rows:
        users_from_db.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "is_learning_ai": bool(row[3])
        })

    return users_from_db

@app.get("/users/{name}")
def get_user(name: str):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, age, is_learning_ai
        FROM users
        WHERE LOWER(name) = LOWER(?)
        """,
        (name,)
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": row[0],
        "name": row[1],
        "age": row[2],
        "is_learning_ai": bool(row[3])
    }

@app.post("/users", status_code=201)
def create_user(user: User):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE LOWER(name) = LOWER(?)",
        (user.name,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        connection.close()
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    cursor.execute("""
        INSERT INTO users (name, age, is_learning_ai)
        VALUES (?, ?, ?)
    """, (
        user.name,
        user.age,
        user.is_learning_ai
    ))

    connection.commit()
    connection.close()

    return user

@app.patch("/users/{name}")
def update_user(name: str, user_update: UserUpdate):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, age, is_learning_ai
        FROM users
        WHERE LOWER(name) = LOWER(?)
        """,
        (name,)
    )

    row = cursor.fetchone()

    if row is None:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_name = user_update.name if user_update.name is not None else row[1]
    new_age = user_update.age if user_update.age is not None else row[2]
    new_is_learning_ai = (
        user_update.is_learning_ai
        if user_update.is_learning_ai is not None
        else bool(row[3])
    )

    cursor.execute(
        """
        UPDATE users
        SET name = ?, age = ?, is_learning_ai = ?
        WHERE id = ?
        """,
        (
            new_name,
            new_age,
            new_is_learning_ai,
            row[0]
        )
    )

    connection.commit()
    connection.close()

    return {
        "id": row[0],
        "name": new_name,
        "age": new_age,
        "is_learning_ai": new_is_learning_ai
    }

@app.delete("/users/{name}")
def delete_user(name: str):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE LOWER(name) = LOWER(?)
        """,
        (name,)
    )

    row = cursor.fetchone()

    if row is None:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (row[0],)
    )

    connection.commit()
    connection.close()

    return {
        "message": f"{name} deleted successfully"
    }