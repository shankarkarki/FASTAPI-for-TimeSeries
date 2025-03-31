from typing import Union
from contextlib import asynccontextmanager
from .api.db.session import init_db
from fastapi import FastAPI
from api.events import router as events_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app starts up
    init_db()
    yield

app = FastAPI()
app.include_router(events_router, prefix="/events")


@app.get("/")
def read_root():
    return {"Hello": "Shankar"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}


    