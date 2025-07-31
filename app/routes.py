from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/categories/", response_model=schemas.CategoryResponse)
def add_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.post("/transactions/", response_model=schemas.TransactionResponse)
def add_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)


@router.get("/transactions/", response_model=list[schemas.TransactionResponse])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip=skip, limit=limit)
