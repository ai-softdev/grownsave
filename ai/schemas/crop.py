from datetime import date
from typing import Optional

from pydantic import BaseModel


class SSoil_info(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: int
    ph: float


class SCrop(BaseModel):
    coord_list: list[str]
    soil_info: Optional[SSoil_info] = None
    with_ai: bool
    with_indicator: bool
