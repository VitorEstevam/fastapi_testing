from typing import List

from .database import db, models
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/records/", response_model=List[models.RecordSchema])
def show_records():
    records = db.get_records()
    print(records)
    return records

@app.post("/record/")
def update_item(item: models.RecordSchemaBase):
    db.insert_record(item.country)
    return {item.country+" created"}
