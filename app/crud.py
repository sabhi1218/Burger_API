from sqlalchemy.orm import Session
from . import models, schemas

BURGER_INGREDIENTS = {
    "bun": 1,
    "patty": 1,
    "lettuce": 1,
    "tomato": 1,
    "ketchup": 1,
}

def add_stock(db: Session, stock: schemas.StockCreate):
    db_item = db.query(models.Stock).filter(models.Stock.item == stock.item).first()
    if db_item:
        db_item.quantity += stock.quantity
    else:
        db_item = models.Stock(item=stock.item, quantity=stock.quantity)
        db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_burger_count(db: Session):
    stock = db.query(models.Stock).all()
    stock_dict = {item.item: item.quantity for item in stock}
    min_burgers = float("inf")
    for ingredient, required in BURGER_INGREDIENTS.items():
        if ingredient not in stock_dict or stock_dict[ingredient] < required:
            return {"burgers": 0}
        min_burgers = min(min_burgers, stock_dict[ingredient] // required)
    return {"burgers": min_burgers}


def get_stock(db: Session):
    return db.query(models.Stock).all()