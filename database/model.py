import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 这一步会生成一个叫data.sqlite的文件，就是它害得我没法重新运行文件
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    # one to many. one puppy to many toys
    # 在这里uselist自动为true
    toys = db.relationship('Toy',backref = 'puppy',lazy='dynamic')
    # one to one
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.owner:
            return f'puppy name is {self.name}, owner name is {self.owner.name}'
        else:
            return f'puppy {self.name} has no owner yet.'

    def report_toys(self):
        print('Here are my toys:')
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    # 这一部分是在制表
    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    # 这一部分是创建一条记录
    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
