#!/usr/bin/env python3

from peewee import *
from Connection_DB.connection_MYSQL_DataBase import *
from Models.base import *
from Models.user import *
from Models.message import *

# Select all records:
#with database:
#    Client.list()

# Select a single record:
#with database:
#    query = Client.get(Client.chat_id == 5828051269)
#print(query.id, type(query.chat_id), query.num)

with database:
    database.create_tables([User])
print("Done")

# CRUD
# There are 3 ways creating a new single record:
# Model.create()
# Model.save()
# Model.insert()

#with database:
#    Client.create(chat_id=5828051269, prenum=0, num=1)
#    s90 = Car(id=8, maker="Volvo", model="s90", price=50000).save(force_insert=True)
#    cerato = Car.insert(id=9, maker="KIA", model="cerato", price=20000).execute()

#with database:
#    BotMessage.list()

# There are 2 ways creating a new record:
# Model.create() in a loop:

#database = [
#    {'id': 1, 'maker': 'BMW', 'model': 'x6', 'price': 93000},
#    {'id': 2, 'maker': 'Nissan', 'model': 'Silvia', 'price': 66000}
#]

#for my_dict in database:
#    Car.create(**my_dict)

#with database:
#    Car.list()

# Method insert many
#with database:
#    data = [
#            (3, 'Roma', 'Ferrari', 220000),
#            (4, 'gt1967', 'Mustang', 80000)
#    ]
#    Car.insert_many(data, fields=[Car.id, Car.maker, Car.model, Car.price]).execute()

#with database:
#    Brand.list()

#message = """Здравствуйте, {user.first_name}!
#
#Увидел ваш комментарий под одним из постов на канале
#@maximum_profinance
#
#Для того, чтобы подобрать лучший вариант под Ваши параметры, напишите пожалуйста: квартира необходима для проживания или для сдачи в аренду?"""

# Update with save
#with database:
#    query = BotMessage(message=message, id=1).save()

# Update with update
#with database:
#    query = Car.update(model="""u"nk'no\nwn""",).where(Car.id == 1).execute()
#    Car.list()

# Delete
#with database:
#    query = Car.delete().where(Car.id == 4).execute()
#    Car.list()
