from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

def test_chache_request():
    status = 200
    for i in range(40):
        response = client.get("/getweather?country=минск&temp_type=K")
        status = response.status_code
        if not (status == 429 or status == 200):
            raise Exception('Request status '+status)

    if not status == 429:
        raise Exception('Not limited')
