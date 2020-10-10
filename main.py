from sqlalchemy.orm import session
from connection import Connection
from models import Product


session = Connection.get_connection()

m = Product(name='IceCream', price=2, count=1)

session.add(m)
session.commit()