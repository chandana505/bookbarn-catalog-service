from fastapi import FastAPI
from .db import Base, engine
from .routers import books

app = FastAPI(title="catalog-service")
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(books.router)
