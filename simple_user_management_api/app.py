from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from typing import Dict 

app = FastAPI()

# in-memory user datastore 
users: Dict[str, Dict[str, str]] = {}

# pydantic model for input validation 
class User(BaseModel):
    username: str
    email: str

@app.post("/user, status_code=201")
async def add_user(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="user already exists")
    
    users[user.username] = {'username': user.username, 'email': user.email}
    
@app.get("/user/{username}")
async def get_user(username: str):
    user = users.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user 