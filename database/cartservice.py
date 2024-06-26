from database.models import Cart
from database import get_db
from datetime import datetime

def add_cart_item(user_id, product_id, quantity):
    db = next(get_db())
    if user_id:
        new = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        db.add(new)
        db.commit()
        db.refresh(new)
        return f'Для пользователя {new.user_id} успешно добавлено продукт {new.product_id} в количестве {new.quantity} '
    return False

def remove_cart_item(user_id, product_id):
    db = next(get_db())
    if user_id and product_id:
        item = db.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
        if item:
            db.delete(item)
            db.commit()
            return f'Товар {product_id} был удален'
        return 'Такого товара нет'
    return False