from app.db.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(Integer)
    createdDate = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    state = Column(Boolean)
