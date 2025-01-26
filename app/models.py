from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, unique=True, index=True, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
