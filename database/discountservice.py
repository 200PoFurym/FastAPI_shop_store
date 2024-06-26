from database.models import Discount
from database import get_db
from datetime import datetime

def create_discount(product_id, pers):
    db = next(get_db())
    data = Discount(product_id=product_id, pers=pers, reg_date=datetime.now())
    db.add(data)
    db.commit()
    return data

def get_all_discount():
    db = next(get_db())
    data = db.query(Discount).all()
    return data

def get_discount_by_product(product_id):
    db = next(get_db())
    data = db.query(Discount).filter_by(product_id=product_id).all()
    return data

def delete_discount(id):
    db = next(get_db())
    data = db.query(Discount).filter_by(id=id).first()
    db.delete(data)
    db.commit()
    return data