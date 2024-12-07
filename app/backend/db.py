from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("sqlite:///taskmanager.db'", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# class Base(DeclarativeBase):
#     pass