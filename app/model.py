from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)


class RegisterClient(Base):
    __tablename__ = 'register_client'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    tax_id = Column(String(14))
