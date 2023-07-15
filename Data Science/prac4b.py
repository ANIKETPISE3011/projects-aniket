from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.get_database('mscit')
records=db.student
print("Count of records ",records.count_documents({}))
print("Records")
for v in records.find():
    print(v)

print("Inserting manu record")
insertquery=[{"FirstName":"Joyel","RollNo":4,"Age":22,"Subject":"CC"},
             {"FirstName":"Jake","RollNo":5,"Age":22,"Subject":"CC"},
             {"FirstName":"Rachel","RollNo":6,"Age":21,"Subject":"MSA"}]
records.insert_many(insertquery)
for v in records.find():
    print(v)

print("Update many record")
query={"Subject":"CC"}
newvalues={"$set":{"Subject":"MN"}}
records.update_many(query,newvalues)
for v in records.find():
    print(v)

print("Delete many record")
records.delete_many({"Subject":"MN"})
for v in records.find():
    print(v)
print("Vighnesh Kargutkar MLDC 3")
