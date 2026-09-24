from sqlalchemy.orm import Session

from . import models, schemas


# CREATE
def create_book(
    db: Session,
    book: schemas.BookCreate
):
    new_book = models.Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        category=book.category,
        quantity=book.quantity
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# READ ALL
def get_books(db: Session):
    return db.query(models.Book).all()


# READ ONE
def get_book(
    db: Session,
    book_id: int
):
    return db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()


# UPDATE
def update_book(
    db: Session,
    book_id: int,
    book: schemas.BookCreate
):
    existing_book = get_book(db, book_id)

    if existing_book is None:
        return None

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.isbn = book.isbn
    existing_book.category = book.category
    existing_book.quantity = book.quantity

    db.commit()
    db.refresh(existing_book)

    return existing_book


# DELETE
def delete_book(
    db: Session,
    book_id: int
):
    existing_book = get_book(db, book_id)

    if existing_book is None:
        return None

    db.delete(existing_book)
    db.commit()

    return existing_book