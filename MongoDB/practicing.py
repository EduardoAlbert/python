import pymongo

client_connection = pymongo.MongoClient()

db = client_connection.users

""" 
db.create_collection('user') """

""" 
db.user.insert_one({
  'name':'Eduardo',
  'age': 18,
  'state': 'São Paulo'
}) """

user = db.user.find_one()

print(user['name'])

print(db.list_collection_names())


