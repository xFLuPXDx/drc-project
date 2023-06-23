from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password : str
    
class UserCreate(UserBase):
    email: str
    