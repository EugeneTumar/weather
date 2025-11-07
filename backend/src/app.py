from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter
from slowapi.util import get_remote_address

from .searchRequestSchema import SearchRequestSchema
from .database import check_conn
from .temptype import TempType
from .service import get_weather
from .exceptions import CountryNotFound
from .weatherHistory.service import get_weather_history
from .utils.pingWeatherApi import ping_api


app = FastAPI(docs_url='/doc')



limiter = Limiter(
    key_func=get_remote_address
)
app.state.limiter=limiter

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get('/getweather')
@limiter.limit("30/minute")
def get_weather_endpoint(request: Request, country: str, temp_type: TempType = TempType.K):
    try:
        return get_weather(country, temp_type)
    except CountryNotFound:
        return Response(status_code=400, headers={'message': 'country not found'})
    except Exception as e:
        return Response(status_code=400, headers={'message': e})


@app.post('/gethitory')
def get_history_endpoint(search_data: SearchRequestSchema):
    try:
        return get_weather_history(search_data)
    except CountryNotFound:
        return Response(status_code=400, headers={'message': 'country not found'})
    except Exception as e:
        return Response(status_code=400, headers={'message': e})

@app.get('/health')
def health_endpoint():
    res = {'start': datetime.now()}
    try:
        db = check_conn()
        api = ping_api()
        res['end'] = datetime.now()
        res['ping'] = res['end']-res['start']
        res['error'] = ''
    except Exception as e:
        res['error'] = e
    finally:
        res['end'] = datetime.now()
        return res


@app.exception_handler(HTTPException)
async def rate_limit_exceeded(request: Request, exc: HTTPException):
    if exc.status_code == 429:
        return {"message": "Too many requests. Please try again later."}
    return {"message": "Internal Server Error"}
