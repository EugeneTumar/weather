from datetime import datetime
from sqlalchemy import  func
from datetime import datetime

from .model import WeatherModel
from .db import db_get_weather_group, db_add_weather, db_get_last_nocache_weather_by_country

from ..utils.getGlobalName import get_global_name
from ..searchRequestSchema import SearchRequestSchema
from ..weatherSchema import WeatherSchema


def save_weather(weather: WeatherSchema):
    model = WeatherModel(**weather.model_dump())
    db_add_weather(weather=model)

def get_cache_weather(country: str):
    weather = db_get_last_nocache_weather_by_country(country=country)

    if weather is None:
        return None
    
    now = datetime.now(tz=weather.time.tzinfo)
    delta = now - weather.time
    if delta.total_seconds() < 300:
        weather.from_cache = True
        weather.time = now
        return WeatherSchema(country=weather.country, temp=weather.temp, temp_type=weather.temp_type, weather=weather.weather, time=weather.time, wind_speed=weather.wind_speed, from_cache=weather.from_cache)
    
    return None

def get_weather_history(search_data: SearchRequestSchema):
    if not search_data.country is None:
        search_data.country = get_global_name(search_data.country)

    return db_get_weather_group(**search_data.model_dump())