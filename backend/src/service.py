import json

import requests

from .temptype import TempType

from .settings import urls, settings
from .exceptions import CountryNotFound
from .weatherSchema import WeatherSchema
from .utils.tempConvertor import temp_convertor
from .weatherHistory.service import save_weather, get_cache_weather
from .utils.getGlobalName import get_global_name


def get_weather(country: str, temp_type):
    global_name = get_global_name(country)
    cache = get_cache_weather(country=global_name)

    weather = None
    if cache is None:
        weather_response = requests.get(urls.weather_api, {'q': country, 'appid': settings.api_key})
        weather_data = json.loads(weather_response.content.decode('utf-8'))
        if weather_data['cod'] == '404':
            raise CountryNotFound()
        weather = setSchema(weather_data)
    else:
        weather = cache
    if temp_type == TempType.F:
        temp_convertor.temp_to_f(weather)
    if temp_type == TempType.K:
        temp_convertor.temp_to_k(weather)
    if temp_type == TempType.C:
        temp_convertor.temp_to_c(weather)
    save_weather(weather)
    return weather

def setSchema(data) -> WeatherSchema:
    schema = WeatherSchema(
        country=data['name'],
        temp = data['main']['temp'],
        temp_type = TempType.K,
        weather = data['weather'][0]['main'],
        wind_speed = data['wind']['speed'])
    return schema
 