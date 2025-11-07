from pydantic import BaseModel, Field
import datetime
from .temptype import TempType

class WeatherSchema(BaseModel):

    country: str
    temp: float
    temp_type: TempType = Field(default=TempType.K)
    weather: str
    time: datetime.datetime|None = Field(default=None)
    wind_speed: float
    from_cache: bool = Field(default=False)


