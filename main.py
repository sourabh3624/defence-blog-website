from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/blog database'
db=SQLAlchemy(app)


class Contacts(db.Model):


    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(12),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    phone_num=db.Column(db.String(12),nullable=False)
    mes=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(20),nullable=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=['GET','POST'])
def contact():

    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')


        entry=Contacts(name=name,phone_num=phone,email=email,date=datetime.now(),mes=message)
    
        db.session.add(entry)
        db.session.commit()
    
    
    return render_template("contact.html")

app.run(debug=True)