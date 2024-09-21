from typing import Dict

from fastapi import APIRouter

from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.payment.schemas import PaymentSystemData

router = APIRouter(prefix="/payment", tags=["Оплата"])



@router.post('/complete')
async def complete_payment(data: PaymentSystemData) -> Dict[str, str]:

    order = await Order.find_one_or_fail(filter=Order.transaction_id == data.transaction_id)

    # success
    if data.status_code == 0:
        await Order.update(model_id=order.id, status=OrderStatus.completed)

    # error
    elif data.status_code == 1:
        await Order.update(model_id=order.id, status=OrderStatus.error)

    return {
        'message': "Payment success"
    }
