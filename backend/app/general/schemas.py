import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.repository.generated_models import SLanguage
from app.repository.schemas import SBaseListResponse


class SRegion(BaseModel):
    id: int
    names: dict
    code: Optional[str]


class SCountry(BaseModel):
    names: SLanguage
    regions: Optional[List[SRegion]]


class SStats(BaseModel):
    info: dict
    date: datetime.date


class SCountryList(SBaseListResponse):
    data: List[SCountry]




class SDisctrict(BaseModel):
    id: int
    names: dict
    district_code: str
    stats: List[SStats]


