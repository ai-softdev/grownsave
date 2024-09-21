import datetime

from sqlalchemy import Column, TIMESTAMP, String, Float
from sqlalchemy.orm import relationship

from app.repository.base import Base


class Order(Base):
    dt = Column(TIMESTAMP, default=datetime.datetime)
    transaction_id = Column(String(100), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    purchase = relationship('Purchase', back_populates='order', uselist=False)