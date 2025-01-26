from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/stock/", response_model=schemas.StockResponse, status_code=status.HTTP_201_CREATED)
def add_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    return crud.add_stock(db, stock)


@app.get("/burgers/", response_model=schemas.BurgerCountResponse, status_code=status.HTTP_200_OK)
def get_burger_count(db: Session = Depends(get_db)):
    return crud.get_burger_count(db)

@app.get("/stock/", response_model=dict, status_code=status.HTTP_200_OK)  #list[schemas.StockResponse]
def get_stock(db: Session = Depends(get_db)):
    stock = crud.get_stock(db)
    stock_dict = {item.item: item.quantity for item in stock}
    return stock_dict
