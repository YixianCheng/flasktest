import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLLCHEMY_TRACK_MODIFICATIONS'] = False

# 就是app.py里导入的那个db
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
