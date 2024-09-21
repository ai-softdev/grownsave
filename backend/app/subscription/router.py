import uuid
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy import and_

from app.exceptions import AlreadyPurchasedException
from app.payment.enums import OrderStatus
from app.payment.models import Order
from app.payment.schemas import PaymentData
from app.request import request
from app.subscription.models import Plan
from app.subscription.tools import has_subscription
from app.users.dependencies import get_current_user
from app.users.models import User

from app.config import settings

router = APIRouter(prefix="/subscription", tags=["Подписка"])


@router.post('/purchase')
async def implement_creating_subscription(data: PaymentData, user: User = Depends(get_current_user)) -> dict[str, str]:


    plan = await Plan.find_by_id_or_fail(model_id=data.plan_id)

    if await has_subscription(user, raise_exception=False):
        raise AlreadyPurchasedException

    '''
    Imitation of creating payment bill
    
    token_response = await request.post('<url for creating token>', data={'card_num': plan.card_num,
                                                                 'exp_month': data.exp_month,
                                                                 'exp_year': data.exp_year,
                                                                 'cvv': data.cvv})
    token = token_response['token']
    
    create_transaction_response = await request.post('<url for creating transaction>', data={'token': token,
                                                                                    'amount': plan.price})
    transaction_id = create_transaction_response['transaction_id']
    
    
    order = await Order.create(transaction_id=transaction_id, amount=plan.price, plan_id=plan.id, user_id=user.id)

    '''
    await Order.create(transaction_id=str(uuid.uuid4()), amount=plan.price, plan_id=plan.id, user_id=user.id)

    return {
        'message': 'Order is created. Waiting to purchase'
    }





