from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str
    author: str
    price: int = Field(ge=0)
    stock: int = Field(ge=0)

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: int | None = Field(default=None, ge=0)
    stock: int | None = Field(default=None, ge=0)

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    price: int
    stock: int
    class Config:
        from_attributes = True

class ReserveRequest(BaseModel):
    qty: int = Field(ge=1)
