from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password : str
    
class UserCreate(UserBase):
    email: str
    
class OrderRequest(BaseModel):
    customer_name: str
    item_name: str


class ItemCreate(BaseModel):
    item_name: str
    item_price: float

class ItemResponse(BaseModel):
    item_name: str
    item_price: float

class CustomerRequest(BaseModel):
    customer_name: str    
    customer_contact: str
    customer_email: str
    customer_address:str


