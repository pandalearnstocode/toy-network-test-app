from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str


app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}



@app.post("/login")
async def login(login_user: User):
    fake_db = {"email": "test@test.com","password": "test"}
    login_user_dict = login_user.dict()
    is_valid = login_user_dict == fake_db
    if is_valid:
        return {"message": "User logged in successfully"}
    else:
        return {"message": "User not found"}
