from fastapi import APIRouter
from database.discountservice import *



discount_router = APIRouter(prefix='/discounts', tags=['Скидки'])

@discount_router.post('/api/discount')
async def create_discount_db(product_id: int, pers: float):
    data = create_discount(product_id=product_id, pers=pers)
    return data

@discount_router.get('/api/all_discount')
async def get_all_discount_db():
    data = get_all_discount()
    return data

@discount_router.get('/api/get_by_product_id')
async def get_by_product_id(product_id: int):
    data = get_discount_by_product(product_id)
    return data

@discount_router.delete('/api/delete_discount')
async def delete_discount_db(id: int):
    data = delete_discount(id=id)
    return data