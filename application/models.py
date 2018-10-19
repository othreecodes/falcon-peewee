import peewee as pw
import datetime as dt
from peewee import SqliteDatabase

app_db = SqliteDatabase('database.db')

class User(pw.Model):
    id = pw.BigIntegerField(primary_key=True, unique=True)
    created = pw.DateTimeField(default=dt.datetime.now())
    name = pw.CharField(255)
    title = pw.CharField(127, null=True)
    active = pw.BooleanField(default=True)
    rating = pw.IntegerField(default=0)

    class Meta:
        database = app_db


try:
    app_db.connect()
    app_db.create_tables([User], safe=True)
    app_db.close()
except:
    pass