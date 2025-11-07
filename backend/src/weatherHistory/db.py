from datetime import datetime
from sqlalchemy import select, delete, update, desc
from sqlalchemy.orm import Session

from .model import WeatherModel

from ..database import connection

@connection
def db_add_weather(session: Session, weather: WeatherModel):
    session.add(weather)
    session.commit()
    
@connection
def db_get_last_nocache_weather_by_country(session: Session, country: str):
    query = select(WeatherModel).where(WeatherModel.country==country).where(WeatherModel.from_cache == False).order_by(desc(WeatherModel.id))
    result = session.execute(query)
    weather_seq = result.scalars().first()
    return weather_seq
    
@connection
def db_get_weather_group(session: Session, 
                         group_num: int, 
                         group_size:int = 10, 
                         country: str | None = None, 
                         start_date: datetime | None = None, 
                         end_date: datetime | None = None):
    query = select(WeatherModel)

    if not country is None:
        query = query.where(WeatherModel.country == country)

    if not start_date is None:
        query = query.where(WeatherModel.time > start_date)

    if not end_date is None:
        query = query.where(WeatherModel.time < end_date)

    offset = (group_num-1)*group_size
    query = query.offset(offset).limit(group_size)
    result = session.execute(query)
    weather_seq = result.scalars().all()
    return weather_seq
   
