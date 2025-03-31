from typing import List,Optional
from sqlmodel import Field, SQLModel



class EventModel(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page:Optional[str] = " "
    description:Optional[str] = " "
    
class EventCreateSchema(SQLModel):
    page: str
    

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]
