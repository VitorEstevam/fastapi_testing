import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Record

engine = create_engine("sqlite:///mydb.db", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

def get_records():
    db = SessionLocal()

    values = db.query(Record).all()

    db.close()
    return values

def insert_record(countryName: string):
    db = SessionLocal()

    db_record = Record(
        country=countryName,
    )

    db.add(db_record)
    db.commit()