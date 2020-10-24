from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self):
        # engine://user:password@host/database
        self.engine = create_engine("mysql://sqlalch:Man30hastam!@localhost/inventory")

    def get_connection(self):
        return self.engine

    def create_session(self):
        Session = sessionmaker(bind=self.get_connection())
        return Session()
