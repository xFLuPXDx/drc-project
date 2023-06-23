from database import Base
from sqlalchemy import Column,String,Integer

class Users(Base):
    __tablename__ = 'users'

    username = Column(String,primary_key=True,nullable = False)
    password = Column(String)
    email = Column(String)

class Customer(Base):
    __tablename__ = 'customers'

    id=Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String,nullable = False)
    contact = Column(String,nullable = False)
    email = Column(String,nullable = False)
    address = Column(String,nullable = False)
