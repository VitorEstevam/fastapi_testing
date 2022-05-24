from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String(255), index=True)


class RecordSchemaBase(BaseModel):
    country: str
    
class RecordSchema(RecordSchemaBase):
    id: int

    class Config:
        orm_mode = True

