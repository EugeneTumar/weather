from datetime import datetime
from typing import Annotated
from fastapi import Query
from pydantic import BaseModel, Field

class SearchRequestSchema(BaseModel):
    group_num: int = Field(ge=1)
    country: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None