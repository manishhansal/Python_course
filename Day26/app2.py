# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo;
MONGODB_URI = 'mongodb+srv://pythonDatabase:cL4xXuSsTpPGPm9q@cluster0.mgnrv.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# print(client.list_database_names())

#Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Manish', 'country': 'Indi', 'city': 'Motihari', 'age': 250})
print(client.list_database_names())

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

student = db.students.find_one()
print(student)

student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

students = db.students.find()
for student in students:
    print(student)

students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)


query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)

query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)
    

query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)


query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)


students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)


query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)


query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)

db.students.drop()

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
