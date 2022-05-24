import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Review, ReviewSchemaBase

engine = create_engine("sqlite:///mydb.db", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

def get_reviews():
    db = SessionLocal()

    values = db.query(Review).all()

    db.close()
    return values

def insert_review(param: ReviewSchemaBase):
    db = SessionLocal()

    entry = Review(
        entry = param.entry,
        language = param.language,
        positive = param.positive
    )

    db.add(entry)
    db.commit()