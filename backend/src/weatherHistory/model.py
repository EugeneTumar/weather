import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Float, func
from ..database import Base, engine
from ..temptype import TempType

class WeatherModel(Base):
    __tablename__ = "weather_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    temp: Mapped[float] = mapped_column(nullable=False)
    temp_type: Mapped[TempType] = mapped_column(default=TempType.K)
    weather: Mapped[str] = mapped_column(String, nullable=False)
    time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    wind_speed: Mapped[float]
    from_cache: Mapped[bool] = mapped_column(default=False)
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



Base.metadata.create_all(engine)