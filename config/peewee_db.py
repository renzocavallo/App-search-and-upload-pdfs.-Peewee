from peewee import SqliteDatabase, Model

db = SqliteDatabase("db_pdf_peewee.db")

class BaseModel(Model):
    class Meta:
        database = db