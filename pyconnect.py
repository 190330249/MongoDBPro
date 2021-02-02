from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = client.employee
emp = [{"IdNO": "2440",
        "Name": "Vikram",
        "Age": "31",
        "Gender":"Male",
        "Designation":"Data Scientist",
        "Date of Joining":"21-11-2017",
        "Salary":"1.5 lac per annum",
        "Email-ID":"vicky@gmail.com"},
        {"IdNO": "2441",
         "Name": "Radhika",
         "Age": "30",
         "Gender":"Female",
         "Designation":"Database Analyst",
         "Date of Joining":"02-03-2016",
         "Salary":"2 lac per annum",
         "Email-ID":"radhika@gmail.com"}]
# Creating document
emps = db.emps
# Inserting data
emps.insert_many(emp)
# Fetching data
for i in emps.find():
    pprint.pprint(i)