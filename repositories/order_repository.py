from typing import Optional,List
from psycopg2.extras import RealDictCursor

from db.base import get_db_connection
from models.product import ItemResponse,ItemCreate


class ItemRepository:

    def get_by_id(self, item_id: int) -> Optional[ItemResponse]:

        connection = get_db_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        cursor.execute(
            "Select * FROM items where id =%s",(item_id,)
        )

        item = cursor.fetchone()
        cursor.close()
        connection.close()

        return ItemResponse(**item) if item else None
        # BookResponse(**book) = {id:1,title: "Atomic habit"} -> BookResponse(id = 1, title = "Atomic..")

    def get_all(self,offset:int,limit:int) -> List[ItemResponse]:

        connection = get_db_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        cursor.execute(
            " Select * FROM item OFFSET %s LIMIt %s",(offset,limit)
        )

        books = cursor.fetchall()
        cursor.close()
        connection.close()

        return [ItemResponse(**item) for item in items]


    def create_item(self, item: ItemCreate) -> ItemCreate:

        connection = get_db_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        query = """
        Insert into items 
        (title,author,isbn,price,updated_at)
        Values(%s,%s,%s,%s,NULL)
        RETURNING * """

        try:
            cursor.execute(query,(item.title,item.author,item.isbn,item.price))

            new_book = cursor.fetchone()

            connection.commit()

            return ItemResponse(**new_item)

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            cursor.close()
            connection.close()

    def delete_item(self,item_id: int) -> bool:

        connection = get_db_connection()

        cursor = connection.cursor(cursor_factory=RealDictCursor)

        try:
            cursor.execute(
                "DELETE FROM books where id = %s",
                (book_id,)
            )

            connection.commit()
            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            cursor.close()
            connection.close()



