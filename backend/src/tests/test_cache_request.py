from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

def test_chache_request():
    response = client.get("/getweather?country=волковыск&temp_type=K")
    response = client.get("/getweather?country=волковыск&temp_type=K")
    weather_cache = response.json()
    if not weather_cache['from_cache'] == True:
        raise Exception('Weather not caching')
    
    