from sqlalchemy import Column, String, Enum, Boolean, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserEntity(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(String)
    language = Column(String, nullable=False)
    enable_notifications = Column(Boolean, nullable=False)
    create_date = Column(DateTime, nullable=False)
    enabled = Column(Boolean, nullable=False)
    display_name = Column(String, nullable=False)