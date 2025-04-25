from flask import Flask, render_template, request, redirect, url_for
from forms import ExpensesForms
from pymongo import MongoClient

app=Flask(__name__)
app.secret_key = 'supersecret'

#client = MongoClient("mongodb://localhost:27017/") #for local machine
client = MongoClient("mongodb://mongodb:27017/") #for ec2 machine using docker container
db = client["user_database"]
users_details = db["users"]




@app.route('/', methods=["POST", "GET"])
def index():
    forms = ExpensesForms()
    if forms.validate_on_submit():
        users_details.insert_one({
            "age": forms.age.data,
            "gender": forms.gender.data,
            "total_income": forms.total_income.data,
            "utilities": forms.utilities.data,
            "entertainment": forms.entertainment.data,
            "school_fees": forms.school_fees.data,
            "shopping": forms.shopping.data,
            "healthcare": forms.healthcare.data
        })
        return redirect(url_for('success'))
    return render_template('index.html', forms=forms)


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
