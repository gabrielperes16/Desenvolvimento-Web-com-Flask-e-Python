from peewee import Model, CharField,DateTimeField
from database.database import db
from datetime import datetime

class cliente(Model):
    name = CharField()
    email = CharField()
    data_criacao = DateTimeField(default=datetime.now)

    class Meta:
        database = db