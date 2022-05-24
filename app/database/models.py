from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = "Reviews"

    id = Column(Integer, primary_key=True, index=True)
    entry = Column(String(255), index=True)
    language = Column(String(50), index=True)
    positive = Column(Boolean, index=True)

class ReviewSchemaBase(BaseModel):
    entry: str
    language: str
    positive: bool
    
class ReviewSchema(ReviewSchemaBase):
    id: int

    class Config:
        orm_mode = True

