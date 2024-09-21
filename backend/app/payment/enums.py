from enum import Enum


class OrderStatus(Enum):
    waiting = 'waiting'
    completed = 'completed'
    canceled = 'canceled'
    error = 'error'
