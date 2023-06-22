from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
import models
from schemas import UserCreate

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
    return "This is about {name}"
    
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users

@app.get('/signup')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.Users(username=user.username, email=user.email , password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

    
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
