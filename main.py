from flask import Flask, render_template, request
import json
from flask_mail import Mail, Message

with open('config.json', 'r') as c:
    params=json.load(c)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail=Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about", methods=['GET','POST'])
def about():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        msg=Message(subject='New Song Request from'+ name,
                  sender=email,
                  recipients=[params['gmail-user']],
                  body = message+"/n"+phone
                 )
        mail.send(msg)

    return render_template("about.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

app.run(debug=True)








