from typing import List, Optional
from pydantic import  BaseModel , Field
from datetime import datetime


class CustomerBase(BaseModel):
    customer_id:str
    mobile_number:int = Field(...,max_length=10)
    full_name:str = Field(min_length=1)
    email:str = Field(min_length=5)
    loyalty_points:int = Field(ge=0)
    registered_at:datetime