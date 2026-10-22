from typing import List, Optional
from pydantic import  BaseModel , Field
from datetime import datetime

class OrderItemBase(BaseModel):
    order_item_id:int = Field(min_length=5)
    quantity:int = Field(ge=0)
    unit_price:float = Field(gt=0)
    subtotal:int = Field(ge=0)
