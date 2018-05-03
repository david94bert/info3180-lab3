from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'need_an_A'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '5ac57756fc04b2'
app.config['MAIL_PASSWORD'] = '890cf833dc343c'
mail = Mail(app)
from app import views