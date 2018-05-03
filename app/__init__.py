from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'need_an_A'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'took out username and password'
app.config['MAIL_PASSWORD'] = 'took out username and password'
mail = Mail(app)
from app import views