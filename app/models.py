from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: int | None = Field(default=None, primary_key=True)

    title: str = Field(max_length=200)

    author: str = Field(max_length=100)

    isbn: str = Field(max_length=20, unique=True)

    category: str = Field(max_length=100)

    quantity: int = Field(default=1)