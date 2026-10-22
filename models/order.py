from typing import List, Optional
from pydantic import  BaseModel , Field
from datetime import datetime

class OrderBase(BaseModel):
    order_id:int = Field(min_length=5)
    order_date_time:datetime
    order_status:bool
    total_amount:float = Field(ge=0)
    loyalty_points_earned:float = Field(ge=0)
