from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import and_

from app.exceptions import NoSubscriptionException
from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.users.models import User


async def has_subscription(user: User, raise_exception=True) -> Optional[Order]:
    order = await Order.find_one_or_none(filter=and_(Order.created_at > datetime.now() - timedelta(days=30),
                                                     Order.status == OrderStatus.completed,
                                                     Order.user_id == user.id), includes=['plan'])

    if raise_exception and order is None:
        raise NoSubscriptionException

    return order
