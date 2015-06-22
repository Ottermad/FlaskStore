from app import db
from peewee import *

class Test(db.Model):
    name = CharField()
    
    @classmethod
    def get_names(cls):
        query = cls.select()
        data = []
        for item in query:
            data.append(item.name)
        return data