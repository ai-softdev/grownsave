from sqlalchemy import Column, TIMESTAMP, String, Float, func, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.payment.enums import OrderStatus
from app.repository.base import Base
from app.subscription.models import Plan


class Order(Base):
    created_at = Column(DateTime, default=func.now())
    transaction_id = Column(String(100), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.waiting)
    plan_id = Column(ForeignKey("plans.id"), nullable=True)
    user_id = Column(ForeignKey("users.id"), nullable=True)
    plan = relationship("Plan")
    user = relationship("User", back_populates='orders')

