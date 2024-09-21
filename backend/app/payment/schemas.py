from pydantic import BaseModel


class PaymentData(BaseModel):
    card_num: str
    exp_month: int
    exp_year: int
    cvv: str
    plan_id: int


class PaymentSystemData(BaseModel):
    transaction_id: str
    status_code: int