from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.get_database('mscit')
records=db.student
print("Count of records ",records.count_documents({}))
print("Records")
for v in records.find():
    print(v)

print("Inserting one record")
insertquery={"FirstName":"Rohit","RollNo":4,"Age":21,"Subject":"BDA"}
records.insert_one(insertquery)
for v in records.find():
    print(v)

print("Update one record")
query={"RollNo":2}
newvalues={"$set":{"Age":22}}
records.update_one(query,newvalues)
for v in records.find():
    print(v)

print("Delete one record")
records.delete_one({"RollNo":4})
for v in records.find():
    print(v)
print("Vighnesh Kargutkar MLDC 3")
