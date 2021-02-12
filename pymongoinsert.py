import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["mydatabases"]
mycol=mydb["customers"]
mydict={"name": "sam", "address": "Los Angeles"}
newvalues= {"$set": {"address": "Hyderabad"}}
x=mycol.update_one(mydict, newvalues)