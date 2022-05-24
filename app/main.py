from typing import List

from .database import db, models
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/reviews/", response_model=List[models.ReviewSchema])
def show_Reviews():
    Reviews = db.get_reviews()
    print(Reviews)
    return Reviews

@app.post("/review/")
def update_item(item: models.ReviewSchemaBase):
    db.insert_review(item)
    return {"created"}
