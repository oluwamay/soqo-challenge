from sqlalchemy import Column, Integer, String, Float, Date
from .db_conn import Base, engine


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    date = Column(Date)
    temperature = Column(Float)
    description = Column(String)


Base.metadata.create_all(engine)
