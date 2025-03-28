from typing import List,Optional
from pydantic import BaseModel


"""
id
path
description
"""


class EventSchema(BaseModel):
    id: int
    page:Optional[str] = " "
    description:Optional[str] = " "
    
class EventCreateSchema(BaseModel):
    page: str
    

class EventUpdateSchema(BaseModel):
    description: str

class EventListSchema(BaseModel):
    results: List[EventSchema]
