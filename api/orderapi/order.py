from fastapi import APIRouter
from pydantic import BaseModel
from database.orderservice import *
from database import get_db
from database.models import Order

# class OrderValidator(BaseModel):
#     user_id: int
#     total: float

order_router = APIRouter(prefix='/order', tags=['Ордер'])

@order_router.get('/api/order')
# async def order_user(validator: OrderValidator):
#     db = next(get_db())
#     user_order = dict(validator)
#     user_id_order = user_order.get('user_id')
#     user = db.query(Order).filter_by(user_id=user_id_order)
#     if not user:
#         try:
#             reg_order_user = create_order(**user_order)
#             return {'status': 1, 'message': reg_order_user}
#         except Exception as a:
#             return {'status': 0, 'message': a}
#     else:
#         return {'status': 0, 'message': 'Ничего не выбрано'}

async def order_user(user_id: int):
    data = create_order(user_id=user_id)
    return data