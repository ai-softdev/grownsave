from pydantic import create_model

from app.exceptions import ModelNotFoundException
from app.repository.base import Base
from app.database import async_session_maker
from sqlalchemy import Column, String, DateTime, ForeignKey, select, JSON, func, Boolean, UniqueConstraint, insert, Text
from sqlalchemy.orm import joinedload, Mapped
from app.area.models import Area
from sqlalchemy.orm import relationship
from app.payment.models import Order

class Role(Base):
    users = relationship("User", back_populates="role")
    system_name = Column(String, nullable=True)


class User(Base):
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    patronymic = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role_id = Column(ForeignKey("roles.id", ondelete="cascade"))
    role = relationship("Role", back_populates="users")
    created_at = Column(DateTime, default=func.now())
    phone = Column(String, nullable=True)
    areas = relationship("Area", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    orders = relationship("Order", back_populates='user')

    def __str__(self):
        return f"{self.email}"

class Notification(Base):

    created_at = Column(DateTime, default=func.now())
    text = Column(Text, nullable=False)
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="notifications")

