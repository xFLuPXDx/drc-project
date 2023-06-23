from fastapi import FastAPI,Depends
from database import SessionLocal,engine
from sqlalchemy.orm import Session
import models
from schemas import UserCreate,UserBase


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

@app.post('/signup/')
def create_user(username : str , email : str , password : str , db: Session = Depends(get_db)):
    db_user = models.Users(username=username, email=email , password = password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

    
@app.post('/login')
def login(username : str , password : str , db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.username == username).first()
    if db_user:
        if db_user.password == password:
            return "Logged In"
        else:
            return "User does not exist"
    else:
        return "User does not exist"

    # for user in users:
    #     if user["username"]==username:
    #         if user["password"]==password:
    #             return "Logged in"
    #     else:
    #         return "User does not exist"
        
@app.post("/delete")
def delete(username : str , password : str ,db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user:
        pwd = db.query(models.Users).filter(models.Users.password == password).first()
        if pwd:
            db.query(models.Users).filter(models.Users.username == username).delete()
            db.commit()
            return "Deleted successfully"

    else:
        return "Delete unsuccessful"        
        
    # for i,user in enumerate(users):
    #     if user['username'] == username and user['password'] == password:
    #         del users[i]
    #         print("***************")
    #         print(users)
    #         print("***************")
    #     return "deleted"

@app.post("/update-password")
def update(username : str , password : str  , new_pwd : str , db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user:
        pwd = db.query(models.Users).filter(models.Users.password == password).first()
        if pwd:
            update = db.query(models.Users).filter(models.Users.username == username).first()
            update.password = new_pwd
            db.commit()
            return "Updated successfully"

    else:
        return "Updated unsuccessful"      
    # for i,user in enumerate(users):
    #     if user['username'] == username and user['password'] == password:
    #         user['password'] = new_pass
    #         users[i] = user
    #     return "updated"
