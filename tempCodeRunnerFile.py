
# Imports
# render_template
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# MY app
app = Flask(__name__)
Scss(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy(app)


#creating the database model or, the blueprint for each row in the database, AKA data class
class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.column(db.String(100))
    complete = db.column(db.Integer,default=0)  
    created = db.column(db.Datetime, default=datetime.now)

    def __repr__(self):
        return f"Task {self.id}"


@app.route("/")   
def index():
    return render_template("index.html")



if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
