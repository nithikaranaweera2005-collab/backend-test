from dataclasses import dataclass
from typing import Optional

from starlette import status
from starlette.exceptions import HTTPException

from models.product import ItemResponse, ItemCreate
from repositories.order_repository import ItemRepository


class ItemService:

    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def get_by_id(self, item_id: int) -> Optional[ItemResponse]:

        item = self.repo.get_by_id(item_id)

        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item Not Found")

        return item


    def get_all_books(self,offset:int = 0, limit:int = 10):

        books = self.repo.get_all(offset,limit)

        if not books:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")

        return books

    def create_book(self, book:ItemCreate):

        try:
            return self.repo.create_item(item)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def delete_item(self,item_id:int):

        try:

            deleted = self.repo.delete_item(item_id)

            if not deleted:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")

            return True

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def update_item(self, item_id: int,book:ItemCreate):

        try:

             updated = self.repo.update_item(item_id,item)

             if not updated:
                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")

             return updated

         except Exception as e:
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

