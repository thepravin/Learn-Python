from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,URL
from dotenv import load_dotenv
import os

load_dotenv()

db_url = URL.create(
    "postgresql+psycopg",
    username=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["POSTGRES_HOST"],
    port= os.environ["POSTGRES_PORT"],
    database=os.environ["POSTGRES_DB"] ,
)
engine = create_engine(db_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()