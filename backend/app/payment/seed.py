from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.subscription.models import Plan
from app.users.models import User


class Seeder:
    @staticmethod
    async def run():
        print('payment seed')

