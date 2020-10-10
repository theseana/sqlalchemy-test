from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from connection import Connection

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30))
    price = Column(Integer())
    count = Column(Integer())
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

    def __init__(self, name=None, price=None, count=None):
        self.name = name
        self.price = price
        self.count = count


engine = Connection().get_connection()
if not engine.dialect.has_table(engine, 'products'):  # If table don't exist, Create. 
    Base.metadata.create_all(engine, checkfirst=True)
else:
    print('Database {} exists!'.format('products'))