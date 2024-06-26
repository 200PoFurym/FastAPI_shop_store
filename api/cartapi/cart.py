from fastapi import APIRouter
from pydantic import BaseModel
from database.cartservice import *
from database import get_db
from database.models import User, Cart
from datetime import datetime


# class CartValidator(BaseModel):
#     user_id: int
#     product_id: int
#     quantity: int

cart_router = APIRouter(prefix='/cart', tags=['Корзина'])

@cart_router.post('/api/cart')
# async def add_to_cart(validator: CartValidator):
#     db = next(get_db())
#     user_cart = dict(validator)
#     user_id_cart = user_cart.get('user_id')
#     user = db.query(Cart).filter_by(user_id=user_id_cart).first()
#     if not user:
#         try:
#             reg_user_cart = add_cart_item(**user_cart)
#             return {'status': 1, 'message': reg_user_cart}
#         except Exception as a:
#             return {'status': 0, 'message': a}
#     else:
#         return {'status': 0, 'message': 'Вы не зарегестрированны'}
async def add_to_cart(user_id: int, product_id: int, quantity: int):
    data = add_cart_item(user_id=user_id, product_id=product_id, quantity=quantity)
    return data

@cart_router.delete('/api/delete_item')
async def remove_item_cart(user_id: int, product_id: int):
    data = remove_cart_item(user_id=user_id, product_id=product_id)
    return data