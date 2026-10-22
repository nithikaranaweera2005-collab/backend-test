from typing import List, Optional
from pydantic import  BaseModel , Field
from datetime import datetime

class CategoryBase(BaseModel):
    category_id:int = Field(min_length=5)
    category_code:int = Field(min_length=5)
    category_name:str = Field(min_length=0)
    description:str = Field(Optional)
    active:bool