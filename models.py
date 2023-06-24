from database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,Float
from sqlalchemy.orm import relationship,mapped_column
class Users(Base):
    __tablename__ = 'users'

    username = Column(String,primary_key=True,nullable = False)
    password = Column(String)
    email = Column(String)

class Customer(Base):
    __tablename__ = 'customers'

    customer_id=Column(Integer,primary_key= True , autoincrement=True)
    customer_name = Column(String,nullable = False)
    customer_contact = Column(String,nullable = False)
    customer_email = Column(String,nullable = False)
    customer_address = Column(String,nullable = False)
    

class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer,primary_key=True,autoincrement=True)
    item_name = Column(String,nullable = False)
    item_price = Column(Float,nullable = False)
   

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = mapped_column(Integer, ForeignKey('customers.customer_id'))
    item_id = mapped_column(Integer, ForeignKey('items.item_id'))
    item_name = mapped_column(String, ForeignKey('items.item_name'))

    # customer = relationship("Customer", backref="orders")
    # item = relationship("Item", backref="orders")

    
