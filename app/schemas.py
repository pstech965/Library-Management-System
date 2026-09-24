from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200
    )

    author: str = Field(
        min_length=1,
        max_length=100
    )

    isbn: str = Field(
        min_length=1,
        max_length=20
    )

    category: str = Field(
        min_length=1,
        max_length=100
    )

    quantity: int = Field(
        default=1,
        ge=0
    )


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    category: str
    quantity: int

    class Config:
        from_attributes = True