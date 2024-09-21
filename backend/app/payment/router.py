from fastapi import APIRouter

from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.payment.schemas import PaymentSystemData

router = APIRouter(prefix="/payment", tags=["Оплата"])



@router.post('/complete')
async def complete_payment(data: PaymentSystemData):

    order = await Order.find_one_or_none(filter=Order.transaction_id == data.transaction_id)

    # success
    if data.status_code == 0:
        order.status = OrderStatus.completed

    # error
    elif data.status_code == 1:
        order.status = OrderStatus.error


