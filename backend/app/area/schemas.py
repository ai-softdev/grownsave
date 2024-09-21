import datetime
from typing import List

from pydantic import BaseModel

from app.repository.schemas import SBaseListResponse




class SAreaSeason(BaseModel):
    id: int
    culture_name: str
    start_date: datetime.date
    end_date: datetime.date


class SSoilIndicator(BaseModel):
    id: int
    created_at: datetime.date
    working_status: bool


class SArea(BaseModel):
    id: int
    name: str
    coordinates: list


class SAreaList(SBaseListResponse):
    data: List[SArea]


class SAreaDetail(SArea):
    seasons: List[SAreaSeason]
    soil_indicators: List[SSoilIndicator]


class SAreaCreate(BaseModel):
    name: str
    coordinates: list[str]



class SSoilIndicatorStats(BaseModel):
    datetime: datetime.datetime
    info: dict
    result: list


class SSatelliteStats(BaseModel):
    date: datetime.date
    info: dict
    result: dict


class SAreaSeasonDetail(BaseModel):
    id: int
    culture_name: str
    start_date: datetime.date
    end_date: datetime.date
    area: SArea
    soil_indicator_stats: List[SSoilIndicatorStats]
    satellite_stats: List[SSatelliteStats]


class SAreaSeasonCreate(BaseModel):
    culture_name: str
    area_id: int
    start_date: datetime.date
    end_date: datetime.date


class SAreaSeasonCreateResponse(SAreaSeason):
    area: SArea