
from sqlmodel import create_engine, Session, SQLModel



if DATABASE_URL == "":
    raise   NotImplementedError("DATABASE_URL is meant to be set in the environment")



engine = create_engine(DATABASE_URL)

def init_db():
    print("Initializing database")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
