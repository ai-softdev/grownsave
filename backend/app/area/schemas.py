import datetime
from typing import List

from pydantic import BaseModel

from app.repository.schemas import SBaseListResponse


class SArea(BaseModel):
    id: int
    name: str
    coordinates: list


class SAreaSeason(BaseModel):
    id: int
    culture_name: str
    start_date: datetime.date
    end_date: datetime.date


class SSoilIndicator(BaseModel):
    id: int
    created_at: datetime.date
    working_status: bool


class SAreaDetail(SArea):
    seasons: List[SAreaSeason]
    soil_indicators: List[SSoilIndicator]


class SAreaList(SBaseListResponse):
    data: List[SArea]


class SAreaSeasonDetail(BaseModel):
    id: int
    culture_name: str
    start_date: datetime.date
    end_date: datetime.date
    area: SArea

