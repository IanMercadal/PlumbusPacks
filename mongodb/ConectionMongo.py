import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId
​
client = MongoClient"mongodb+srv://sandbox.behmw.mongodb.net/"
db = client.get_database("Plumbus_Packs")
record = db.Plumbus_Packs
record.count.documents({})

new_student = {
    "name"
}
# seleccionamos la coleccion users
users = Plumbus_Packs.fake_users
# drop de los posibles usuarios/as
users.drop()

print(dumps(users.find_one(), indent=2))
