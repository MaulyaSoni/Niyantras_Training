from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DB_URL = "sqlite:///employee_database.db"
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind = engine , autocommit = False)

def get_db():
    db = SessionLocal()

    try:
        yield db 

    finally:
        db.close()