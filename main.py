from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, URL
from datetime import date
import smtplib

my_email = "rickkleinjan.rk@gmail.com"
my_password = "wpac oblp zjgw zmqr"

app = Flask(__name__)



# SET UP A ENV SECRET KEY
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    email = EmailField(validators=[DataRequired()], render_kw={"placeholder": "Your Email"})
    subject = StringField(validators=[DataRequired()], render_kw={"placeholder": "Subject"})
    message = TextAreaField(validators=[DataRequired()], render_kw={"placeholder": "Message"})
    submit = SubmitField()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact",methods=["POST", "GET"])
def contact():
    contact_form = ContactForm()
    
    if contact_form.validate_on_submit():
        with smtplib.SMTP("gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: {contact_form.subject.data} \\n{contact_form.message.data}"
        )
    
    
    return render_template("contact.html", form=contact_form)

@app.route("/feature")
def feature():
    return render_template("feature.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")

@app.route("/countdown")
def countdown():
    return render_template("countdown.html")

if __name__ == "__main__":
    app.run(debug=True)