from typing import List, Optional
from pydantic import  BaseModel , Field
from datetime import datetime

class ItemBase(BaseModel):
    name:str
    minPrice:float = Field(ge=0)
    maxPrice:float
    categoryID:int


class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id:int
    created_ar:datetime
    updated_at:datetime


class ItemPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = None


