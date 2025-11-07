class Setings:
    api_key = 'd780b73c5360b6daf9d82c05843cd40e'
    database_conn = 'postgresql://postgres:postgres@localhost:5432/weather'

settings = Setings()

class URLs:
    api = 'https://openweathermap.org/api'
    weather_api = 'http://api.openweathermap.org/data/2.5/weather'
    locals_api = 'http://api.openweathermap.org/geo/1.0/direct'

urls = URLs()