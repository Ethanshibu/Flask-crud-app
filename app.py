# Imports
from flask import Flask, render_template, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# MY app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Creating the database model (Blueprint for each row in the database)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)  # Fixed capitalization
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)  # Fixed DateTime usage

    def __repr__(self):
        return f"Task {self.id}"
    
with app.app_context():
    db.create_all()

#home page
@app.route("/",methods = ['GET','POST'])   
def index():

    
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = Task(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")
            return f"Error:{e}" 
        
    # else see all current tasks
    else:
        tasks = Task.query.order_by(Task.created).all()
        return render_template("index.html", tasks=tasks)
    

@app.route("/delete/<int:id>")
def delete(id:int):
    del_task = Task.query.get_or_404(id)
    try:
        db.session.delete(del_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:  
        print(f"Error:{e}") 
        return f"Error:{e}"
    

@app.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id:int):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")
            return f"Error:{e}"
    else:
        return   render_template("edit.html", task=task) 
            




if __name__ == "__main__":  # Fixed comparison operator
    app.run(debug=True)
