import os
from fastapi import APIRouter
from .models import( 
EventModel , 
EventListSchema , 
EventCreateSchema,
EventUpdateSchema)

from api.db.config import DATABASE_URL

router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    print(os.getenv("DATABASE_URL"),DATABASE_URL)
    return {
        "results": [{"id":1},{"id":1,},{"id":1,}]
    }


@router.post("/")
def create_events(payload:EventCreateSchema)->EventModel:
    print(payload.page)
    data = payload.model_dump()
    return {
        "id": 123 ,
        **data
    }

@router.get("/{events_id}")
def get_events(events_id: int) -> EventModel:
    return {
       "id": events_id
    }

@router.put("/{events_id}")
def update_events(events_id: int, payload : EventUpdateSchema) -> EventModel:
    print(payload.description)
    data = payload.model_dump()
    return {
       "id": events_id ,
       "description":payload.description,
       **data
    }

@router.delete("/{events_id}")
def delete_events(events_id: int) -> EventModel:
    return {
       "id": events_id,
    }
