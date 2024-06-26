from fastapi import FastAPI

from api.cartapi.cart import cart_router
from api.categoryapi.category import category_router
from api.discountapi.discount import discount_router
from api.orderapi.order import order_router
from api.photoapi.photos import photo_router
from api.productapi.products import product_router
from api.usersapi.users import user_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(photo_router)
app.include_router(discount_router)
app.include_router(category_router)