from sqlalchemy import Column, Integer, String, Numeric
from .db import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    price_cents = Column(Integer, nullable=False, default=0)
    stock = Column(Integer, nullable=False, default=0)
