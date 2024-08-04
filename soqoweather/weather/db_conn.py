from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""Connect to sqlite database"""
engine = create_engine('sqlite:///soqo_weather.db', echo=True)

"""Base for models"""
Base = declarative_base()

'''Create a session'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

