#class python fill in database data, generated dynamically or randomly for data analysis
#using this to generate 1000 records for the database

import random
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['user_database']

collection = db['users']

for i in range(1000):
    age = random.randint(18, 70)
    gender = random.choice(['male', 'female'])
    total_income = random.randint(100000, 250000)
    utilities = random.randint(950, 5000)
    entertainment = random.randint(1550, 7000)
    school_fees = random.randint(2050, 8500)
    shopping = random.randint(750, 15000)
    healthcare = random.randint(350, 12000)

    data = {
        'age': age,
        'gender': gender,
        'total_income': total_income,
        'utilities': utilities,
        'entertainment': entertainment,
        'school_fees': school_fees,
        'shopping': shopping,
        'healthcare': healthcare
    }

    collection.insert_one(data)
