from pymongo import MongoClient
client = MongoClient('localhost:27017')
db=client.msc
collection=db.student
print(collection.count_documents({}))
for x in collection.find()
































                             
