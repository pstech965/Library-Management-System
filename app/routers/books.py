from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_session


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# CREATE BOOK
@router.post(
    "/",
    response_model=schemas.BookResponse
)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_session)
):
    return crud.create_book(db, book)


# GET ALL BOOKS
@router.get(
    "/",
    response_model=list[schemas.BookResponse]
)
def get_books(
    db: Session = Depends(get_session)
):
    return crud.get_books(db)


# GET BOOK BY ID
@router.get(
    "/{book_id}",
    response_model=schemas.BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_session)
):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# UPDATE BOOK
@router.put(
    "/{book_id}",
    response_model=schemas.BookResponse
)
def update_book(
    book_id: int,
    book: schemas.BookCreate,
    db: Session = Depends(get_session)
):
    updated_book = crud.update_book(
        db,
        book_id,
        book
    )

    if updated_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated_book


# DELETE BOOK
@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_session)
):
    deleted_book = crud.delete_book(
        db,
        book_id
    )

    if deleted_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "message": "Book deleted successfully",
        "book_id": book_id
    }