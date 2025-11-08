from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/books", tags=["books"])

@router.post("", response_model=schemas.BookOut, status_code=201)
def create_book(payload: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(**payload.dict())
    db.add(book); db.commit(); db.refresh(book)
    return book

@router.get("", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.patch("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, payload: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(book, k, v)
    db.commit(); db.refresh(book)
    return book

@router.post("/{book_id}/reserve")
def reserve_stock(book_id: int, req: schemas.ReserveRequest, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    if book.stock < req.qty:
        raise HTTPException(409, "Insufficient stock")
    book.stock -= req.qty
    db.commit()
    return {"reserved": True}
