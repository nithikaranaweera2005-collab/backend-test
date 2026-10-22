from typing import Optional, List

from fastapi import APIRouter

from models.product import ItemResponse, ItemCreate
from repositories.order_repository import ItemRepository
from services.product_service import ItemService

router = APIRouter(prefix="/books",tags=["books"])

repo = ItemRepository()
service = ItemService(repo)


@router.get("/{book_id}",response_model=Optional[ItemResponse])
def get_book(book_id: int):
    return service.get_by_id(book_id)

@router.get("",response_model=List[ItemResponse])
def get_all(offset:int = 0, limit: int = 10):
    return service.get_all_books(offset, limit)


@router.post("/",response_model=ItemResponse)
def create_book(request:ItemCreate):
    return service.create_book(request)


@router.delete("/{book_id}",response_model=Optional[ItemResponse])
def delete_book(book_id:int):
    return service.delete_book(book_id)

def update_book(book_id:int,book:ItemCreate):
    return service.update_book()

