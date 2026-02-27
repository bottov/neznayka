from peewee import *
from Connection_DB.connection_MYSQL_DataBase import *
from Models.base import *
from datetime import datetime

class Message(BaseModel):
    chat_id = CharField(null=True, default=0)
    text = TextField(default=False)
    datetime = DateTimeField(null=False, default=datetime.now())

    @staticmethod
    def list():
        query = Message.select()
        for row in query:
            print(row.chat_id, row.text)

    class Meta:
        database = database
        db_table = "messages"
