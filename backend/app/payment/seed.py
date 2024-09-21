from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.subscription.models import Plan
from app.users.models import User


class Seeder:
    @staticmethod
    async def run():
        print('payment seed')
        user = await User.find_one_or_fail(filter=User.email == 'oktanc71@yandex.com')
        pro_plan = await Plan.find_one_or_fail(filter=Plan.system_name == 'pro')
        await Order.first_or_create(
            filter=Order.transaction_id == 'test_transaction',
            amount=25,
            status=OrderStatus.completed,
            user_id=user.id,
            plan_id=pro_plan.id
        )
