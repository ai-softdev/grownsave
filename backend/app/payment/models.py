


from sqlalchemy import Column, TIMESTAMP, String, Float, func, Enum
from sqlalchemy.orm import relationship

from app.payment.enums import OrderStatus
from app.repository.base import Base


class Order(Base):
    date_time = Column(TIMESTAMP, default=func.now())
    transaction_id = Column(String(100), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.waiting)
    purchase = relationship('Purchase', back_populates='order', uselist=False)
