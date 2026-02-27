from peewee import *
from Connection_DB.connection_MYSQL_DataBase import *

class BaseModel(Model):
    class Meta:
        order_by = id
