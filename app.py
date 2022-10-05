
import pymongo 
client= pymongo.MongoClient("mongodb+srv://ahmed:workshop2022@workshop.2lgsmty.mongodb.net/?retryWrites=true&w=majority ")

# CRUD = CREATE - READ - UPDATE - DELETE
# create a database
db= client['workshop-db']
# create a collection 
col= db.employer

employer1={
 "name":"kidocode",
 "location":"mont kiara",
 "nature_of_business":"education",
 "date":"20-20-2012"   
}
employer2={
 "name":"google",
 "location":"usa",
 "nature_of_business":"stealing people data",
 "date":"20-20-2012"   
}
employer3={
 "name":"facebook",
 "location":"usa",
 "nature_of_business":"they know everythihng about you ",
 "date":"20-20-2012"   
}

# CREATE
# col.insert_one(employer1)
# col.insert_many([employer2,employer3])
# READ
for doc in col.find({}):
    print(doc)

# UPDATE

# DELETE