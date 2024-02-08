from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initaiate a flask app instance
app=Flask(__name__)
app.secret_key = "xxxx"

# DB connection string-DB engine
app.config["SQLALCHEMY_DATABASE_URI"]= "mysql+pymsql://root:experion@123@localhost/contact"

# creating a connection object to database
db=SQLAlchemy(app)

# Creating  a table for store contact information
# Automatically creates a table

class Contacts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=False,nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)
    phone_number=db.Column(db.String(12),unique=True,nullable=False)
    msg=db.Column(db.String(120),unique=False,nullable=False)
    date=db.Column(db.String(10),unique=False,nullable=False)


@app.route('/',methods=['GET'])
def contact():
        return {"Welcome":"API index"}
# run the application
if __name__ == "__main__":
    app.run(debug=True)