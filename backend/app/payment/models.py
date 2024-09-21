from sqlalchemy import Column, TIMESTAMP, String, Float, func, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.payment.enums import OrderStatus
from app.repository.base import Base
from app.subscription.models import Plan


class Order(Base):
    date_time = Column(TIMESTAMP, default=func.now())
    transaction_id = Column(String(100), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.waiting)
    plan_id = Column(ForeignKey("plans.id"), nullable=True)
    user_id = Column(ForeignKey("users.id"), nullable=True)
    plan = relationship("Plan")
<<<<<<< HEAD
    # user = relationship("User", back_populates='purchases')
=======
    user = relationship("User", back_populates='orders')
>>>>>>> 4a4aed333c906c46104e65267e1350c3007f844b
