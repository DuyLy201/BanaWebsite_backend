from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)

# run_with_ngrok(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dict.db'
app.config['SECRET_KEY'] ='1b253b240b0a78e764b9ec90'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from dict import routes
