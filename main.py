from fastapi import FastAPI,Depends
from database import SessionLocal,engine
from sqlalchemy.orm import Session
import models
import schemas


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
    if db_user and  db_user.password == password:
        return "Logged In"
    else:
        return "User does not exist"
    

    # for user in users:
    #     if user["username"]==username:
    #         if user["password"]==password:
    #             return "Logged in"
    #     else:
    #         return "User does not exist"
        
@app.post("/delete")
def delete(username : str , pwd : str ,db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user and pwd == user.password:
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
def update(username : str , pwd : str  , new_pwd : str , db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if user and pwd == user.password:
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

@app.post("/create-item")
def create_item(item : schemas.ItemCreate , db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.post("/order-item")
def order_item(order : schemas.OrderRequest , db: Session = Depends(get_db)):
    db_cid = db.query(models.Customer).filter(models.Customer.customer_name == order.customer_name).first()
    db_iid = db.query(models.Item).filter(models.Item.item_name == order.item_name).first()
    if db_cid and db_iid:
        db_order = models.Order(customer_id = db_cid.customer_id , item_id = db_iid.item_id , item_name = db_iid.item_name)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    
@app.post("/create-customer")
def create_customer(customer : schemas.CustomerRequest , db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/order-history")
def order_history(cid : int,db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == cid).first()
    if db_customer:
        db_order = db.query(models.Order).filter(models.Order.customer_id == cid).all()
        return db_order
    else:
        return "Customer does not exist"