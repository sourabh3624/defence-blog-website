from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
# from flask_mail import Mail



with open("config.json","r") as c:
    params=json.load(c)['params']
local_server=True 


app = Flask(__name__, static_url_path='/static')

'''app.config.update(
    MAIL_SERVER ="smtp.gmail.com",
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME =params['gmail_user'],
    MAIL_PASSWORD =params['gmail_password']
)


mail=Mail(app)

'''


if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"]=params['prod_uri']
db=SQLAlchemy(app)


class Contacts(db.Model):


    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(12),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    phone_num=db.Column(db.String(12),nullable=False)
    mes=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(20),nullable=False)



class Posts(db.Model):


    sno=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(12),nullable=False)
    slug=db.Column(db.String(30),nullable=False)
    Content=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(20),nullable=False)
    img_file=db.Column(db.String(20),nullable=False)
@app.route("/")
def home():
    return render_template("index.html",params=params)

@app.route("/about")
def about():
    return render_template("about.html",params=params)

@app.route('/post/<string:postslug>', methods=['GET'])
def post_route(postslug):
    slug2 = str(postslug)
    post = db.session.query(Posts).filter_by(slug = slug2).first()
    return render_template('post.html', params=params, post=post)




'''
@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params=params,post=post)
'''




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
        '''
        mail.send_message('New message from'+ name,
                          sender=email,
                          recipients=[params['gmail_user']],
                          body=message+"\n"+phone)
    '''
    
    return render_template("contact.html",params=params)

app.run(debug=True)