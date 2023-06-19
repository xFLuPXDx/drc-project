from fastapi import FastAPI,depends
from database import get_db,engine
from sqlalchemy.orm import session
import models
import sqlite3

app = FastAPI()
#create_tables()
models.Base.metadata.create_all(bind=engine)

users=[]

@app.get("/")
def home():
    return "home"

@app.get("/about")
def about(name : str):
    return f"This is about {name}"
    
    
@app.get('/signup')
def signup(username : str,email : str ,password : str,db : session depends(get_db)):
    user=models.Users("username" = username,"email" = email,"password" = password)
    

    
@app.get('/login')
def login(username : str,password : str):
    for user in users:
        if user["username"]==username:
            if user["password"]==password:
                return "Logged in"
        else:
            return "User does not exist"
        
@app.get("/delete")
def delete(username : str,password : str):
    for i,user in enumerate(users):
        if user['username'] == username and user['password'] == password:
            del users[i]
            print("***************")
            print(users)
            print("***************")
        return "deleted"

@app.get("/update-password")
def update(username : str,password : str,new_pass : str):
    for i,user in enumerate(users):
        if user['username'] == username and user['password'] == password:
            user['password'] = new_pass
            users[i] = user
        return "updated"
