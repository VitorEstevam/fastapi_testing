import csv
import datetime

import database.models as models

def load_db(db):
    with open("C:/Users/vitor_estevam/Desktop/r3d3/fastapi_testing/app/database/sars_2003_complete_dataset_clean.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            db_record = models.Record(
                country=row["country"],
            )
            db.add(db_record)
        db.commit()