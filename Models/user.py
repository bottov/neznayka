from peewee import *
from Connection_DB.connection_MYSQL_DataBase import *
from Models.base import *

class User(BaseModel):
    chat_id = CharField(unique=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)

    @staticmethod
    def list():
        query = User.select()
        for row in query:
            print(row.id, row.chat_id)

    class Meta:
        database = database
        db_table = "users"
