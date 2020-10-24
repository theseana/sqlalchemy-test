from sqlalchemy.orm import session
from connection import Connection
from models import Product


session = Connection().create_session()

m = Product(name='Cookie', price=3, count=2)

session.add(m)
session.commit()