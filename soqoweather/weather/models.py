from sqlalchemy import Column, Integer, String, Float, Date
from .db_conn import Base, engine


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    date = Column(Date)
    temperature = Column(Float)
    description = Column(String)


class WeatherTest:

    def __init__(self, city, date, temperature, description):
        self.city = city
        self.date = date
        self.temperature = temperature
        self.description = description


Base.metadata.create_all(engine)
