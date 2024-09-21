import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.repository.base import Base

from app.payment.models import Order
class Plan(Base):
    name = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Integer, default=0)
    system_name = Column(String(10), nullable=False)
    with_ai = Column(Boolean)
    with_indicator = Column(Boolean)


