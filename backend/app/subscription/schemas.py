from pydantic import BaseModel


class SPlan(BaseModel):
    id: int
    name: str
    price: float
    discount: int
    with_ai: bool
    with_indicator: bool