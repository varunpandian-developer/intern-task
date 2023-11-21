from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
