
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
database = client["test_db"]
collection = database["test_collection"]

# collection.insert_one({"name": "Alice", "age": 25})
# collection.insert_many([
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 22}
# ])

print('\nread test')

user = collection.find_one({"name": "Alice"})
print(user)

for user in collection.find():
    print(user)

print('\nupdate test')

collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

for user in collection.find():
    print(user)

print('\ndelete test')
# collection.delete_one({"name": "Charlie"})

for user in collection.find():
    print(user)
    

