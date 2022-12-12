from config.peewee_db import db, BaseModel
from peewee import CharField

class File_pdf(BaseModel):
    name = CharField(unique=True)
    path = CharField(unique=True)
    size = CharField()
    creation = CharField()

db.connect()
db.create_tables([File_pdf])