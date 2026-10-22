from fastapi import FastAPI

from routers.products import routers as book_router

app = FastAPI(title="Shop POS System")

app.include_router(book_router)