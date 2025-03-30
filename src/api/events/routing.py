import os
from fastapi import APIRouter
from .schema import( 
EventSchema , 
EventListSchema , 
EventCreateSchema,
EventUpdateSchema)


router = APIRouter()


@router.get("/")
def read_events() -> EventListSchema:
    print(os.getenv("DATABASE_URL"))
    return {
        "results": [{"id":1},{"id":1,},{"id":1,}]
    }


@router.post("/")
def create_events(payload:EventCreateSchema)->EventSchema:
    print(payload.page)
    data = payload.model_dump()
    return {
        "id": 123 ,
        **data
    }

@router.get("/{events_id}")
def get_events(events_id: int) -> EventSchema:
    return {
       "id": events_id
    }

@router.put("/{events_id}")
def update_events(events_id: int, payload : EventUpdateSchema) -> EventSchema:
    print(payload.description)
    data = payload.model_dump()
    return {
       "id": events_id ,
       "description":payload.description,
       **data
    }

@router.delete("/{events_id}")
def delete_events(events_id: int) -> EventSchema:
    return {
       "id": events_id,
    }
