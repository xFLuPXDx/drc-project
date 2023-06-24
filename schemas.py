from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password : str
    
class UserCreate(UserBase):
    email: str
    
class OrderRequest(BaseModel):
    customer_name: str
    item_name: str

    class Config:
        orm_mode = True
