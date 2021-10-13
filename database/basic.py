import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> 1.py
# os.path.dirname(__file__) --> flasktest/database/1.py
# os.path.abspath(os.path.dirname(__file__)) --> C:\Users\CST\AppData\Local\atom\flasktest\database\1.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db) # connect the application with my db

class Puppy(db.Model):

    # manual table name choice
    __tablename__ = 'puppies'

    # 这个id是不允许重复的，它是数字
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text) # name是text
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old.'
